# netra/core/validator.py

from typing import List, Dict


class Validator:
    """
    Final validation layer.
    Decides which assets survive into final output.
    """

    MIN_CONFIDENCE = 0.4

    def validate(self, correlated_results: List[Dict]) -> List[Dict]:
        validated = []

        for item in correlated_results:
            # Rule 1: must have domain
            if not item.get("domain"):
                continue

            # Rule 2: must have IPs
            ips = item.get("ips", [])
            if not ips:
                continue

            # Rule 3: confidence threshold
            if item.get("confidence", 0) < self.MIN_CONFIDENCE:
                continue

            # Rule 4: at least one source
            if not item.get("sources"):
                continue

            validated.append(item)

        return validated
