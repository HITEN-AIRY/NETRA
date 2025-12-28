# netra/core/correlator.py

from typing import Dict, List


class Correlator:
    """
    Correlates and deduplicates recon results
    from multiple sources into a single view
    """

    def correlate(self, results: Dict[str, List[Dict]]) -> List[Dict]:
        """
        Input:
            results = {
                "passive": [...],
                "active": [...],
                ...
            }

        Output:
            deduplicated list of domains
        """
        merged = {}

        for phase, items in results.items():
            for item in items:
                domain = item.get("domain")
                if not domain:
                    continue

                if domain not in merged:
                    merged[domain] = {
                        "domain": domain,
                        "ips": set(item.get("ips", [])),
                        "sources": set([item.get("source")]),
                        "methods": set([item.get("method")]),
                        "confidence": item.get("confidence", 0.0)
                    }
                else:
                    merged[domain]["ips"].update(item.get("ips", []))
                    merged[domain]["sources"].add(item.get("source"))
                    merged[domain]["methods"].add(item.get("method"))
                    merged[domain]["confidence"] = max(
                        merged[domain]["confidence"],
                        item.get("confidence", 0.0)
                    )

        # Normalize output
        final_results = []
        for data in merged.values():
            final_results.append({
                "domain": data["domain"],
                "ips": list(data["ips"]),
                "sources": sorted(data["sources"]),
                "methods": sorted(data["methods"]),
                "confidence": round(data["confidence"], 2)
            })

        return final_results
