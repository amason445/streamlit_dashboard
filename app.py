import altair as alt
import streamlit as st

from database import get_dataframe
from queries import ACTOR_SUMMARY_QUERY

st.title("Pagila Actors Dashboard")

df = get_dataframe(ACTOR_SUMMARY_QUERY)

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