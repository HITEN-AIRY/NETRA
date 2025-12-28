import asyncio
from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


async def main():
    print("[TEST] Starting Passive Recon Test")  # 👈 IMPORTANT

    context = DomainContext.create(
        root_domain="google.com",
        recon_mode="passive",
        ai_enabled=False
    )

    orch = Orchestrator(context)
    await orch.run_passive()

    print("\n[PASSIVE RESULTS]")
    for r in orch.results["passive"]:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
