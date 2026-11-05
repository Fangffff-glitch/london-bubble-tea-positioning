# Collection protocol and coverage

## Scope

Google Maps listings for T4 Liverpool Street, Milksha Shaftesbury Avenue and Truedan Russell Square, collected on 5 November 2026. This release supersedes the 53-text-review pilot retained in Git history.

| Store | Listing total | Unique captured IDs | Text | Rating only | Stars 5 / 4 / 3 / 2 / 1 |
|---|---:|---:|---:|---:|---|
| T4 | 1,521 | 1,521 | 1,323 | 198 | 1,403 / 66 / 18 / 3 / 31 |
| Milksha | 531 | 531 | 418 | 113 | 398 / 61 / 22 / 12 / 38 |
| Truedan | 889 | 889 | 634 | 255 | 817 / 38 / 13 / 8 / 13 |

The final unique-ID counts and per-star counts reconcile with the observed listing totals and rating breakdown. IDs are also unique across all three files. See [collection_checks.json](collection_checks.json).

## Actual extraction steps

1. Open the listing's Reviews tab in Google Maps, using English display. The final complete collection used **Most relevant**, with no search term or star filter. An initial Newest loading attempt was abandoned; the final corpus is not a newest-first sample.
2. Scroll the reviews panel repeatedly while retaining loaded review cards, until the number of unique customer review IDs matches the visible listing total.
3. Expand available long-review text controls. Read rendered customer content, not hidden application state or private endpoints.
4. Extract each rendered `div.jftiEf[data-review-id]`: ID from `data-review-id`; stars from `.kvMYJc`'s accessible label; relative date from `.rsqaWe`; **customer text only** from `.MyEned .wiI7pd`. Owner response text is outside this customer selector and is excluded. Selectors document this collection and may change.
5. Save raw records locally and check unique IDs, rating values, presence of text and category totals. Raw file SHA-256 hashes are published; full source text stays outside this repository.

No per-store cap, rating filter, language exclusion or recent-date exclusion was applied. The Milksha record explicitly referring to a 2021 experience, excluded from the earlier recent pilot, is now included as MILKSHA-0331. Different IDs with similar or identical wording are retained: they cannot be safely treated as the same reviewer. An edited review is one record, not a separate version history.

## Time and language

All displayed history was retained. Relative ages run from hours/months to years; T4 and Truedan include records displayed as six years old, and Milksha four years old. These are listing-history observations, not verified store-opening dates or visit dates. Historical changes in ownership/menu/service are not controlled.

The public table preserves the exact displayed age. `under_one_year` means its label uses hours, days, weeks or months rather than years. It is a coarse display-age bucket, not an inferred calendar date. Google may show the edit age. There are 35 edited T4 records, 17 Milksha and 18 Truedan records. The historical MILKSHA-0331 example shows why recent display age need not mean recent experience.

Google-displayed English translations were read where present, alongside untranslated text where displayed. Original language and translation accuracy were not exhaustively verified; no reliable translation count is asserted for this corpus.

## What complete coverage means

All 2,941 records visible through these three listings were captured and reconciled at collection. Deleted, hidden, later-added or inaccessible reviews, other branches, delivery-platform reviews and non-reviewing customers are outside the frame. Completeness within this snapshot does not establish representativeness of customers or London demand.

## Public fields

`record_id` is a project lookup key based on capture order, not chronological rank. `google_review_id` is the source identifier. `stars` and `displayed_age` are observed. `has_text`, `text_characters`, `text_sha256` and `display_age_band` are derived. `sentiment` is an AI judgement; ten 0/1 theme columns are dictionary results. `source_url` opens the relevant store listing, not a guaranteed deep link to an individual review.

Names, profile links, images and full text are omitted from the published table. Selected paraphrases are in the audit. Source review IDs and content hashes support matching, but cannot reconstruct withheld text. Numerical outputs are reproducible from public labels; independently validating semantic coding requires source access.
