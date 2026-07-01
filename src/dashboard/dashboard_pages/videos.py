import streamlit as st
import pandas as pd

from src.dashboard.charts import (
    top_viewed_chart,
    top_liked_chart,
    top_commented_chart,
    engagement_chart,
    views_vs_likes,
    views_vs_comments,
    likes_vs_comments,
    bubble_chart
)

from src.dashboard.metrics import format_number


def show_videos(videos_df: pd.DataFrame, filters: dict):

    st.title("🎥 Video Analytics")

    st.markdown(
        "Analyze video performance using interactive charts and filters."
    )

    st.divider()

    df = videos_df.copy()

    # ----------------------------------------
    # Search
    # ----------------------------------------

    if filters["video_search"]:

        df = df[
            df["title"].str.contains(
                filters["video_search"],
                case=False,
                na=False
            )
        ]

    # ----------------------------------------
    # Minimum Views
    # ----------------------------------------

    df = df[
        df["view_count"] >= filters["minimum_views"]
    ]

    # ----------------------------------------
    # KPIs
    # ----------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Videos",
        len(df)
    )

    c2.metric(
        "Total Views",
        format_number(
            int(df["view_count"].sum())
        )
    )

    c3.metric(
        "Total Likes",
        format_number(
            int(df["like_count"].sum())
        )
    )

    c4.metric(
        "Total Comments",
        format_number(
            int(df["comment_count"].sum())
        )
    )

    st.divider()

    # ----------------------------------------
    # Engagement
    # ----------------------------------------

    df["engagement_rate"] = (

        (

            df["like_count"]

            +

            df["comment_count"]

        )

        /

        df["view_count"]

    ) * 100

    avg_engagement = round(

        df["engagement_rate"].mean(),

        2

    )

    st.metric(

        "Average Engagement Rate",

        f"{avg_engagement}%"

    )

    st.divider()

        # =====================================================
    # Top Viewed Videos
    # =====================================================

    st.subheader("👀 Top Viewed Videos")

    st.plotly_chart(

        top_viewed_chart(

            df,

            filters["top_n"]

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Top Liked Videos
    # =====================================================

    st.subheader("❤️ Top Liked Videos")

    st.plotly_chart(

        top_liked_chart(

            df,

            filters["top_n"]

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Top Commented Videos
    # =====================================================

    st.subheader("💬 Top Commented Videos")

    st.plotly_chart(

        top_commented_chart(

            df,

            filters["top_n"]

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Highest Engagement Videos
    # =====================================================

    st.subheader("🚀 Highest Engagement Videos")

    st.plotly_chart(

        engagement_chart(

            df,

            filters["top_n"]

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Scatter Charts
    # =====================================================

    st.subheader("📊 Relationship Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(

            views_vs_likes(

                df

            ),

            use_container_width=True

        )

    with col2:

        st.plotly_chart(

            views_vs_comments(

                df

            ),

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # Likes vs Comments
    # =====================================================

    st.subheader("👍 Likes vs Comments")

    st.plotly_chart(

        likes_vs_comments(

            df

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Bubble Chart
    # =====================================================

    st.subheader("🫧 Bubble Chart")

    st.plotly_chart(

        bubble_chart(

            df

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Performance Overview
    # =====================================================

    st.subheader("📈 Performance Summary")

    left, right = st.columns(2)

    with left:

        st.metric(

            "Highest Views",

            format_number(

                int(

                    df["view_count"].max()

                )

            )

        )

        st.metric(

            "Highest Likes",

            format_number(

                int(

                    df["like_count"].max()

                )

            )

        )

    with right:

        st.metric(

            "Highest Comments",

            format_number(

                int(

                    df["comment_count"].max()

                )

            )

        )

        st.metric(

            "Highest Engagement",

            f"{df['engagement_rate'].max():.2f}%"

        )

    st.divider()

        # =====================================================
    # Video Statistics
    # =====================================================

    st.subheader("📊 Video Statistics")

    stats = pd.DataFrame({

        "Metric": [

            "Total Videos",

            "Average Views",

            "Average Likes",

            "Average Comments",

            "Highest Engagement"

        ],

        "Value": [

            len(df),

            round(df["view_count"].mean()),

            round(df["like_count"].mean()),

            round(df["comment_count"].mean()),

            f"{df['engagement_rate'].max():.2f}%"

        ]

    })

    st.dataframe(

        stats,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Top 10 Videos Table
    # =====================================================

    st.subheader("🏆 Top Videos")

    top_table = (

        df

        .sort_values(

            by="view_count",

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

        .head(filters["top_n"])

    )

    st.dataframe(

        top_table,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Complete Dataset
    # =====================================================

    st.subheader("📋 Complete Video Dataset")

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Download CSV
    # =====================================================

    csv = df.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        label="⬇ Download Video Data",

        data=csv,

        file_name="videos.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # Insights
    # =====================================================

    st.subheader("💡 Video Insights")

    highest_view = df.loc[

        df["view_count"].idxmax()

    ]

    highest_like = df.loc[

        df["like_count"].idxmax()

    ]

    highest_comment = df.loc[

        df["comment_count"].idxmax()

    ]

    st.info(

        f"""
### Highest Viewed Video

{highest_view['title']}

👀 Views : {format_number(int(highest_view['view_count']))}

❤️ Likes : {format_number(int(highest_view['like_count']))}

💬 Comments : {format_number(int(highest_view['comment_count']))}
"""
    )

    st.success(

        f"""
### Most Liked Video

{highest_like['title']}

❤️ Likes : {format_number(int(highest_like['like_count']))}
"""
    )

    st.warning(

        f"""
### Most Discussed Video

{highest_comment['title']}

💬 Comments : {format_number(int(highest_comment['comment_count']))}
"""
    )

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption(

        "InfluenceIQ • Video Analytics Dashboard"

    )