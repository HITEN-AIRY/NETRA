import time
from typing import List

from netra.core.context import DomainContext
from netra.dns.resolver import DNSResolver
from netra.dns.wildcard import WildcardDetector

from netra.passive.search import PassiveRecon
from netra.certs.ct_parser import CertificateParser
from netra.active.enumerator import ActiveEnumerator
from netra.intelligence.scorer import AIScorer

from netra.core.correlator import Correlator
from netra.core.validator import Validator
from netra.output.writer import OutputWriter


class Orchestrator:
    """
    Central control unit for NETRA
    """

    def __init__(self, context: DomainContext):
        self.context = context

        # DNS core
        self.dns_resolver = DNSResolver()
        self.wildcard_detector = WildcardDetector(self.dns_resolver)

        # Unified results store
        self.results = {
            "passive": [],
            "active": [],
            "bruteforce": [],
            "validated": [],
        }

    # ---------- DNS ----------

    async def validate_domain(self, domain: str) -> dict:
        return await self.dns_resolver.resolve(domain)

    async def validate_domains_batch(self, domains: List[str]) -> list:
        return await self.dns_resolver.resolve_batch(domains)

    async def check_wildcard(self) -> bool:
        return await self.wildcard_detector.has_wildcard(
            self.context.root_domain
        )

    # ---------- Passive ----------

    async def run_passive(self):
        start = time.perf_counter()
        print("[*] Running Passive Recon")

        recon = PassiveRecon(self.context.root_domain)
        candidates = recon.run()

        if not candidates:
            print("[*] No passive candidates found")
            return

        subdomains = list(set(item["subdomain"] for item in candidates))
        dns_results = await self.validate_domains_batch(subdomains)
        dns_map = {r["domain"]: r for r in dns_results if r.get("resolved")}

        for item in candidates:
            domain = item["subdomain"]
            if domain in dns_map:
                result = dns_map[domain]
                result.update({
                    "source": item.get("source"),
                    "method": item.get("method"),
                })
                self.results["passive"].append(result)

        self.run_intelligence()

        elapsed = time.perf_counter() - start
        print(f"[METRIC] Passive recon took {elapsed:.2f}s")

    # ---------- Certificates ----------

    async def run_certificates(self):
        start = time.perf_counter()
        print("[*] Running Certificate Parsing")

        parser = CertificateParser(self.context.root_domain)
        candidates = parser.run()

        if not candidates:
            print("[*] No certificate candidates found")
            return

        subdomains = list(set(item["subdomain"] for item in candidates))
        dns_results = await self.validate_domains_batch(subdomains)
        dns_map = {r["domain"]: r for r in dns_results if r.get("resolved")}

        for item in candidates:
            domain = item["subdomain"]
            if domain in dns_map:
                result = dns_map[domain]
                result.update({
                    "source": item.get("source"),
                    "method": item.get("method"),
                })
                self.results["passive"].append(result)

        self.run_intelligence()

        elapsed = time.perf_counter() - start
        print(f"[METRIC] Certificate parsing took {elapsed:.2f}s")

    # ---------- Active ----------

    async def run_active(self):
        start = time.perf_counter()
        print("[*] Running Active Enumeration")

        if await self.check_wildcard():
            print("[!] Wildcard DNS detected — skipping active enum")
            return

        known = [r["domain"] for r in self.results["passive"]]

        enumerator = ActiveEnumerator(
            self.context.root_domain,
            ai_enabled=self.context.ai_enabled,
            known_domains=known,
        )

        candidates = enumerator.generate_candidates()

        if not candidates:
            print("[*] No active candidates generated")
            return

        print(f"[*] Active candidates generated: {len(candidates)}")

        results = await self.validate_domains_batch(candidates)

        for result in results:
            if result.get("resolved"):
                result.update({
                    "source": "wordlist",
                    "method": "active",
                })
                self.results["active"].append(result)

        elapsed = time.perf_counter() - start
        print(f"[METRIC] Active enum took {elapsed:.2f}s")

    # ---------- Intelligence ----------

    def run_intelligence(self):
        scorer = AIScorer()
        self.results["passive"] = scorer.score(self.results["passive"])

    # ---------- Correlation ----------

    def correlate_results(self) -> list:
        return Correlator().correlate(self.results)

    # ---------- Validation ----------

    def validate_results(self) -> list:
        correlated = self.correlate_results()
        return Validator().validate(correlated)

    # ---------- Output ----------

    def _normalize(self, results: list) -> list:
        for r in results:
            r.setdefault("ips", [])
            r.setdefault("source", None)
            r.setdefault("method", None)
            r.setdefault("reason", None)
        return results

    def finalize(self):
        validated = self._normalize(self.validate_results())
        output_file = OutputWriter(self.context.root_domain).write_json(validated)
        print(f"[+] Final recon output written to: {output_file}")
        return output_file
