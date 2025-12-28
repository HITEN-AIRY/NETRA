# netra/output/writer.py

import json
from datetime import datetime
from typing import List, Dict
from pathlib import Path


class OutputWriter:
    """
    Handles final output and recon memory storage
    """

    def __init__(self, target: str, output_dir: str = "netra_output"):
        self.target = target
        self.timestamp = datetime.utcnow().isoformat()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def build_payload(self, assets: List[Dict]) -> Dict:
        """
        Build final structured output
        """
        return {
            "target": self.target,
            "generated_at": self.timestamp,
            "asset_count": len(assets),
            "assets": assets
        }

    def write_json(self, assets: List[Dict]) -> str:
        """
        Write final results to JSON file
        """
        payload = self.build_payload(assets)

        filename = f"{self.target.replace('.', '_')}_recon.json"
        file_path = self.output_dir / filename

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

        return str(file_path)
