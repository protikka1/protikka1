# Google Workspace email troubleshooting

Test messages sent from a personal Gmail account to a Workspace alias reached the primary mailbox's Spam folder. Google Admin's Email Log Search showed four messages to the alias marked as spam. A message sent directly to the primary address was delivered to the Gmail mailbox.

## DNS checks

| Record | Observed result |
| --- | --- |
| MX | Five Google Workspace MX records with priorities 1, 5, 5, 10, and 10 |
| SPF | One TXT record authorizing Google Workspace: `v=spf1 include:_spf.google.com ~all` |
| DKIM | Google public key published at `google._domainkey` |
| DMARC | TXT record visible in Google Public DNS with `p=none` and an aggregate reporting address |

## What remains to verify

- For incoming mail, open a test message in Spam and use **More → Show original** to check the sender's SPF, DKIM, and DMARC results. Compare those results with the delivery log.
- For outgoing mail, send a test from the Workspace mailbox to a separate Gmail account. Use **Show original** in the receiving account to verify DKIM signing and DMARC alignment. Publishing the DKIM key verifies the DNS record. The message header verifies whether signing worked.
