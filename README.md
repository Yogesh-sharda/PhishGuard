# 🛡️ PhishGuard – Advanced Phishing Detection Website

PhishGuard is a modern, user-friendly **phishing detection platform** that helps users instantly analyze suspicious URLs and identify potential online threats.  
It uses **AI-powered heuristics** and real-time checks to provide **detailed phishing scores** and educate users on staying safe online.

---

## 🚀 Features

### 🔍 Core Detection
- **Real-time URL scanning** for:
  - IP-based domains
  - Suspicious keywords (`login`, `bank`, `verify`, etc.)
  - Dangerous TLDs (`.tk`, `.ml`, `.xyz`, etc.)
  - URL shortening services
  - Multiple subdomains
  - Brand impersonation attempts
  - Uncommon ports & homograph attacks
- **Phishing Score Calculation** (score ≥ 4 means highly suspicious)
- **Instant, detailed safety reports** in a clean table format

### 🎨 User Experience
- **Attractive, responsive design** (mobile, tablet, desktop)
- Color-coded results (**red** for dangerous, **green** for safe)
- **Educational section** on spotting phishing attempts
- Planned **browser extension** for 1-click scanning

### 🔒 Privacy & Trust
- **No data storage** – scans are done securely without saving URLs
- **Trust badges** and clear security disclaimers

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5, CSS3, JavaScript (Vanilla)

**Backend (CLI/Server-side):**
- Python 3
- `re` for regex pattern matching
- `requests` for optional page content checks

---

## 📂 Project Structure
├── index.html # Main UI
├── styles.css # Website styling
├── script.js # Frontend JS for scan simulation
├── phishing_link_scanner.py # Python backend scan logic

