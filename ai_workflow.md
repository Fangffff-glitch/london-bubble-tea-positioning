# AI use: historical brief versus new pilot

## Historical brief

The submitted assignment declares Gemini 1.5 Flash for semantic analysis and proofreading. Historical prompts/model provenance have not been independently recovered. NotebookLM stores research inputs and derived notes; its summary is not independent verification.

## New pilot, 5 November 2026

Codex (GPT-6-based assistant in this task) operated the public Google Maps UI, inspected 60 candidate cards, expanded long reviews, excluded seven records and assigned provisional labels to 53 customer texts. Labels were semantic judgements in the assistant conversation, not predictions from a separately trained model or an external API batch. No sampling temperature, model checkpoint or exact reproducible inference configuration was recorded.

The assistant checked owner-response leakage, exclusion rules, ambiguous polarity and theme boundaries in a second reading. This is **AI self-review, not a second human coder or independent validation**. Author review is pending in author_review.csv. Python code then aggregates fixed labels and renders charts. No Python sentiment classifier or model-accuracy statistic is claimed.

## Coding instruction specification used for this extension

Read only the displayed customer text and the codebook. Assign overall positive/negative/mixed/neutral sentiment; assign multiple explicit themes with polarity. Preserve positive and negative aspects within the same review. Do not infer commuter status, nationality, actual ingredients or commercial outcomes. Do not classify owner replies as customer text. Exclude absent text and explicitly historical out-of-scope experience; record the reason. Flag ambiguous classifications and keep source identity and date metadata.

This is a documented instruction specification, not a fabricated verbatim historical Gemini prompt or a standalone prompt log. The public table contains the resulting labels, concise paraphrases and judgement notes. Changes from the initial proposed protocol are documented in collection.md.

## Remaining author review

Check all 53 rows against their sources if feasible, especially translated and mixed records; record any changes without overwriting the AI label. No author decisions have been filled on their behalf. Re-run build_charts.py if labels change. Author-AI agreement would measure consistency with that reviewer, not validated classifier accuracy.
