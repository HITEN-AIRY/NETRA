from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


context = DomainContext.create(
    root_domain="example.com",
    recon_mode="hybrid",
    ai_enabled=True
)

orch = Orchestrator(context)

# Simulated correlated data
orch.results["passive"] = [
    {
        "domain": "api.example.com",
        "ips": ["1.1.1.1"],
        "source": "crtsh",
        "method": "passive",
        "confidence": 0.3  # low
    },
    {
        "domain": "admin.example.com",
        "ips": ["2.2.2.2"],
        "source": "wordlist",
        "method": "active",
        "confidence": 0.7
    }
]

final = orch.validate_results()

print("\n[VALIDATED RESULTS]")
for r in final:
    print(r)
