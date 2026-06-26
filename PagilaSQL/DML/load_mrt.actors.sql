INSERT INTO mrt.actors
(
    actor_id,
    actor_name
)
SELECT
    actor_id,
    CONCAT(INITCAP(first_name), ' ', INITCAP(last_name)) AS actor_name
FROM actor
ORDER BY
    actor_id;