import streamlit as st
import pandas as pd
import plotly.express as px

from src.dashboard.metrics import (
    format_number,
)


def show_insights(

    videos_df: pd.DataFrame,

    comments_df: pd.DataFrame,

):

    st.title("📈 Executive Business Insights")

    st.markdown(
        "High level analytics for business decision making."
    )

    st.divider()

    # =====================================================
    # KPI Calculations
    # =====================================================

    total_views = int(

        videos_df["view_count"].sum()

    )

    total_likes = int(

        videos_df["like_count"].sum()

    )

    total_comments = int(

        videos_df["comment_count"].sum()

    )

    total_videos = len(

        videos_df

    )

    avg_views = round(

        videos_df["view_count"].mean(),

        2

    )

    avg_likes = round(

        videos_df["like_count"].mean(),

        2

    )

    avg_comments = round(

        videos_df["comment_count"].mean(),

        2

    )

    engagement = round(

        (

            (

                videos_df["like_count"]

                +

                videos_df["comment_count"]

            )

            /

            videos_df["view_count"]

        ).mean()

        * 100,

        2

    )

    # =====================================================
    # KPI Cards
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "Videos",

        total_videos

    )

    c2.metric(

        "Views",

        format_number(

            total_views

        )

    )

    c3.metric(

        "Likes",

        format_number(

            total_likes

        )

    )

    c4.metric(

        "Comments",

        format_number(

            total_comments

        )

    )

    st.divider()

    # =====================================================
    # Average KPIs
    # =====================================================

    a1, a2, a3, a4 = st.columns(4)

    a1.metric(

        "Average Views",

        format_number(

            int(avg_views)

        )

    )

    a2.metric(

        "Average Likes",

        format_number(

            int(avg_likes)

        )

    )

    a3.metric(

        "Average Comments",

        format_number(

            int(avg_comments)

        )

    )

    a4.metric(

        "Avg Engagement",

        f"{engagement}%"

    )

    st.divider()

    # =====================================================
    # Sentiment Overview
    # =====================================================

    positive = (

        comments_df["sentiment"]

        ==

        "Positive"

    ).sum()

    neutral = (

        comments_df["sentiment"]

        ==

        "Neutral"

    ).sum()

    negative = (

        comments_df["sentiment"]

        ==

        "Negative"

    ).sum()

    spam = int(

        comments_df["is_spam"].sum()

    )

    abusive = int(

        comments_df["contains_abusive_language"].sum()

    )

    s1, s2, s3, s4, s5 = st.columns(5)

    s1.metric(

        "Positive",

        positive

    )

    s2.metric(

        "Neutral",

        neutral

    )

    s3.metric(

        "Negative",

        negative

    )

    s4.metric(

        "Spam",

        spam

    )

    s5.metric(

        "Abusive",

        abusive

    )

    st.divider()

    # =====================================================
    # Executive Summary Table
    # =====================================================

    summary = pd.DataFrame({

        "Metric":[

            "Videos",

            "Views",

            "Likes",

            "Comments",

            "Positive",

            "Neutral",

            "Negative",

            "Spam",

            "Abusive",

            "Average Engagement"

        ],

        "Value":[

            total_videos,

            total_views,

            total_likes,

            total_comments,

            positive,

            neutral,

            negative,

            spam,

            abusive,

            f"{engagement}%"

        ]

    })

    st.subheader("📊 Executive Summary")

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    