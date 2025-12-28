from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


# Fake test to simulate multiple sources
context = DomainContext.create(
    root_domain="example.com",
    recon_mode="hybrid",
    ai_enabled=True
)

orch = Orchestrator(context)

orch.results["passive"] = [
    {
        "domain": "api.example.com",
        "ips": ["1.1.1.1"],
        "source": "crtsh",
        "method": "passive",
        "confidence": 0.6
    }
]

orch.results["active"] = [
    {
        "domain": "api.example.com",
        "ips": ["1.1.1.1"],
        "source": "wordlist",
        "method": "active",
        "confidence": 0.8
    }
]

final = orch.correlate_results()

print("\n[CORRELATED RESULTS]")
for r in final:
    print(r)
