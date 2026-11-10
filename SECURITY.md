# Security Policy

## Supported Versions

Critical bug fixes and security patches are actively applied to the latest `main` branch.

| Version / Branch | Supported          |
| ---------------- | ------------------ |
| `main`           | :white_check_mark: |
| `< 1.0.0`        | :x:                |

---

## Reporting a Vulnerability

If you discover a potential security vulnerability within `dns_audit.py` or associated repository configurations, please follow responsible disclosure guidelines:

1. **Do Not Open a Public Issue:** To protect users and domain configurations, avoid submitting vulnerability reports via public GitHub issues, discussions, or pull requests.
2. **Direct Contact:** Email full vulnerability details directly to:
   * **Security Contact:** [support@eporth.org](mailto:support@eporth.org)
   * **Subject Line:** `[Vulnerability Report] protikka1 repository`
3. **Report Details to Include:**
   * Description of the vulnerability and attack vector.
   * Minimal reproducible steps or proof-of-concept (PoC) code.
   * Potential impact on DNS resolution, credential handling, or system execution.
   * Suggested remediation steps if identified.

---

## Response & Disclosure Process

* **Acknowledgment:** Initial receipt of the vulnerability report will be acknowledged within 48 hours.
* **Assessment & Fix:** We will evaluate the impact, develop a fix on a private branch, and verify resolution across DNS environments.
* **Public Release:** Once the patch is merged to `main`, an advisory notice and patch notes will be documented.
