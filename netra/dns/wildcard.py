# netra/dns/wildcard.py

import random
import string
from netra.dns.resolver import DNSResolver


class WildcardDetector:
    def __init__(self, resolver: DNSResolver):
        self.resolver = resolver

    def _random_subdomain(self, root_domain: str) -> str:
        rand = ''.join(random.choices(string.ascii_lowercase, k=12))
        return f"{rand}.{root_domain}"

    async def has_wildcard(self, root_domain: str) -> bool:
        """
        Detect wildcard DNS by resolving random subdomains.
        """
        test_domain = self._random_subdomain(root_domain)
        result = await self.resolver.resolve(test_domain)

        return result["resolved"]

'''
Logic (simple but powerful)

Generate a random subdomain

Resolve it

If it resolves → wildcard exists

This prevents:

False positives

Massive noise

Fake discoveries

'''