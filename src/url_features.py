import ipaddress
import math
import re
from collections import Counter
from urllib.parse import urlsplit, parse_qsl


POPULAR_TLDS = {
    "com", "org", "net", "edu", "gov",
    "in", "uk", "de", "jp", "au", "co"
}

SUSPICIOUS_EXTENSIONS = {
    ".exe", ".zip", ".rar", ".scr",
    ".bat", ".apk", ".msi", ".js"
}


def calculate_entropy(text):
    """Calculate Shannon entropy of a string."""
    if not text:
        return 0.0

    counts = Counter(text)
    length = len(text)

    return -sum(
        (count / length) * math.log2(count / length)
        for count in counts.values()
    )


def extract_features(url):
    """Extract 16 numerical features from a URL."""

    if not isinstance(url, str) or not url.strip():
        raise ValueError("Please provide a valid URL.")

    url = url.strip()

    if "://" not in url:
        url = "http://" + url

    try:
        parsed = urlsplit(url)
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

    domain_parts = hostname.split(".")

    tld = domain_parts[-1] if domain_parts else ""

    subdomain_count = max(0, len(domain_parts) - 2)

    domain_name = ".".join(domain_parts[-2:]) if len(domain_parts) >= 2 else hostname

    query_parameters = parse_qsl(parsed.query, keep_blank_values=True)

    numeric_count = sum(char.isdigit() for char in url)

    features = {
        "url_length": len(url),
        "has_ip_address": has_ip,
        "dot_count": url.count("."),
        "https_flag": int(parsed.scheme.lower() == "https"),
        "url_entropy": calculate_entropy(url),
        "token_count": len(re.findall(r"[A-Za-z0-9]+", url)),
        "subdomain_count": subdomain_count,
        "query_param_count": len(query_parameters),
        "tld_length": len(tld),
        "path_length": len(parsed.path),
        "has_hyphen_in_domain": int("-" in hostname),
        "number_of_digits": numeric_count,
        "tld_popularity": int(tld in POPULAR_TLDS),
        "suspicious_file_extension": int(
            any(parsed.path.lower().endswith(ext)
                for ext in SUSPICIOUS_EXTENSIONS)
        ),
        "domain_name_length": len(domain_name),
        "percentage_numeric_chars": (
            numeric_count / len(url) * 100 if url else 0
        )
    }

    return features