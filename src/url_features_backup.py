import ipaddress
from urllib.parse import urlsplit

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "secure",
    "account", "banking", "password",
    "signin", "confirm", "wallet"
]

URL_SHORTENERS = [
    "bit.ly", "tinyurl.com", "t.co",
    "is.gd", "cutt.ly", "shorturl.at"
]


def extract_features(url):
    """Extract numerical features from a URL without visiting it."""

    if not isinstance(url, str) or not url.strip():
        raise ValueError("Please provide a valid URL.")

    url = url.strip()
    parse_url = url if "://" in url else "http://" + url

    try:
        parsed = urlsplit(parse_url)
        hostname = (parsed.hostname or "").lower().rstrip(".")
    except ValueError:
        raise ValueError("Unable to parse the URL.")

    if not hostname:
        raise ValueError("URL must contain a hostname.")

    try:
        ipaddress.ip_address(hostname)
        has_ip = 1
    except ValueError:
        has_ip = 0

    labels = hostname.split(".")
    subdomain_count = max(0, len(labels) - 2)

    features = {
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(parsed.path),
        "query_length": len(parsed.query),
        "count_dots": url.count("."),
        "count_hyphens": url.count("-"),
        "count_at": url.count("@"),
        "count_question": url.count("?"),
        "count_equal": url.count("="),
        "count_underscore": url.count("_"),
        "count_percent": url.count("%"),
        "count_digits": sum(c.isdigit() for c in url),
        "count_slashes": url.count("/"),
        "subdomain_count": subdomain_count,
        "has_ip_address": has_ip,
        "uses_https": int(parsed.scheme.lower() == "https"),
        "has_suspicious_keyword": int(
            any(word in url.lower() for word in SUSPICIOUS_KEYWORDS)
        ),
        "is_shortened_url": int(hostname in URL_SHORTENERS),
        "has_double_slash_in_path": int("//" in parsed.path)
    }

    return features