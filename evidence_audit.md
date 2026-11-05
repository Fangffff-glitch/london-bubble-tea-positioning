# Evidence audit and validation status

## Completed checks

- Confirmed three live Google Maps listing identities and addresses. T4 is on Brushfield Street, not inside Liverpool Street station; Truedan is the Brunswick Centre listing.
- Recorded 60 unique native review IDs and display ranks; excluded 6 records without customer text and 1 explicitly historical 2021 experience.
- Separated customer text from owner replies, including replies attached to rating-only cards.
- Expanded available long-review controls and preserved substantive mixed sentiment.
- Checked that sentiment totals equal included n (18, 17, 18), that IDs are unique and that themes use the codebook.
- Chart calculations are deterministic from the public CSV; chart code does not infer sentiment from star ratings.

These checks were performed by the assistant. **No human validation has yet occurred.** author_review.csv is intentionally unfilled; it is a worksheet, not a completed audit log.

## Classification decisions requiring author attention

| Record | Decision | Reason / uncertainty |
|---|---|---|
| MILKSHA-11 | Exclude | Recently edited but explicitly describes a 2021 experience |
| MILKSHA-16 | Mixed | Qualified praise; positive is a plausible alternative, quantified in findings.md |
| TRUEDAN-04 | Mixed | Flavour and staff praise coexist with ice/portion concerns |
| TRUEDAN-09 | No authenticity tag | Comparator is not explicit in displayed translated text |
| TRUEDAN-12 | Mixed; capacity negative, staff positive | No explicit waiting statement; does not establish channel causality |
| TRUEDAN-14 | Service/product negative; no price tag | Complaint centres on treatment and product experience, not willingness to pay |

Nine included records used displayed Google translations. Original-language review remains pending. Native IDs improve traceability, but deleted/edited source text and the lack of a permanent raw-text archive limit exact reproduction.

## Original claims revised

Review volume does not establish demand, revenue or profitability. Reviews are expressed experience, not revealed purchasing preferences. Brand/location confounding remains. The 45-second target is unvalidated; EPOS/legal terms are omitted as weak evidence. Current franchise-scale and Taiwan footprint claims remain unverified. The original store-count inconsistencies are not resolved by new listing totals.

Repeated staff mentions, product launches and promotional comments may shape recent review activity. These patterns merit caution but do not prove manipulation. A fixed-neighbourhood, longer-window study would be a separate design rather than a relabelling of this pilot.
