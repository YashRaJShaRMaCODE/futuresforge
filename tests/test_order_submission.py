import importlib.util
import os
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
place_limit_order = importlib.import_module("limit_order").place_limit_order
place_market_order = importlib.import_module("market_orders").place_market_order


class FakeClient:
    def __init__(self):
        self.order = None

    def futures_create_order(self, **order):
        self.order = order
        return {"status": "NEW", "orderId": 42}


class OrderSubmissionTests(unittest.TestCase):
    def test_market_submission_uses_validated_market_payload(self):
        client = FakeClient()

        result = place_market_order("btcusdt", "buy", "0.01", client=client)

        self.assertEqual(result, {"status": "NEW", "orderId": 42})
        self.assertEqual(
            client.order,
            {"symbol": "BTCUSDT", "side": "BUY", "quantity": "0.01", "type": "MARKET"},
        )

    def test_limit_submission_uses_validated_limit_payload(self):
        client = FakeClient()

        place_limit_order("btcusdt", "sell", "0.01", "65000", client=client)

        self.assertEqual(
            client.order,
            {
                "symbol": "BTCUSDT",
                "side": "SELL",
                "quantity": "0.01",
                "price": "65000",
                "type": "LIMIT",
                "timeInForce": "GTC",
            },
        )

    def test_exchange_client_is_always_created_in_testnet_mode(self):
        binance = types.ModuleType("binance")
        binance.__path__ = []
        binance_client = types.ModuleType("binance.client")
        client_factory = Mock(return_value=FakeClient())
        binance_client.Client = client_factory
        dotenv = types.ModuleType("dotenv")
        dotenv.load_dotenv = Mock()
        modules = {"binance": binance, "binance.client": binance_client, "dotenv": dotenv}
        spec = importlib.util.spec_from_file_location("test_futureforge_utils", ROOT / "src" / "utils.py")
        module = importlib.util.module_from_spec(spec)
        with (
            patch.dict(sys.modules, modules),
            patch.dict(
                os.environ,
                {"BINANCE_API_KEY": "test-key-only", "BINANCE_API_SECRET": "test-secret-only"},
            ),
        ):
            spec.loader.exec_module(module)
            client = module.get_binance_client()

        self.assertIsInstance(client, FakeClient)
        client_factory.assert_called_once_with("test-key-only", "test-secret-only", testnet=True)

    def test_missing_credentials_fail_before_client_creation(self):
        binance = types.ModuleType("binance")
        binance.__path__ = []
        binance_client = types.ModuleType("binance.client")
        client_factory = Mock()
        binance_client.Client = client_factory
        dotenv = types.ModuleType("dotenv")
        dotenv.load_dotenv = Mock()
        modules = {"binance": binance, "binance.client": binance_client, "dotenv": dotenv}
        spec = importlib.util.spec_from_file_location("test_futureforge_utils_missing", ROOT / "src" / "utils.py")
        module = importlib.util.module_from_spec(spec)
        with (
            patch.dict(sys.modules, modules),
            patch.dict(
                os.environ,
                {"BINANCE_API_KEY": "", "BINANCE_API_SECRET": ""},
            ),
        ):
            spec.loader.exec_module(module)
            with self.assertRaisesRegex(RuntimeError, "BINANCE_API_KEY"):
                module.get_binance_client()

        client_factory.assert_not_called()


if __name__ == "__main__":
    unittest.main()
