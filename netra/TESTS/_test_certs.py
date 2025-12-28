# netra/certs/_test_certs.py

import asyncio
print("[FILE LOADED] _test_certs.py")

from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


async def main():
    print("[TEST] Starting Certificate Parsing Test")

    context = DomainContext.create(
        root_domain="example.com",
        recon_mode="passive",
        ai_enabled=False
    )

    orch = Orchestrator(context)

    print("[TEST] Calling run_certificates()")
    await orch.run_certificates()

    print("\n[CERTIFICATE RESULTS]")
    if not orch.results["passive"]:
        print("No certificate-based results found.")
    else:
        for r in orch.results["passive"]:
            print(r)


if __name__ == "__main__":
    asyncio.run(main())
