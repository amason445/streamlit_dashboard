ACTOR_SUMMARY_QUERY = """
    SELECT
        actor_name,
        rating,
        mostrecentappearance,
        earliestappearance,
        ratingfrequency,
        avgmovielength
    FROM actor_movies_agg
"""