# Sentiment and theme codebook

## Current analysis frame

Main charts use the two-year relative-display-age proxy (1,112 texts); the one-year comparison uses 382 texts. The archive retains all 2,375 text labels. Theme denominators are text reviews **within the stated window**, not the full history. See [time-window rules](time_window_method.md). Classification definitions are unchanged by this revision.

## Unit of analysis

One unique Google customer-review ID at one selected store. Text may cover several visits or products; the whole displayed customer text is one unit. Owner replies are excluded. Rating-only records have `sentiment=not_applicable` and all theme flags 0; this means unavailable text, not neutral sentiment.

## Semantic sentiment

Every one of the 2,375 non-empty texts was read by Codex in batches. Stars were not used to determine the label.

| Label | Rule |
|---|---|
| Positive | Explicit favourable evaluation, recommendation, thanks or positive experience, without substantive criticism of the target store experience |
| Mixed | Explicit praise and criticism coexist, including good tea with poor service, price concerns despite enjoyment, or an initial failure followed by recovery |
| Negative | Explicit dissatisfaction or criticism without substantive praise of the target experience |
| Neutral | Factual/descriptive content without clear evaluation, including some identity-only or similarity-only statements |
| Unclear | Insufficient or ambiguous evaluative meaning; used for an ambiguous emoji, unclear phrasing or an implausible joke |

Mere queues, small size or a busy shop are not automatically negative. A complaint about waiting, space or price is. Contrasts against other businesses do not automatically make a review mixed. Mild preferences and implied dissatisfaction require judgement, so marginal cases remain suitable for human checking. All genuine text, including brief comments and emojis, stays in the denominator.

The final three unclear cases are T4-1320, TRUEDAN-0349 and TRUEDAN-0369. They are not forced into neutral. Whole-review labels cannot be interpreted as aspect-specific sentiment.

## Dictionary-based multi-label themes

All texts are matched case-insensitively against the exact regular expressions in [theme_dictionary.json](theme_dictionary.json). A theme is 1 if at least one match exists; repeated words do not increase the count. Denominator = text reviews at that store within the stated analysis window. Several themes may be 1 for one review; percentages can total more than 100%.

| Field | What is detected | Important limits |
|---|---|---|
| drink_product | Drink/product vocabulary, ingredients, taste, flavour and texture | Broad: generic “delicious” and dessert comments can match; not a drink-only quality score |
| staff_service | Staff/service terms, friendliness, helpfulness and conduct | Names alone do not match; inflections and implicit references can be missed |
| speed_waiting | Queue/wait, fast/slow/efficient and time vocabulary | Includes favourable and unfavourable mentions; some time references may be incidental |
| authenticity_origin | Authenticity, Taiwan/Taiwanese and home/homesickness language | Origin mentions do not necessarily praise authenticity or imply willingness to pay |
| price_value | Price, value, cost, discounts and promotion language | Includes both complaints and praise; not actual price benchmarking |
| customisation | Sugar/ice levels, percentages, adjustment and milk alternatives | Mentions are not proof of availability today |
| setting_location | Atmosphere, seating, cleanliness and location context | Combines environment and accessibility; not a measured location score |
| desserts_bakery | Ice cream, cakes, desserts, bakery and related items | Can overlap drinks, such as ice-cream toppings or sago |
| digital_delivery | Delivery, online/app, kiosk/machine and QR vocabulary | Includes ordering convenience as well as delivery; literal matches can be incidental |
| repeat_loyalty | Return intentions, loyalty and favourite/go-to language | Not observed repeat-purchase rate or customer lifetime value |

The speed detector removes selected anticipatory expressions such as “can't wait for my next visit” before matching. T4-0364 was checked as a false positive and corrected. “Can't wait any longer to order” is retained as waiting friction. The precise preprocessing is in [code_themes.py](code_themes.py).

The dictionary is transparent and reproducible but incomplete. It is **not** a second AI semantic classification of every theme, a validated classifier, or a measure of causal importance. Google translation may change matches. Topic counts are directional indicators for reading and testing; they do not prove the topics customers value most.
