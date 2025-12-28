# netra/passive/search.py

import requests
from typing import List, Dict, Set


class PassiveRecon:
    def __init__(self, root_domain: str):
        self.root_domain = root_domain

    def from_crtsh(self) -> Set[str]:
        """
        Fetch subdomains from crt.sh
        """
        url = f"https://crt.sh/?q=%25.{self.root_domain}&output=json"
        subdomains = set()

        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            for entry in data:
                name_value = entry.get("name_value", "")
                for sub in name_value.split("\n"):
                    sub = sub.strip().lower()
                    if sub.endswith(self.root_domain):
                        subdomains.add(sub)

        except Exception:
            pass  # passive recon must never crash

        return subdomains

    def run(self) -> List[Dict]:
        """
        Run all passive sources and return structured results
        """
        results = []

        for sub in self.from_crtsh():
            results.append({
                "subdomain": sub,
                "source": "crtsh",
                "method": "passive"
            })

        return results
