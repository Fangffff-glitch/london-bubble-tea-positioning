# Coding definitions

**Status: proposed definitions for new or reconstructed review-level analysis.**

## Overall sentiment

| Label | Rule |
|---|---|
| Positive | Clear favourable evaluation without a substantive negative evaluation |
| Negative | Clear unfavourable evaluation without a substantive positive evaluation |
| Mixed | Both substantive favourable and unfavourable evaluations |
| Neutral | Descriptive or informational text with no clear evaluative direction |

Unclear, unreadable or insufficient text receives a separate needs_review flag; do not force it into neutral. Star ratings are retained for context but do not determine the text label.

## Themes (multiple labels allowed)

| Theme | Include |
|---|---|
| Taste and texture | Flavour, sweetness, tea strength, pearl texture |
| Ingredients and authenticity | Explicit ingredient claims or references to authenticity/home |
| Price and value | Cost, portion value, discounts, worth paying |
| Waiting and speed | Queue, preparation, pickup or perceived speed |
| Staff and service | Courtesy, helpfulness, order accuracy |
| Convenience and setting | Location, access, seating, ordering arrangements |
| Packaging | Lids, leaks, transportability |

Assign positive, negative, mixed or neutral polarity to each mentioned theme. Record the supporting evidence span privately. Do not infer nationality, commuter identity, health outcomes or actual ingredient composition from a review.

**Synthetic illustration, not collected data:** “The pearls tasted great, but the wait was too long.” → overall mixed; taste positive; waiting negative.
