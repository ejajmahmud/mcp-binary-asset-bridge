"""Bridge for encoding and verifying binary payloads over MCP."""
import base64
import hashlib
from typing import Dict, Any, Tuple


class BinaryAssetBridge:
    @staticmethod
    def encode_asset(raw_bytes: bytes, mime_type: str = "application/octet-stream") -> Dict[str, Any]:
        b64_str = base64.b64encode(raw_bytes).decode("ascii")
        sha256 = hashlib.sha256(raw_bytes).hexdigest()
        return {
            "mime_type": mime_type,
            "size_bytes": len(raw_bytes),
            "sha256": sha256,
            "data_b64": b64_str
        }

    @staticmethod
    def decode_asset(payload: Dict[str, Any]) -> Tuple[bytes, bool]:
        b64_str = payload["data_b64"]
        raw = base64.b64decode(b64_str.encode("ascii"))
        computed_hash = hashlib.sha256(raw).hexdigest()
        is_valid = (computed_hash == payload.get("sha256"))
        return raw, is_valid
