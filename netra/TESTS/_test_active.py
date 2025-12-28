import asyncio
from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


async def main():
    context = DomainContext.create(
        root_domain="example.com",
        recon_mode="active",
        ai_enabled=False
    )

    orch = Orchestrator(context)
    await orch.run_active()

    print("\n[ACTIVE RESULTS]")
    for r in orch.results["active"]:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
