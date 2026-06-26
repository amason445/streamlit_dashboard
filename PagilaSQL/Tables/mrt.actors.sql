CREATE TABLE mrt.actors
(
    actor_id    INTEGER NOT NULL,
    actor_name  VARCHAR(101) NOT NULL,

    CONSTRAINT pk_actor
        PRIMARY KEY (actor_id)
);