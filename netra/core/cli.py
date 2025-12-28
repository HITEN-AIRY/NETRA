import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="NETRA - Intelligent Subdomain Recon Engine"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    recon_parser = subparsers.add_parser("recon", help="Run reconnaissance")

    recon_parser.add_argument(
        "--domain",
        required=True,
        help="Target root domain (example.com)"
    )

    recon_parser.add_argument(
        "--mode",
        choices=["passive", "active", "hybrid"],
        required=True,
        help="Recon mode"
    )

    recon_parser.add_argument(
        "--ai",
        choices=["on", "off"],
        default="on",
        help="Enable or disable AI assistance"
    )

    return parser.parse_args()

def main():
    args = parse_args()
    print("Command:", args.command)
    print("Domain:", args.domain)
    print("Mode:", args.mode)
    print("AI:", args.ai)

if __name__ == "__main__":
    main()
