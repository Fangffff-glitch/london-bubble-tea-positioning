# Collection and time-window protocol

The underlying snapshot was collected on 5 November 2026. The analysis frame was revised on 6 November 2026, without adding new reviews. Main outputs use recent subsets; collection coverage and analytical inclusion are distinct.

## Time period — what is actually included?

**Snapshot: 5 November 2026. Revision: 6 November 2026. No new reviews were collected for this revision.**

| Role | Intended calendar period | Operational rule applied to saved Google display ages |
|---|---|---|
| Main analysis | Approximately 5 Nov 2024–5 Nov 2026 | Hours/days/weeks/months ago, plus “a year ago”; exclude “2 years ago” and older |
| Sensitivity comparison | Approximately 5 Nov 2025–5 Nov 2026 | Hours/days/weeks/months ago only; exclude all year-labelled records |
| Historical appendix | All captured listing history through 5 Nov 2026 | Retain all 2,941 original records for traceability |

**These are relative-display-age proxies, not verified exact 24- or 12-month windows or visit dates.** The saved data contain rounded relative labels, sometimes edit ages. We do not assign invented calendar dates. Boundary reviews may be misclassified if Google's rounding differs from the assumed age bands. MILKSHA-0331 explicitly describes a 2021 experience and is excluded from both recent windows, even though its displayed age is recent. Other undisclosed historical experiences may remain. Edited records stay in the main analysis but are flagged and tested separately.

| Analysis frame | T4 records / texts | Milksha records / texts | Truedan records / texts | Total records / texts |
|---|---:|---:|---:|---:|
| Main: approximately two years | 776 / 712 | 276 / 230 | 222 / 170 | 1,274 / 1,112 |
| Comparison: approximately one year | 170 / 158 | 185 / 159 | 84 / 65 | 439 / 382 |
| Full history: archive only | 1,521 / 1,323 | 531 / 418 | 889 / 634 | 2,941 / 2,375 |

## How the source corpus was collected

The complete unfiltered Reviews lists were loaded in Google Maps in default **Most relevant** order. Available long customer texts were expanded. Rendered review cards were read until unique review IDs matched each listing total. There was no per-store cap, keyword, star or language filter. Customer text was separated from owner replies; owner replies were excluded.

Extraction from rendered `div.jftiEf[data-review-id]` used its ID; `.kvMYJc` for the star accessible label; `.rsqaWe` for displayed age; and `.MyEned .wiI7pd` for customer text. Selectors document the collection and may change. No hidden/private endpoint was used.

| Store | All captured records | All text | Rating only | Stars 5 / 4 / 3 / 2 / 1 |
|---|---:|---:|---:|---|
| T4 | 1,521 | 1,323 | 198 | 1,403 / 66 / 18 / 3 / 31 |
| Milksha | 531 | 418 | 113 | 398 / 61 / 22 / 12 / 38 |
| Truedan | 889 | 634 | 255 | 817 / 38 / 13 / 8 / 13 |

Unique IDs and star distributions reconcile with the observed snapshot. Different IDs with repeated wording remain separate records; edited reviews are not a version history. Raw files remain local; integrity hashes are in `collection_checks.json`.

## Reproducible inclusion rules

`build_windows.py` applies rules to the saved `displayed_age`, without changing sentiment or theme labels. The public archive includes `main_2y_proxy`, `comparison_1y_proxy`, `edited_date_flag`, `known_historical_experience` and `window_reason` for every row. A 1 means included/flagged; a 0 means not included/not flagged. “Not flagged” does not prove an experience is recent.

- Strip the literal `Edited ` prefix solely for age parsing, retaining an edit flag.
- Hours/days/weeks/months → both recent proxies, unless explicitly historical.
- `a year ago` → main proxy only.
- `2 years ago` and older → historical archive only.
- MILKSHA-0331 → archive only because the text explicitly describes 2021.
- Unknown date labels must raise an error for inspection; never silently assign a date.

Boundary uncertainty cannot be eliminated from these saved labels. Exact rolling windows would require verified exact publication dates and a separately stated policy for edits. Visit dates would still need separate evidence. We therefore use approximate periods and report an additional main-frame check excluding all flagged edited records.

## Language and access limitations

Google-displayed English translations were used where present; original language and translation accuracy were not exhaustively checked. These listing snapshots exclude hidden/deleted or later-added reviews and all other branches/platforms. Complete collection does not mean representative customer coverage. Links open store listings, not guaranteed individual-review deep links. IDs and hashes cannot reconstruct withheld wording.

## Why two years, and what are the trade-offs?

The decision concerns a venture entering the market now. Recent reviews are more relevant to current menus, staff and operating practices than six-year-old experiences. Two years provides more material than one year while reducing the weight of older conditions; the one-year comparison checks whether the interpretation changes with a tighter window.

| Choice | Benefit | Risk / cost | How it is handled |
|---|---|---|---|
| Two-year main frame | Better balance of recency and evidence volume; Truedan has 170 texts rather than 65 | May still mix older menus, staff or service regimes | Compare the one-year subset; avoid claims of current measured performance |
| One-year comparison | Closer to recent customer accounts | Smaller and unequal groups; promotions or seasonal activity may have greater influence | Show denominators and counts; do not treat changes as a causal trend |
| Relative-age filtering | Transparent, reproducible use of the data actually retained | Rounded boundaries and edit dates are not exact publication/visit dates | Label all periods approximate, preserve original labels and flag edits |
| Full history in the appendix | Keeps the original collection auditable | Old comments can distract from the current decision | Do not use archive totals as the denominator of main charts |

More reviews do not automatically mean better evidence for a current decision. These windows reduce historical mismatch but do not remove Google self-selection, incentives, translation effects or the confounding of brand and location. Stars are from the same source, not independent triangulation. No minimum sample-size threshold or statistical representativeness is claimed.
