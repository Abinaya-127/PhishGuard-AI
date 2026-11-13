import unittest

from src.url_features import extract_features


class TestURLFeatures(unittest.TestCase):

    def test_valid_url(self):
        features = extract_features("https://www.google.com")
        self.assertIsInstance(features, dict)

    def test_feature_count(self):
        features = extract_features("https://www.google.com")
        self.assertEqual(len(features), 16)

    def test_https_flag(self):
        features = extract_features("https://www.google.com")
        self.assertEqual(features["https_flag"], 1)

    def test_http_flag(self):
        features = extract_features("http://example.com")
        self.assertEqual(features["https_flag"], 0)

    def test_empty_url(self):
        with self.assertRaises(ValueError):
            extract_features("")

    def test_ip_address(self):
        features = extract_features("http://192.168.1.1")
        self.assertEqual(features["has_ip_address"], 1)


if __name__ == "__main__":
    unittest.main()