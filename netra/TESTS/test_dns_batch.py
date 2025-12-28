import asyncio
from netra.dns.resolver import DNSResolver


async def main():
    resolver = DNSResolver(concurrency=10)

    domains = [
        "google.com",
        "mail.google.com",
        "doesnotexist123.google.com"
    ]

    results = await resolver.resolve_batch(domains)

    print("\nDNS Batch Results:")
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
