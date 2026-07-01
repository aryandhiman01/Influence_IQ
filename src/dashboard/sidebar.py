import streamlit as st
import pandas as pd


def render_sidebar(
    channels_df: pd.DataFrame,
    videos_df: pd.DataFrame,
):
    """
    Render dashboard sidebar.
    """

    st.sidebar.title("🎯 InfluenceIQ")

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Dashboard Filters")

    # ----------------------------
    # Channel
    # ----------------------------

    channels = sorted(
        channels_df["channel_name"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_channel = st.sidebar.selectbox(
        "Select Channel",
        channels
    )

    # ----------------------------
    # Video Search
    # ----------------------------

    search_video = st.sidebar.text_input(
        "Search Video"
    )

    # ----------------------------
    # Minimum Views
    # ----------------------------

    min_views = int(
        videos_df["view_count"].min()
    )

    max_views = int(
        videos_df["view_count"].max()
    )

    selected_views = st.sidebar.slider(

        "Minimum Views",

        min_value=min_views,

        max_value=max_views,

        value=min_views

    )

    # ----------------------------
    # Sentiment
    # ----------------------------

    sentiment = st.sidebar.multiselect(

        "Sentiment",

        [

            "Positive",

            "Neutral",

            "Negative"

        ],

        default=[

            "Positive",

            "Neutral",

            "Negative"

        ]

    )

    # ----------------------------
    # Spam Filter
    # ----------------------------

    spam_filter = st.sidebar.selectbox(

        "Spam Filter",

        [

            "All",

            "Spam",

            "Normal"

        ]

    )

    # ----------------------------
    # Abusive Filter
    # ----------------------------

    abusive_filter = st.sidebar.selectbox(

        "Abusive Language",

        [

            "All",

            "Abusive",

            "Normal"

        ]

    )

    # ----------------------------
    # Top N
    # ----------------------------

    top_n = st.sidebar.slider(

        "Top Records",

        5,

        50,

        10

    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Project")

    st.sidebar.info(
        """
InfluenceIQ

YouTube Analytics &
NLP Dashboard

Powered by:

• PostgreSQL

• SQLAlchemy

• Pandas

• Plotly

• Streamlit
"""
    )

    return {

        "channel": selected_channel,

        "video_search": search_video,

        "minimum_views": selected_views,

        "sentiment": sentiment,

        "spam_filter": spam_filter,

        "abusive_filter": abusive_filter,

        "top_n": top_n,

    }