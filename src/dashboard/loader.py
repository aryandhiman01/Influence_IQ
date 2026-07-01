import pandas as pd
import streamlit as st

from sqlalchemy import text

from src.database.connection import engine


@st.cache_data(show_spinner=False)
def load_data():

    with engine.connect() as connection:

        channels_df = pd.read_sql(

            text("SELECT * FROM channels"),

            connection

        )

        videos_df = pd.read_sql(

            text("SELECT * FROM videos"),

            connection

        )

        comments_df = pd.read_sql(

            text("SELECT * FROM comments"),

            connection

        )

    return (

        channels_df,

        videos_df,

        comments_df

    )