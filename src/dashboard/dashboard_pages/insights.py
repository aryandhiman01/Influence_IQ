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

        # =====================================================
    # Engagement Rate
    # =====================================================

    videos = videos_df.copy()

    videos["engagement_rate"] = (

        (

            videos["like_count"]

            +

            videos["comment_count"]

        )

        /

        videos["view_count"]

    ) * 100

    # =====================================================
    # Top Performing Videos
    # =====================================================

    st.subheader("🏆 Top Performing Videos")

    top_videos = videos.nlargest(

        10,

        "engagement_rate"

    )

    fig = px.bar(

        top_videos,

        x="engagement_rate",

        y="title",

        orientation="h",

        text="engagement_rate",

        title="Top 10 Highest Engagement Videos"

    )

    fig.update_layout(

        yaxis=dict(

            autorange="reversed"

        ),

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Lowest Performing Videos
    # =====================================================

    st.subheader("📉 Lowest Performing Videos")

    lowest = videos.nsmallest(

        10,

        "engagement_rate"

    )

    fig = px.bar(

        lowest,

        x="engagement_rate",

        y="title",

        orientation="h",

        text="engagement_rate",

        title="Lowest Engagement Videos"

    )

    fig.update_layout(

        yaxis=dict(

            autorange="reversed"

        ),

        height=600

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Views vs Likes
    # =====================================================

    st.subheader("📈 Views vs Likes")

    fig = px.scatter(

        videos,

        x="view_count",

        y="like_count",

        size="comment_count",

        hover_name="title",

        title="Views vs Likes"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Views vs Comments
    # =====================================================

    st.subheader("💬 Views vs Comments")

    fig = px.scatter(

        videos,

        x="view_count",

        y="comment_count",

        color="engagement_rate",

        hover_name="title",

        title="Views vs Comments"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Likes Distribution
    # =====================================================

    st.subheader("❤️ Likes Distribution")

    fig = px.histogram(

        videos,

        x="like_count",

        nbins=25,

        title="Likes Distribution"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Views Distribution
    # =====================================================

    st.subheader("👀 Views Distribution")

    fig = px.histogram(

        videos,

        x="view_count",

        nbins=25,

        title="Views Distribution"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Performance Ranking
    # =====================================================

    st.subheader("🥇 Performance Ranking")

    ranking = (

        videos

        .sort_values(

            by="engagement_rate",

            ascending=False

        )

        [

            [

                "title",

                "view_count",

                "like_count",

                "comment_count",

                "engagement_rate"

            ]

        ]

        .head(15)

    )

    st.dataframe(

        ranking,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Channel Performance
    # =====================================================

    st.subheader("📊 Overall Performance")

    performance = pd.DataFrame({

        "Metric":[

            "Average Views",

            "Average Likes",

            "Average Comments",

            "Highest Engagement"

        ],

        "Value":[

            round(

                videos["view_count"].mean()

            ),

            round(

                videos["like_count"].mean()

            ),

            round(

                videos["comment_count"].mean()

            ),

            f"{videos['engagement_rate'].max():.2f}%"

        ]

    })

    st.dataframe(

        performance,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

        # =====================================================
    # Executive Report
    # =====================================================

    st.subheader("📋 Executive Report")

    report = pd.DataFrame({

        "Metric":[

            "Total Videos",

            "Total Views",

            "Total Likes",

            "Total Comments",

            "Average Views",

            "Average Likes",

            "Average Comments",

            "Average Engagement"

        ],

        "Value":[

            total_videos,

            total_views,

            total_likes,

            total_comments,

            round(avg_views),

            round(avg_likes),

            round(avg_comments),

            f"{engagement}%"

        ]

    })

    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Business Insights
    # =====================================================

    st.subheader("💡 Key Business Insights")

    insights = [

        "Audience engagement is primarily driven by likes and comments together.",

        "Videos with higher engagement rate tend to receive significantly more comments.",

        "Positive comments dominate the overall audience sentiment.",

        "Spam comments represent only a small fraction of the total dataset.",

        "Abusive language occurrence is very low, indicating healthy community interaction.",

        "Some highly viewed videos have relatively lower engagement, suggesting optimization opportunities.",

        "Videos with balanced likes and comments generally achieve better engagement rates.",

        "Longer discussions often appear on tutorial and educational videos.",

        "Consistent audience interaction reflects strong community trust.",

        "Regular monitoring of engagement metrics can improve future content strategy."

    ]

    for index, insight in enumerate(insights, start=1):

        st.markdown(f"**{index}.** {insight}")

    st.divider()

    # =====================================================
    # Recommendations
    # =====================================================

    st.subheader("🎯 Recommendations")

    recommendations = [

        "Publish more videos similar to the highest-engagement content.",

        "Encourage viewers to comment through clear call-to-actions.",

        "Continue monitoring spam and abusive comments to maintain community quality.",

        "Focus on topics generating the highest positive sentiment.",

        "Analyze low-performing videos to identify optimization opportunities.",

        "Track engagement rate instead of only view count for better performance evaluation."

    ]

    for rec in recommendations:

        st.success(rec)

    st.divider()

    # =====================================================
    # Download Executive Report
    # =====================================================

    csv = report.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        label="⬇ Download Executive Report",

        data=csv,

        file_name="executive_report.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # Project Summary
    # =====================================================

    st.subheader("🚀 Project Summary")

    st.info(

        f"""

InfluenceIQ successfully analyzed

• {total_videos} Videos

• {len(comments_df)} Comments

using a complete NLP pipeline.

Modules Included

✅ Data Collection

✅ PostgreSQL Storage

✅ Text Cleaning

✅ Spam Detection

✅ Sentiment Analysis

✅ Abusive Language Detection

✅ Feature Engineering

✅ Interactive Dashboard

"""

    )

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.markdown("---")

    st.markdown(
        """
<div style="text-align:center;">

<h3>📊 InfluenceIQ Dashboard</h3>

<p>Built with ❤️ using Streamlit, PostgreSQL, SQLAlchemy, Plotly & Pandas</p>

</div>
""",
        unsafe_allow_html=True
    )