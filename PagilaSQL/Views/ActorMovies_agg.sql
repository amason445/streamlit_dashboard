CREATE VIEW mrt.actor_movies_agg
AS
SELECT
    actor_name,
    fm.film_rating,
    MAX(fm.release_year) AS mostrecentappearance,
    MIN(fm.release_year) AS earliestappearance,
    COUNT(fm.film_rating) AS ratingfrequency,
    AVG(fm.film_length) AS avgmovielength
FROM mrt.actors ac
JOIN mrt.film_actor fac
    ON ac.actor_id = fac.actor_id
JOIN mrt.film_inventory fm
    ON fac.film_id = fm.film_id
GROUP BY
    actor_name,
    fm.film_rating
ORDER BY
    actor_name,
    fm.film_rating;