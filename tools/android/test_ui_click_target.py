import importlib.util
import pathlib
import tempfile
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("ui_click_target.py")
spec = importlib.util.spec_from_file_location("ui_click_target", MODULE_PATH)
click_target = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(click_target)


class ClickTargetTest(unittest.TestCase):
    def write_xml(self, body: str) -> pathlib.Path:
        handle = tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False)
        handle.write("<hierarchy>" + body + "</hierarchy>")
        handle.close()
        return pathlib.Path(handle.name)

    def test_avoids_non_clickable_label_overlay(self):
        path = self.write_xml(
            '<node class="android.widget.Button" clickable="true" bounds="[10,10][110,50]" />'
            '<node class="android.widget.TextView" text="POWER CORE +1" clickable="false" bounds="[30,10][90,60]" />'
        )
        x, y = click_target.find_click_target(path, "Power Core")
        self.assertTrue(10 <= x <= 110 and 10 <= y <= 50)
        self.assertFalse(30 <= x <= 90 and 10 <= y <= 60)

    def test_uses_direct_clickable_match(self):
        path = self.write_xml('<node text="HIRE" clickable="true" bounds="[20,20][120,80]" />')
        self.assertEqual(click_target.find_click_target(path, "HIRE"), (70, 50))

    def test_fails_without_matching_clickable(self):
        path = self.write_xml('<node text="POWER CORE +1" clickable="false" bounds="[30,10][90,60]" />')
        with self.assertRaises(ValueError):
            click_target.find_click_target(path, "Power Core")


if __name__ == "__main__":
    unittest.main()
