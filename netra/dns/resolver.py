# netra/dns/resolver.py

import asyncio
import dns.resolver
from typing import List, Dict
from netra.core.task_engine import TaskEngine


DEFAULT_TIMEOUT = 3.0
DEFAULT_RETRIES = 2
DEFAULT_CONCURRENCY = 50


class DNSResolver:
    """
    Phase 1.2 DNS Resolver
    - Single resolve (backward compatible)
    - Batch resolve (high performance)
    """

    def __init__(
            self,
            timeout:float = DEFAULT_TIMEOUT,
            retries:int = DEFAULT_RETRIES, 
            concurrency:int = DEFAULT_CONCURRENCY
):
        self.resolver = dns.resolver.Resolver()
        self.resolver.lifetime = timeout
        self.retries = retries

        # Phase 1 async control
        self.engine = TaskEngine(concurrency)


        self.resolver.nameservers= [
            "8.8.8.8",   # Google DNS
            "1.1.1.1",   # Cloudflare DNS
            "9.9.9.9"    # Quad9 DNS
        ]

    

    
    async def resolve_one(self, domain: str) -> Dict:
        """
        Core DNS logic for one domain
        """
        for attempt in range(self.retries):
            try:
                answers = await asyncio.to_thread(
                    self.resolver.resolve, domain, "A"
                )

                return {
                    "domain": domain,
                    "resolved": True,
                    "ips": [r.address for r in answers],
                }

            except dns.resolver.NXDOMAIN:
                return {
                    "domain": domain,
                    "resolved": False,
                    "reason": "NXDOMAIN",
                }

            except dns.resolver.Timeout:
                if attempt == self.retries - 1:
                    return {
                        "domain": domain,
                        "resolved": False,
                        "reason": "TIMEOUT",
                    }

            except Exception as e:
                return {
                    "domain": domain,
                    "resolved": False,
                    "reason": str(e),
                }

        return {
            "domain": domain,
            "resolved": False,
            "reason": "UNKNOWN_FAILURE",
        }

    async def resolve(self, domain: str) -> Dict:
        """
        Phase 0 compatible API
        """
        return await self.resolve_one(domain)

    async def resolve_batch(self, domains: List[str]) -> List[Dict]:
        """
        Phase 1.2: Resolve many domains concurrently
        """
        return await self.engine.run(self.resolve_one, domains)
        async def validate_domains_batch(self, domains: list) -> list:
         """
            Phase 1.2 batch DNS validation
        """
        return await self.dns_resolver.resolve_batch(domains)
