import asyncio
from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


async def main():
    ctx = DomainContext.create(
        root_domain="example.com",
        recon_mode="full",
        ai_enabled=False
    )

    orch = Orchestrator(ctx)
    await orch.run_passive()
    await orch.run_certificates()
    await orch.run_active()

    orch.finalize()


if __name__ == "__main__":
    asyncio.run(main())
