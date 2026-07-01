import streamlit as st

from src.dashboard.metrics import format_number

from src.dashboard.charts import (
    sentiment_chart,
    spam_chart,
    abusive_chart,
    top_viewed_chart,
    engagement_chart
)


def show_home(

    channels_df,

    videos_df,

    comments_df,

    metrics,

    filters

):

    st.title("📊 InfluenceIQ Dashboard")

    st.caption(
        "YouTube Analytics & NLP Dashboard"
    )

    st.divider()

    # =====================================================
    # KPI Cards
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Subscribers",
        format_number(
            metrics["total_subscribers"]
        )
    )

    c2.metric(
        "Views",
        format_number(
            metrics["total_views"]
        )
    )

    c3.metric(
        "Videos",
        metrics["total_videos"]
    )

    c4.metric(
        "Comments",
        metrics["total_comments"]
    )

    st.divider()

    c5, c6, c7, c8 = st.columns(4)

    c5.metric(
        "Positive",
        metrics["positive_comments"]
    )

    c6.metric(
        "Neutral",
        metrics["neutral_comments"]
    )

    c7.metric(
        "Negative",
        metrics["negative_comments"]
    )

    c8.metric(
        "Spam",
        metrics["spam_comments"]
    )

    st.divider()

    # =====================================================
    # Average Statistics
    # =====================================================

    st.subheader("📈 Average Statistics")

    a1, a2, a3, a4 = st.columns(4)

    a1.metric(
        "Avg Views",
        format_number(
            int(metrics["average_views"])
        )
    )

    a2.metric(
        "Avg Likes",
        format_number(
            int(metrics["average_likes"])
        )
    )

    a3.metric(
        "Avg Comments",
        format_number(
            int(metrics["average_comments"])
        )
    )

    a4.metric(
        "Engagement",
        f"{metrics['average_engagement']}%"
    )

    st.divider()

    # =====================================================
    # Pie Charts
    # =====================================================

    st.subheader("🧠 NLP Overview")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.plotly_chart(

            sentiment_chart(

                comments_df

            ),

            use_container_width=True

        )

    with col2:

        st.plotly_chart(

            spam_chart(

                comments_df

            ),

            use_container_width=True

        )

    with col3:

        st.plotly_chart(

            abusive_chart(

                comments_df

            ),

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # Top Viewed Videos
    # =====================================================

    st.subheader("🎥 Top Viewed Videos")

    st.plotly_chart(

        top_viewed_chart(

            videos_df,

            filters["top_n"]

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Engagement Chart
    # =====================================================

    st.subheader("🚀 Highest Engagement")

    st.plotly_chart(

        engagement_chart(

            videos_df,

            filters["top_n"]

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Recent Videos
    # =====================================================

    st.subheader("📺 Latest Videos")

    latest = videos_df.sort_values(

        by="published_at",

        ascending=False

    )

    st.dataframe(

        latest[

            [

                "title",

                "view_count",

                "like_count",

                "comment_count"

            ]

        ].head(10),

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Dataset Summary
    # =====================================================

    st.subheader("📌 Dataset Summary")

    left, right = st.columns(2)

    with left:

        st.info(f"""
Channels : {len(channels_df)}

Videos : {len(videos_df)}

Comments : {len(comments_df)}
""")

    with right:

        st.success(f"""
Positive : {metrics["positive_comments"]}

Neutral : {metrics["neutral_comments"]}

Negative : {metrics["negative_comments"]}
""")

    st.divider()

    st.caption(
        "InfluenceIQ • YouTube Analytics Dashboard"
    )