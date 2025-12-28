# netra/core/orchestrator.py

from netra.core.context import DomainContext
from netra.dns.resolver import DNSResolver
from netra.dns.wildcard import WildcardDetector

from netra.passive.search import PassiveRecon
from netra.certs.ct_parser import CertificateParser
from netra.active.enumerator import ActiveEnumerator
from netra.intelligence.scorer import AIScorer

from netra.core.correlator import Correlator

from netra.core.correlator import Correlator
from netra.core.validator import Validator

from netra.output.writer import OutputWriter





class Orchestrator:
    def __init__(self, context: DomainContext):
        self.context = context

        # DNS Core
        self.dns_resolver = DNSResolver()
        self.wildcard_detector = WildcardDetector(self.dns_resolver)

        # Results storage
        self.results = {
            "passive": [],
            "active": [],
            "bruteforce": [],
            "validated": []
        }

    async def validate_domain(self, domain: str) -> dict:
        """Central DNS validation point"""
        return await self.dns_resolver.resolve(domain)

    async def check_wildcard(self) -> bool:
        """Check wildcard DNS once per run"""
        return await self.wildcard_detector.has_wildcard(
            self.context.root_domain
        )

    async def run_passive(self):
        """STEP 0.4 – Passive Recon"""
        print("[*] Running Passive Recon")

        recon = PassiveRecon(self.context.root_domain)
        candidates = recon.run()

        print(f"[*] Passive candidates found: {len(candidates)}")

        for item in candidates:
            sub = item["subdomain"]
            result = await self.validate_domain(sub)

            if result.get("resolved"):
                result["source"] = item["source"]
                result["method"] = item["method"]
                self.results["passive"].append(result)

        self.run_intelligence()

    async def run_certificates(self):
        """STEP 0.5 – Certificate Transparency Parsing"""
        print("[*] Running Certificate Parsing")

        parser = CertificateParser(self.context.root_domain)
        candidates = parser.run()

        print(f"[*] Certificate candidates found: {len(candidates)}")

        for item in candidates:
            sub = item["subdomain"]
            result = await self.validate_domain(sub)

            if result.get("resolved"):
                result["source"] = item["source"]
                result["method"] = item["method"]
                self.results["passive"].append(result)

        self.run_intelligence()

    async def run_active(self):
        """STEP 0.6 – Active Enumeration (AI-assisted, DNS-first)"""
        print("[*] Running Active Enumeration")

        # Skip if wildcard DNS exists
        if await self.check_wildcard():
            print("[!] Wildcard DNS detected — skipping active enum")
            return

        # Use passive intelligence for AI expansion
        known = [r["domain"] for r in self.results["passive"]]

        enumerator = ActiveEnumerator(
            self.context.root_domain,
            ai_enabled=self.context.ai_enabled,
            known_domains=known
        )

        candidates = enumerator.generate_candidates()
        print(f"[*] Active candidates generated: {len(candidates)}")

        for sub in candidates:
            result = await self.validate_domain(sub)

            if result.get("resolved"):
                result["source"] = "wordlist"
                result["method"] = "active"
                self.results["active"].append(result)

    def run_intelligence(self):
        """Phase-0 AI scoring layer"""
        scorer = AIScorer()
        self.results["passive"] = scorer.score(self.results["passive"])

    def correlate_results(self):
        """
         STEP 0.8 – Correlate & deduplicate all results
        """
        correlator = Correlator()
        return correlator.correlate(self.results)
    
    def validate_results(self):
        """
        STEP 0.9 – Final validation layer
        """
        correlator = Correlator()
        validator = Validator()

        correlated = correlator.correlate(self.results)
        validated = validator.validate(correlated)

        return validated

    def finalize(self):
        """
        STEP 0.10 – Final output & recon memory
        """
        validated = self.validate_results()

        writer = OutputWriter(self.context.root_domain)
        output_file = writer.write_json(validated)

        print(f"[+] Final recon output written to: {output_file}")

        return output_file



