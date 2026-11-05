"""CLI for mcp-binary-asset-bridge."""
import sys
import argparse
from .bridge import BinaryAssetBridge


def main():
    parser = argparse.ArgumentParser(description="MCP Binary Asset Bridge")
    parser.add_argument("--demo", action="store_true", help="Run binary asset encoding demonstration")
    args = parser.parse_args()

    bridge = BinaryAssetBridge()
    if args.demo:
        sample_bytes = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR..."
        encoded = bridge.encode_asset(sample_bytes, "image/png")
        print("Encoded Asset Envelope:", {k: v for k, v in encoded.items() if k != "data_b64"})
        print("Data B64 Preview:", encoded["data_b64"][:20] + "...")
        decoded, valid = bridge.decode_asset(encoded)
        print(f"Decoded {len(decoded)} bytes. Integrity Valid: {valid}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
