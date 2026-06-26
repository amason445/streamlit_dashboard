INSERT INTO mrt.film_actor
(
    actor_id,
    film_id
)
SELECT
    fa.actor_id,
    fa.film_id
FROM film_actor fa
ORDER BY
    fa.actor_id,
    fa.film_id;