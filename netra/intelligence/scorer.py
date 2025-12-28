# netra/intelligence/scorer.py

from typing import List, Dict


class AIScorer:
    """
    Phase-0 Intelligence Scorer
    Heuristic-based (no LLM yet)
    """

    def score(self, passive_results: List[Dict]) -> List[Dict]:
        for item in passive_results:
            domain = item.get("domain", "")

            score = 0.3  # base confidence

            keywords = [
                "admin", "api", "dev", "test",
                "staging", "internal", "portal"
            ]

            for kw in keywords:
                if kw in domain:
                    score += 0.15

            item["confidence"] = min(score, 0.95)

        return passive_results
