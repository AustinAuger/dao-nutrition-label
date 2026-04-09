# OGIS → DAO Nutrition Label Mapping

## Overview

The DAO Nutrition Label provides a human-readable summary of governance health and transparency.

The Open Governance Integrity Standard (OGIS) provides the underlying structured data that powers this label.

This document defines how OGIS data fields map to DAO Nutrition Label components.

---

## Mapping Table

| DAO Nutrition Label Field | OGIS Data Source | Description |
|--------------------------|----------------|-------------|
| Governance Participation | participation_rate_percent | Percentage of eligible tokens participating in the vote |
| Wallet Concentration     | top_5_wallet_concentration_percent | Share of voting power held by top wallets |
| Identity Verification    | verified_voter_percent | Percentage of voters with verified identity (if enabled) |
| Sentiment Integrity      | integrity_confidence_score | Confidence score indicating organic vs coordinated activity |
| Governance Risk Level    | treasury_impact_classification | Estimated impact level of proposal on treasury |

---

## Example

### OGIS Input (YAML)

```yaml
participation_rate_percent: 41
top_5_wallet_concentration_percent: 38
verified_voter_percent: 27
integrity_confidence_score: 0.92
treasury_impact_classification: "moderate"
