# Hi, I'm Abul Islam 👋
### Google Workspace & Email Deliverability Specialist | Python Automation

I help businesses, agencies, and domain owners secure custom email infrastructure, eliminate spam folder placement, and resolve Google Workspace DNS issues.

---

## 🛠️ Core Services & Expertise

* **Google Workspace Configuration:** Clean tenant setup, user provisioning, custom domain routing, and MX load-balancing.
* **Email Deliverability (SPF, DKIM, DMARC):** Full compliance implementation to meet Google and Yahoo deliverability requirements (SPF alignment, 2048-bit DKIM keys, and strict DMARC policies: `p=quarantine` / `p=reject`).
* **Automated DNS Diagnostics:** Custom Python tooling to verify DNS propagation, detect configuration errors, and prevent spoofing.

---

## 🔍 Featured Tool: `dns_audit.py`

A terminal diagnostic utility built with `dnspython` to perform real-time verification of mission-critical DNS records:

```text
[✓] MX Records:    Configured for Google Workspace (ASPMX.L.GOOGLE.COM)
[✓] SPF Record:    v=spf1 include:_spf.google.com ~all (Valid)
[✓] DKIM Record:   google._domainkey (Active & Resolving)
[✓] DMARC Policy:  v=DMARC1; p=quarantine; rua=... (Protected)

Overall Deliverability Score: 4/4 PASSED
git clone [https://github.com/protikka1/protikka1.git](https://github.com/protikka1/protikka1.git)
cd protikka1
pip install -r requirements.txt
python3 dns_audit.py eporth.org
📊 Technical Stack
DNS & Hosting: Squarespace DNS, Cloudflare, Google Workspace DNS, Route 53
Scripting & Automation: Python 3 (dnspython, requests), Bash / Shell
Environments & Tools: Linux / Termux, Git, Postmaster Tools, MXToolbox
📬 Contact & Engagements
Email: support@eporth.org
Website: eporth.org
GitHub: @protikka1
Available for freelance Google Workspace migrations, domain audits, and deliverability triage.
