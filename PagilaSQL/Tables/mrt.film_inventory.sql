CREATE TABLE mrt.film_inventory
(
    film_id         INTEGER PRIMARY KEY,
    title           VARCHAR(255),
    description     TEXT,
    release_year    INTEGER,
    film_language   VARCHAR(20),
    film_rating     VARCHAR(10),
    film_length     INTEGER
);