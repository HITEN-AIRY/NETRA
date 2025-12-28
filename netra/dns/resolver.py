# netra/dns/resolver.py

import asyncio
import dns.resolver
import dns.exception
from typing import Dict, Any


class DNSResolver:
    def __init__(self, timeout: float = 2.0, retries: int = 2):
        self.resolver = dns.resolver.Resolver()
        self.resolver.lifetime = timeout
        self.retries = retries

    async def resolve(self, domain: str) -> Dict[str, Any]:
        """
        Resolve a domain asynchronously.
        Always returns a structured result.
        """

        for attempt in range(self.retries):
            try:
                answers = await asyncio.to_thread(
                    self.resolver.resolve, domain, "A"
                )

                ips = [rdata.address for rdata in answers]
                return {
                    "domain": domain,
                    "resolved": True,
                    "ips": ips
                }

            except dns.resolver.NXDOMAIN:
                return {
                    "domain": domain,
                    "resolved": False,
                    "reason": "NXDOMAIN"
                }

            except dns.exception.Timeout:
                # retry until last attempt
                if attempt == self.retries - 1:
                    return {
                        "domain": domain,
                        "resolved": False,
                        "reason": "TIMEOUT"
                    }

            except Exception as e:
                return {
                    "domain": domain,
                    "resolved": False,
                    "reason": str(e)
                }

        # 🔒 GUARANTEED RETURN (satisfies Pylance + safety)
        return {
            "domain": domain,
            "resolved": False,
            "reason": "UNKNOWN_ERROR"
        }
