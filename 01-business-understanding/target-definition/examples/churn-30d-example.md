# Example — Churn 30 days

- Unit of analysis: customer_id at reference_date.
- Positive class: customer with no eligible transaction during the next 30 days.
- Negative class: customer with at least one eligible transaction during the next 30 days.
- Observation window: previous 90 days.
- Gap window: 0 days.
- Performance window: next 30 days.
- Exclusion: customers without enough history or whose performance window is not mature.
