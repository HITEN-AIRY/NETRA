# netra/certs/ct_parser.py

import requests
from typing import Set, List, Dict


class CertificateParser:
    """
    Parses Certificate Transparency logs
    to extract subdomains (Amass-style)
    """

    def __init__(self, root_domain: str):
        self.root_domain = root_domain

    def fetch_ct_logs(self) -> List[Dict]:
        """
        Fetch raw certificate data from crt.sh
        """
        url = f"https://crt.sh/?q=%25.{self.root_domain}&output=json"

        try:
            response = requests.get(url, timeout=15)
            return response.json()
        except Exception:
            return []

    def extract_domains(self) -> Set[str]:
        """
        Extract and normalize domains from certificates
        """
        domains = set()
        data = self.fetch_ct_logs()

        for entry in data:
            name_value = entry.get("name_value", "")
            for domain in name_value.split("\n"):
                domain = domain.strip().lower()

                # Remove wildcard
                if domain.startswith("*."):
                    domain = domain[2:]

                if domain.endswith(self.root_domain):
                    domains.add(domain)

        return domains

    def run(self) -> List[Dict]:
        """
        Structured, source-tagged output
        """
        results = []

        for domain in self.extract_domains():
            results.append({
                "subdomain": domain,
                "source": "certificate",
                "method": "ct-log"
            })

        return results
