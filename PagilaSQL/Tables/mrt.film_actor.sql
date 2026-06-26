CREATE TABLE mrt.film_actor
(
    actor_id    INTEGER NOT NULL,
    film_id     INTEGER NOT NULL,

    CONSTRAINT pk_film_actor
        PRIMARY KEY (actor_id, film_id)
);