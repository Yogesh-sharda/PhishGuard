import re
import requests

SUSPICIOUS_KEYWORDS = [
    "login", "update", "account", "verify", "secure", "bank", "paypal", "password", "free", "gift"
]
SUSPICIOUS_TLDS = [
    ".tk", ".ml", ".ga", ".cf", ".gq", ".xyz", ".top", ".work", ".support"
]
URL_SHORTENERS = [
    "bit.ly", "t.co", "goo.gl", "tinyurl.com", "ow.ly", "shorte.st", "adf.ly"
]
BRAND_NAMES = [
    "google", "facebook", "apple", "amazon", "microsoft", "paypal", "bankofamerica", "wellsfargo"
]
HOMOGRAPH_REGEX = re.compile(r'[\u0430\u0435\u043E\u0440\u0441\u0445]', re.I)

def analyze_url(url):
    results = {}

    # contains_ip_address
    results['contains_ip_address'] = bool(re.search(r'https?://(\d{1,3}\.){3}\d{1,3}', url))
    # contains_suspicious_keywords
    results['contains_suspicious_keywords'] = any(kw in url.lower() for kw in SUSPICIOUS_KEYWORDS)
    # contains_suspicious_tld
    results['contains_suspicious_tld'] = any(url.lower().endswith(tld) for tld in SUSPICIOUS_TLDS)
    # url_length
    results['url_length'] = len(url)
    # long_url
    results['long_url'] = results['url_length'] > 75
    # has_https
    results['has_https'] = url.lower().startswith("https://")
    # contains_special_chars
    results['contains_special_chars'] = bool(re.search(r'[@%]|%[0-9a-f]{2}', url))
    # uses_shortener
    results['uses_shortener'] = any(short in url.lower() for short in URL_SHORTENERS)
    # contains_multiple_subdomains
    try:
        domain_part = re.sub(r'^https?://', '', url).split('/')[0].split(':')[0]
        results['contains_multiple_subdomains'] = domain_part.count('.') > 2
    except Exception:
        results['contains_multiple_subdomains'] = False
    # impersonates_brand
    results['impersonates_brand'] = any(re.search(brand + r"[^a-z]", url, re.I) for brand in BRAND_NAMES)
    # uses_uncommon_port
    results['uses_uncommon_port'] = bool(re.search(r':\d{2,5}', url)) and not re.search(r':80\b|:443\b', url)
    # has_homograph
    results['has_homograph'] = bool(HOMOGRAPH_REGEX.search(url))

    # phishing_score
    phishing_score = 0
    if results['contains_ip_address']: phishing_score += 2
    if results['contains_suspicious_keywords']: phishing_score += 2
    if results['contains_suspicious_tld']: phishing_score += 1
    if results['long_url']: phishing_score += 1
    if not results['has_https']: phishing_score += 1
    if results['contains_special_chars']: phishing_score += 1
    if results['uses_shortener']: phishing_score += 2
    if results['contains_multiple_subdomains']: phishing_score += 1
    if results['impersonates_brand']: phishing_score += 2
    if results['uses_uncommon_port']: phishing_score += 1
    if results['has_homograph']: phishing_score += 2

    results['phishing_score'] = phishing_score
    results['is_phishing'] = phishing_score >= 4
    return results

if __name__ == "__main__":
    url = input("Enter the URL to scan: ").strip()
    if not re.match(r"^https?://", url):
        print("Please enter a valid URL starting with http:// or https://")
    else:
        results = analyze_url(url)
        print("Scan Results (Advanced):")
        for k, v in results.items():
            print(f"{k}: {v}")
        # Optional: Try fetching and look for suspicious content
        try:
            resp = requests.get(url, timeout=5)
            content = resp.text.lower()
            if "enter your password" in content or "verify your account" in content:
                print("Note: Website asks for sensitive info. Be careful!")
        except Exception as e:
            print(f"Note: Could not access URL ({e})")