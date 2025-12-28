# netra/dns/_test_dns.py

import asyncio
from netra.dns.resolver import DNSResolver
from netra.dns.wildcard import WildcardDetector


async def main():
    resolver = DNSResolver(timeout=2.0, retries=2)
    wildcard_detector = WildcardDetector(resolver)

    test_domain = "example.com"

    print("\n[DNS RESOLUTION TEST]")
    result = await resolver.resolve(test_domain)
    print(result)

    print("\n[WILDCARD DNS TEST]")
    has_wildcard = await wildcard_detector.has_wildcard(test_domain)
    print("Wildcard Present:", has_wildcard)


if __name__ == "__main__":
    asyncio.run(main())
