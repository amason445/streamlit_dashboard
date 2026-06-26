ACTOR_SUMMARY_QUERY = """
SELECT
    CONCAT(INITCAP(first_name), ' ', INITCAP(last_name)) AS actor_name,
    fm.rating,
    MAX(fm.release_year) AS mostrecentappearance,
    MIN(fm.release_year) AS earliestappearance,
    COUNT(fm.rating) AS ratingfrequency,
    AVG(fm.length) AS avgmovielength
FROM actor ac
JOIN film_actor fac
    ON ac.actor_id = fac.actor_id
JOIN film fm
    ON fac.film_id = fm.film_id
GROUP BY
    actor_name,
    ac.first_name,
    ac.last_name,
    fm.rating
ORDER BY
    actor_name,
    fm.rating;
"""