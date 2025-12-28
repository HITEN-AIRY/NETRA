# netra/intelligence/wordlist_expander.py

from typing import List, Set


class AIWordlistExpander:
    """
    Phase-0 AI Wordlist Expansion
    Pattern-based (no LLM yet)
    """

    COMMON_PATTERNS = [
        "api",
        "admin",
        "auth",
        "internal",
        "portal",
        "dashboard",
        "dev",
        "test",
        "staging",
        "beta",
        "secure",
        "private"
    ]

    def expand(self, discovered_domains: List[str]) -> Set[str]:
        """
        Generate new words based on discovered subdomains
        """
        generated = set()

        for domain in discovered_domains:
            prefix = domain.split(".")[0]

            # Pattern: api-v2, api-dev, admin-test
            for pattern in self.COMMON_PATTERNS:
                if prefix != pattern:
                    generated.add(f"{pattern}")
                    generated.add(f"{prefix}-{pattern}")
                    generated.add(f"{pattern}-{prefix}")

        return generated


'''
🧠 WHY THIS IS SMART (NOT NOISY)

Learns from real assets

Produces small, high-quality expansions

Avoids massive wordlists

Perfect for bug bounty & red teaming


'''