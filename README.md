## Hi there 👋
# 1. Initialize repository matching your username
mkdir protikka1
cd protikka1
git init

# 2. Write the content to README.md
cat << 'EOF' > README.md
# Google Workspace & Domain Deliverability Hardening

Automated DNS configuration, DKIM key generation, and mail-authentication audit for custom domain email delivery.

---

## 1. Problem

* **Spam & Rejection:** Outbound business emails fail Gmail and Yahoo bulk-sender requirements, landing in spam folders or bouncing with `550 5.7.26` authentication errors.
* **DNS Misconfiguration:** Missing or malformed SPF records, unaligned DKIM keys, and absent DMARC monitoring policies.
* **Spoofing Vulnerability:** Domain unprotected against unauthorized third-party sender impersonation.

---

## 2. Action

### DNS Routing & MX Configuration
Mapped primary mail exchanges to Google Workspace infrastructure with strict priority weighting:

| Hostname | Type | Priority | Target | TTL |
| :--- | :--- | :--- | :--- | :--- |
| `@` | MX | 1 | `ASPMX.L.GOOGLE.COM.` | 3600 |
| `@` | MX | 5 | `ALT1.ASPMX.L.GOOGLE.COM.` | 3600 |
| `@` | MX | 5 | `ALT2.ASPMX.L.GOOGLE.COM.` | 3600 |
| `@` | MX | 10 | `ALT3.ASPMX.L.GOOGLE.COM.` | 3600 |
| `@` | MX | 10 | `ALT4.ASPMX.L.GOOGLE.COM.` | 3600 |

### Email Authentication Deployment
* **SPF (Sender Policy Framework):** Deployed a single validated TXT record authorizing Google mail servers:
  ```text
  v=spf1 include:_spf.google.com ~all
  
<!--
**protikka1/protikka1** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
