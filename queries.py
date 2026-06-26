ACTOR_SUMMARY_QUERY = """
    SELECT
        actor_name,
        film_rating as rating,
        mostrecentappearance,
        earliestappearance,
        ratingfrequency,
        avgmovielength
    FROM mrt.actor_movies_agg
"""