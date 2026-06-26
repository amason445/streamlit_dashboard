INSERT INTO mrt.film_inventory
(
    film_id,
    title,
    description,
    release_year,
    film_language,
    film_rating,
    film_length
)
SELECT
    fm.film_id,
    fm.title,
    fm.description,
    fm.release_year,
    ln.name AS film_language,
    fm.rating AS film_rating,
    fm.length AS film_length
FROM film fm
LEFT JOIN language ln
    ON fm.language_id = ln.language_id
ORDER BY
    fm.title;