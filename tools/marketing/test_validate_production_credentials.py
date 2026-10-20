#!/usr/bin/env python3
import base64
import unittest
from validate_production_credentials import check

def good():
    return {
        "ZERO_EMPIRE_KEYSTORE_BASE64": base64.b64encode(bytes.fromhex("FEEDFEED") + b"x" * 40).decode(),
        "ZERO_EMPIRE_KEYSTORE_PASSWORD": "secret",
        "ZERO_EMPIRE_KEY_ALIAS": "upload",
        "ZERO_EMPIRE_KEY_PASSWORD": "secret",
        "ADMOB_APP_ID": "ca-app-pub-1234567890123456~1234567890",
        "REWARDED_AD_UNIT_ID": "ca-app-pub-1234567890123456/1234567890",
        "INTERSTITIAL_AD_UNIT_ID": "ca-app-pub-1234567890123456/1234567891",
    }

class CredentialsTest(unittest.TestCase):
    def test_valid_format(self):
        self.assertEqual(check(good()), [])
    def test_missing(self):
        self.assertTrue(any("missing" in s for s in check({})))
    def test_reject_sample(self):
        env = good()
        env["ADMOB_APP_ID"] = "ca-app-pub-3940256099942544~3347511713"
        self.assertTrue(any("sample publisher" in s for s in check(env)))
    def test_reject_cross_publisher(self):
        env = good()
        env["REWARDED_AD_UNIT_ID"] = "ca-app-pub-1111111111111111/1234567890"
        self.assertTrue(any("does not match" in s for s in check(env)))
    def test_reject_duplicate_units(self):
        env = good()
        env["INTERSTITIAL_AD_UNIT_ID"] = env["REWARDED_AD_UNIT_ID"]
        self.assertTrue(any("distinct" in s for s in check(env)))
    def test_reject_corrupt_base64(self):
        env = good()
        env["ZERO_EMPIRE_KEYSTORE_BASE64"] = "not/base64!"
        self.assertTrue(any("Base64" in s for s in check(env)))
    def test_never_leak_secret(self):
        env = good()
        env["ZERO_EMPIRE_KEYSTORE_PASSWORD"] = "SUPER_SECRET_PASSWORD"
        self.assertNotIn("SUPER_SECRET_PASSWORD", "\n".join(check(env)))

if __name__ == "__main__":
    unittest.main()
