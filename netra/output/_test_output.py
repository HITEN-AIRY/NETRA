from netra.core.context import DomainContext
from netra.core.orchestrator import Orchestrator


context = DomainContext.create(
    root_domain="example.com",
    recon_mode="hybrid",
    ai_enabled=True
)

orch = Orchestrator(context)

# Simulate final validated results
orch.results["passive"] = [
    {
        "domain": "admin.example.com",
        "ips": ["2.2.2.2"],
        "source": "wordlist",
        "method": "active",
        "confidence": 0.8
    }
]

output = orch.finalize()
print("Output file:", output)
