import os
import pandas as pd
import psycopg
import streamlit as st
import altair as alt
from dotenv import load_dotenv

load_dotenv()

st.title("Pagila Actors Dashboard")

conn = psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

query = """
    SELECT
        CONCAT(INITCAP(first_name), ' ', INITCAP(last_name)) AS actor_name,
        fm.rating,
        max(fm.release_year) AS MostRecentAppearance,
        min(fm.release_year) AS EarliestAppearance,
        count(fm.rating) AS RatingFrequency,
        sum(fm.length) / count(DISTINCT fm.film_id) AS AvgMovieLength
    FROM actor ac
    INNER JOIN film_actor fac ON
        ac.actor_id = fac.actor_id
    INNER JOIN film fm ON
        fac.film_id = fm.film_id
    GROUP BY
        CONCAT(INITCAP(first_name), ' ', INITCAP(last_name)),
        ac.first_name,
        ac.last_name,
        fm.rating
    ORDER BY 
        actor_name,
        fm.rating
"""

df = pd.read_sql(query, conn)

conn.close()

st.subheader("Actor Film Summary by Rating")

rating_options = ["All"] + sorted(df["rating"].dropna().unique().tolist())
actor_options = ["All"] + sorted(df["actor_name"].dropna().unique().tolist())

rating_filter = st.selectbox(
    "Filter by rating",
    options=rating_options
)

actor_filter = st.selectbox(
    "Filter by actor",
    options=actor_options
)

filtered_df = df.copy()

if rating_filter != "All":
    filtered_df = filtered_df[filtered_df["rating"] == rating_filter]

if actor_filter != "All":
    filtered_df = filtered_df[filtered_df["actor_name"] == actor_filter]

st.subheader("Rating Frequency & Average Movie Length")

chart_df = (
    filtered_df
    .groupby("rating", as_index=False)
    .agg(
        RatingFrequency=("ratingfrequency", "sum"),
        AvgMovieLength=("avgmovielength", "mean")
    )
)

bars = (
    alt.Chart(chart_df)
    .mark_bar()
    .encode(
        x=alt.X("rating:N", title="Rating"),
        y=alt.Y("RatingFrequency:Q", title="Rating Frequency")
    )
)

line = (
    alt.Chart(chart_df)
    .mark_line(point=True, color="red")
    .encode(
        x="rating:N",
        y=alt.Y("AvgMovieLength:Q", title="Average Movie Length")
    )
)

st.altair_chart(
    alt.layer(bars, line).resolve_scale(
        y="independent"
    ),
    use_container_width=True
)

st.subheader("Filtered Results")
st.dataframe(filtered_df)