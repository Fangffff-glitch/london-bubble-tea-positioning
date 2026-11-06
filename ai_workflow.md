# AI workflow and provenance

The 6 November revision changes the analysis frame, not the original labels. Main analysis uses 1,112 texts in the two-year relative-age proxy; comparison uses 382 texts in the one-year proxy. All 2,375 historical text labels remain in the archive. See [time-window protocol](time_window_method.md).

## Roles

The project author supplied the business question, Taiwanese-brand case selection and original strategic framing. In this extension, Codex collected rendered public review records, read every non-empty text, assigned sentiment, designed and checked a theme dictionary, generated Python aggregation/chart code and drafted documentation. This is AI-assisted research, not a claim of unaided coding or a custom-trained sentiment model.

The original assignment declared Gemini support. Historical prompts and precise historical model versions have not been independently recovered. NotebookLM research materials are context, not independent corroboration. No external sentiment API was run for this extension.

## Executed sentiment workflow

1. Read all text in batches, retaining one-based capture indices linked to stable Google review IDs.
2. Apply the codebook semantically. For bookkeeping, a batch's reviewed texts use positive as the stored default with explicit negative/mixed/neutral/unclear exceptions; this follows reading the batch, not an automatic positive assumption for unseen records.
3. Keep blank-text records outside text sentiment; preserve every record in the public table.
4. Recheck selected ambiguous examples and verify label coverage. All 2,375 texts have exactly one sentiment label. A second independent annotator was not used.

The historical-archive totals are 2,130 positive, 122 mixed, 26 neutral, 94 negative and 3 unclear. No sentiment is inferred from stars. 76 five-star text reviews have a non-positive-only label.

## Reusable coding instruction

The following is a consolidated specification for reproducing the approach, **not a verbatim historical prompt transcript**:

> Read the entire customer text. Assign one of positive, mixed, neutral, negative or unclear using the codebook. Preserve explicit positive and negative experiences as mixed, including recovery. Do not infer sentiment from stars, other reviews or the desired business conclusion. Evaluate the target store, keep uncertainty visible, and do not invent missing text. Return the review ID and label; keep rating-only entries not applicable.

Theme flags are generated separately by [code_themes.py](code_themes.py), using [theme_dictionary.json](theme_dictionary.json). They are not model-generated semantic aspect judgements. The script expects locally held raw JSON; this repository does not redistribute that full text.

## Verification actually completed

- All captured IDs are unique and match listing totals; per-star totals reconcile.
- All non-empty texts were read for sentiment and included in aggregation.
- Rating-only entries remain identifiable; no sentiment categories were filled with invented data.
- Selected exceptions and the anticipatory-wait false positive were checked against raw wording.
- Charts are regenerated from public labels and checked visually.

**Human validation remains pending.** The blank `author_review.csv` worklist is now restricted to the main frame and selects up to ten records per store/label in capture order, including all scarce neutral/unclear cases. It is a stratified audit aid, not a random accuracy-test sample. Record disagreements and corrections before reporting any accuracy figure. An independent random sample would be needed for a defensible population-level accuracy estimate.

## Reproducibility boundary

Run `python3 build_windows.py` and then `python3 build_charts.py` to reproduce the time flags, subsets, counts and charts from the public archive. Raw local text → theme flags is reproducible with the dictionary and `code_themes.py`. Raw text → semantic sentiment is a judgement process and may differ on rerun. The private raw files are hashed in `collection_checks.json`; content hashes are integrity checks, not access to the source wording.
