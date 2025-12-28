# netra/core/context.py

from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass(frozen=True)
class DomainContext:
    run_id: str
    root_domain: str
    recon_mode: str
    ai_enabled: bool
    created_at: datetime

    @staticmethod
    def create(root_domain: str, recon_mode: str, ai_enabled: bool):
        return DomainContext(
            run_id=str(uuid.uuid4()),
            root_domain=root_domain,
            recon_mode=recon_mode,
            ai_enabled=ai_enabled,
            created_at=datetime.utcnow()
        )


''' 
You never “run” context.py
It is a library file, not an executable.

Only cli.py is executed.

S
'''