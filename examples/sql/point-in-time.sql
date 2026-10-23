-- Portable SQL core; tested with SQLite, not executed in Databricks.
-- anchors: one row per (entity_id, reference_time).
-- events: deduplicated events; timestamps in the same ISO format and timezone.
-- Zero activity is valid only if source coverage for the window is known complete.
SELECT
    a.entity_id,
    a.reference_time,
    COUNT(e.event_id) AS observed_events,
    COALESCE(SUM(e.amount), 0) AS observed_amount
FROM anchors AS a
LEFT JOIN events AS e
    ON e.entity_id = a.entity_id
    AND e.event_time >= a.observation_start
    AND e.event_time < a.reference_time
    AND e.available_at <= a.reference_time
GROUP BY a.entity_id, a.reference_time;
