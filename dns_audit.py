#!/usr/bin/env python3
"""
DNS & Google Workspace Deliverability Verification Tool
Audits MX, SPF, DKIM, and DMARC enforcement.
"""

import argparse
import sys

try:
    import dns.resolver
except ImportError:
    print("Error: dnspython is required. Install via: pip install -r requirements.txt")
    sys.exit(1)

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def check_mx(domain, resolver):
    print(f"\n{BOLD}[1] Checking MX Records (Mail Routing)...{RESET}")
    try:
        answers = resolver.resolve(domain, "MX")
        for rdata in sorted(answers, key=lambda r: r.preference):
            print(f"  {GREEN}✓{RESET} Priority {rdata.preference:>2} -> {rdata.exchange}")
        return True
    except Exception as e:
        print(f"  {RED}✗ MX verification failed: {e}{RESET}")
        return False

def check_spf(domain, resolver):
    print(f"\n{BOLD}[2] Checking SPF (Sender Policy Framework)...{RESET}")
    try:
        answers = resolver.resolve(domain, "TXT")
        records = [r.to_text().strip('"') for r in answers if "v=spf1" in r.to_text()]
        if not records:
            print(f"  {RED}✗ Missing SPF record! Outbound mail risks spam rejection.{RESET}")
            return False
        if len(records) > 1:
            print(f"  {RED}✗ Multiple SPF records found (RFC Violation).{RESET}")
            return False
        spf = records[0]
        print(f"  {GREEN}✓ Found SPF:{RESET} {spf}")
        if "include:_spf.google.com" in spf:
            print(f"    {GREEN}↳ Google Workspace authorized.{RESET}")
        return True
    except Exception as e:
        print(f"  {RED}✗ SPF verification failed: {e}{RESET}")
        return False

def check_dkim(domain, selector, resolver):
    dkim_host = f"{selector}._domainkey.{domain}"
    print(f"\n{BOLD}[3] Checking DKIM (Selector: '{selector}')...{RESET}")
    try:
        answers = resolver.resolve(dkim_host, "TXT")
        for r in answers:
            txt = r.to_text().strip('"')
            if "v=DKIM1" in txt or "p=" in txt:
                print(f"  {GREEN}✓ DKIM key verified at {dkim_host}{RESET}")
                return True
        print(f"  {YELLOW}⚠ Record exists but syntax is non-standard.{RESET}")
        return False
    except Exception:
        print(f"  {RED}✗ Missing DKIM key at {dkim_host}.{RESET}")
        return False

def check_dmarc(domain, resolver):
    dmarc_host = f"_dmarc.{domain}"
    print(f"\n{BOLD}[4] Checking DMARC Policy...{RESET}")
    try:
        answers = resolver.resolve(dmarc_host, "TXT")
        records = [r.to_text().strip('"') for r in answers if "v=DMARC1" in r.to_text()]
        if not records:
            print(f"  {RED}✗ Missing DMARC record at {dmarc_host}.{RESET}")
            return False
        print(f"  {GREEN}✓ Found DMARC:{RESET} {records[0]}")
        return True
    except Exception:
        print(f"  {RED}✗ Missing DMARC record at {dmarc_host}.{RESET}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Audit domain email authentication.")
    parser.add_argument("domain", nargs="?", default="eporth.org", help="Target domain (default: eporth.org)")
    parser.add_argument("--selector", default="google", help="DKIM selector (default: google)")
    args = parser.parse_args()

    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
    resolver.timeout = 4.0
    resolver.lifetime = 4.0

    print(f"\n{BOLD}=== DNS Deliverability Audit: {args.domain} ==={RESET}")
    mx = check_mx(args.domain, resolver)
    spf = check_spf(args.domain, resolver)
    dkim = check_dkim(args.domain, args.selector, resolver)
    dmarc = check_dmarc(args.domain, resolver)

    total = sum([mx, spf, dkim, dmarc])
    status = GREEN if total == 4 else RED
    print(f"\n{BOLD}Audit Score: {status}{total}/4 Checks Passed{RESET}\n")

if __name__ == "__main__":
    main()
