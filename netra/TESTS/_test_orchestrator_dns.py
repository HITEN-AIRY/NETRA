# netra/core/_test_orchestrator_dns.py

import asyncio
from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


async def main():
    context = DomainContext.create(
        root_domain="example.com",
        recon_mode="hybrid",
        ai_enabled=False
    )

    orchestrator = Orchestrator(context)

    print("\n[DNS VALIDATION VIA ORCHESTRATOR]")
    result = await orchestrator.validate_domain("www.example.com")
    print(result)

    print("\n[WILDCARD CHECK]")
    wildcard = await orchestrator.check_wildcard()
    print("Wildcard:", wildcard)


if __name__ == "__main__":
    asyncio.run(main())
