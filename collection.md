# Collection and sampling protocol

**Status: prospective protocol for the portfolio extension; not a reconstruction of completed historical work.**

1. Verify the exact listing and address for each store. Resolve Russell Square versus Hampstead before using Truedan material.
2. Choose either a within-neighbourhood study or the existing cross-location Zone 1 comparison. This release describes the latter.
3. Record collection date, listing URL, platform total review count, displayed rating, review dates and sort order separately.
4. For a new feasible pilot, use up to 50 consecutive text reviews per store within the same predeclared 12-month window, ordered newest first. This is a proposed cap, not an achieved sample or a power calculation. Record fewer eligible reviews honestly. Record the final window before collecting.
5. Exclude empty text and exact duplicate records; log reasons. Do not exclude a review because it contradicts the hypothesis. Record language; mark any translation and retain the original privately for checking.
6. Preserve a local review ID and evidence pointer for every coded row. Mark inaccessible or untraceable material as such.
7. Keep historical recovered reviews separate from newly collected records. Do not backdate new observations.

## Recommended fields

review_id, store_id, brand, store_address, listing_url, collected_at, review_date, date_precision, rating, language, paraphrase, evidence_pointer, overall_sentiment, themes, theme_polarity, ai_label, human_label, validation_status, exclusion_reason.

Displayed relative dates must not be converted into falsely precise dates. Platform total review counts are metadata, never the analysis denominator.

## Reporting

Report included and excluded n for every store, dates, language handling and manual-check coverage. With one store per brand, label results by store and avoid generalising to the entire brand. Treat recent consecutive reviews as a convenience sample, not a random sample of customers.
