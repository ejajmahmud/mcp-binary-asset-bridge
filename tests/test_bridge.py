"""Tests for mcp-binary-asset-bridge."""
import unittest
from mcp_binary_asset_bridge.bridge import BinaryAssetBridge


class TestBinaryAssetBridge(unittest.TestCase):
    def test_roundtrip(self):
        data = b"Hello MCP Multimodal Binary Data!"
        env = BinaryAssetBridge.encode_asset(data, "text/plain")
        self.assertEqual(env["size_bytes"], len(data))
        decoded, valid = BinaryAssetBridge.decode_asset(env)
        self.assertTrue(valid)
        self.assertEqual(decoded, data)


if __name__ == "__main__":
    unittest.main()
