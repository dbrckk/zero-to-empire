import importlib.util
import pathlib
import tempfile
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("ui_economy_probe.py")
spec = importlib.util.spec_from_file_location("ui_economy_probe", MODULE_PATH)
probe = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(probe)


class EconomyProbeTest(unittest.TestCase):
    def write_xml(self, texts: list[str]) -> pathlib.Path:
        handle = tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False)
        nodes = "".join(f'<node text="{text}" content-desc="" />' for text in texts)
        handle.write(f"<hierarchy>{nodes}</hierarchy>")
        handle.close()
        return pathlib.Path(handle.name)

    def test_reads_plain_capital(self):
        path = self.write_xml(["CAPITAL", "801", "+1/s"])
        self.assertEqual(probe.read_capital(path), 801.0)

    def test_reads_compact_capital(self):
        path = self.write_xml(["CAPITAL", "2.50K", "+24/s"])
        self.assertEqual(probe.read_capital(path), 2500.0)

    def test_money_suffixes(self):
        self.assertEqual(probe.parse_money("1.25M"), 1_250_000.0)
        self.assertEqual(probe.parse_money("3.00B"), 3_000_000_000.0)
        self.assertEqual(probe.parse_money("4.20T"), 4_200_000_000_000.0)

    def test_rejects_missing_capital(self):
        path = self.write_xml(["NET WORTH", "801"])
        with self.assertRaises(ValueError):
            probe.read_capital(path)


if __name__ == "__main__":
    unittest.main()
