import streamlit as st
import pandas as pd

from src.dashboard.metrics import (
    format_number,
)

from src.dashboard.charts import (
    sentiment_chart,
    spam_chart,
    abusive_chart,
    word_count_chart,
    character_count_chart,
)


def show_comments(

    comments_df: pd.DataFrame,

    filters: dict,

):

    st.title("💬 Comments Analytics")

    st.markdown(
        "Analyze YouTube comments using NLP filters."
    )

    st.divider()

    df = comments_df.copy()

    # ============================================
    # Search Comment
    # ============================================

    if filters["video_search"]:

        df = df[
            df["comment"].str.contains(
                filters["video_search"],
                case=False,
                na=False
            )
        ]

    # ============================================
    # Sentiment Filter
    # ============================================

    if filters["sentiment"]:

        df = df[
            df["sentiment"].isin(
                filters["sentiment"]
            )
        ]

    # ============================================
    # Spam Filter
    # ============================================

    if filters["spam_filter"] == "Spam":

        df = df[
            df["is_spam"] == True
        ]

    elif filters["spam_filter"] == "Normal":

        df = df[
            df["is_spam"] == False
        ]

    # ============================================
    # Abusive Filter
    # ============================================

    if filters["abusive_filter"] == "Abusive":

        df = df[
            df["contains_abusive_language"] == True
        ]

    elif filters["abusive_filter"] == "Normal":

        df = df[
            df["contains_abusive_language"] == False
        ]

    # ============================================
    # KPI Cards
    # ============================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "Comments",

        format_number(len(df))

    )

    c2.metric(

        "Spam",

        format_number(

            int(

                df["is_spam"].sum()

            )

        )

    )

    c3.metric(

        "Abusive",

        format_number(

            int(

                df["contains_abusive_language"].sum()

            )

        )

    )

    c4.metric(

        "Average Likes",

        round(

            df["likes"].mean(),

            2

        )

    )

    st.divider()

    # ============================================
    # Sentiment KPIs
    # ============================================

    positive = (

        df["sentiment"] == "Positive"

    ).sum()

    neutral = (

        df["sentiment"] == "Neutral"

    ).sum()

    negative = (

        df["sentiment"] == "Negative"

    ).sum()

    p1, p2, p3 = st.columns(3)

    p1.metric(

        "Positive",

        positive

    )

    p2.metric(

        "Neutral",

        neutral

    )

    p3.metric(

        "Negative",

        negative

    )

    st.divider()

    # ============================================
    # Comment Statistics
    # ============================================

    st.subheader("📊 Comment Statistics")

    s1, s2, s3 = st.columns(3)

    s1.metric(

        "Average Words",

        round(

            df["word_count"].mean(),

            2

        )

    )

    s2.metric(

        "Average Characters",

        round(

            df["character_count"].mean(),

            2

        )

    )

    s3.metric(

        "Average Likes",

        round(

            df["likes"].mean(),

            2

        )

    )

    st.divider()

        # =====================================================
    # Sentiment Distribution
    # =====================================================

    st.subheader("🧠 Sentiment Distribution")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.plotly_chart(

            sentiment_chart(

                df

            ),

            use_container_width=True

        )

    with col2:

        st.plotly_chart(

            spam_chart(

                df

            ),

            use_container_width=True

        )

    with col3:

        st.plotly_chart(

            abusive_chart(

                df

            ),

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # Word Count Distribution
    # =====================================================

    st.subheader("📝 Word Count Distribution")

    st.plotly_chart(

        word_count_chart(

            df

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Character Count Distribution
    # =====================================================

    st.subheader("📄 Character Count Distribution")

    st.plotly_chart(

        character_count_chart(

            df

        ),

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Top Liked Comments
    # =====================================================

    st.subheader("👍 Top Liked Comments")

    top_comments = (

        df

        .sort_values(

            by="likes",

            ascending=False

        )

        [

            [

                "author",

                "likes",

                "sentiment",

                "comment"

            ]

        ]

        .head(filters["top_n"])

    )

    st.dataframe(

        top_comments,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Longest Comments
    # =====================================================

    st.subheader("📚 Longest Comments")

    longest_comments = (

        df

        .sort_values(

            by="character_count",

            ascending=False

        )

        [

            [

                "author",

                "character_count",

                "comment"

            ]

        ]

        .head(filters["top_n"])

    )

    st.dataframe(

        longest_comments,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Most Active Users
    # =====================================================

    st.subheader("👤 Most Active Comment Authors")

    active_users = (

        df

        .groupby(

            "author"

        )

        .size()

        .reset_index(

            name="Total Comments"

        )

        .sort_values(

            by="Total Comments",

            ascending=False

        )

        .head(filters["top_n"])

    )

    st.dataframe(

        active_users,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Average Likes by Sentiment
    # =====================================================

    st.subheader("❤️ Average Likes by Sentiment")

    sentiment_likes = (

        df

        .groupby(

            "sentiment"

        )["likes"]

        .mean()

        .reset_index()

    )

    st.bar_chart(

        sentiment_likes,

        x="sentiment",

        y="likes"

    )

    st.divider()

    # =====================================================
    # NLP Summary
    # =====================================================

    st.subheader("📈 NLP Summary")

    summary = pd.DataFrame(

        {

            "Metric": [

                "Positive",

                "Neutral",

                "Negative",

                "Spam",

                "Abusive"

            ],

            "Count": [

                positive,

                neutral,

                negative,

                int(df["is_spam"].sum()),

                int(df["contains_abusive_language"].sum())

            ]

        }

    )

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

        # =====================================================
    # Complete Comments Dataset
    # =====================================================

    st.subheader("📋 Complete Comments Dataset")

    display_df = df[
        [
            "author",
            "likes",
            "sentiment",
            "is_spam",
            "contains_abusive_language",
            "word_count",
            "character_count",
            "comment"
        ]
    ]

    st.dataframe(

        display_df,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Download CSV
    # =====================================================

    csv = display_df.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        label="⬇ Download Comments CSV",

        data=csv,

        file_name="comments.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # Best Comment
    # =====================================================

    st.subheader("🏆 Most Liked Comment")

    best_comment = df.loc[

        df["likes"].idxmax()

    ]

    st.success(

        f"""

Author : {best_comment['author']}

Likes : {best_comment['likes']}

Sentiment : {best_comment['sentiment']}

Comment

{best_comment['comment']}

"""

    )

    st.divider()

    # =====================================================
    # Spam Insights
    # =====================================================

    st.subheader("🚫 Spam Insights")

    spam_df = df[

        df["is_spam"] == True

    ]

    if len(spam_df):

        st.info(

            f"""

Spam Comments Found : {len(spam_df)}

Spam Percentage : {(len(spam_df)/len(df))*100:.2f}%

"""

        )

    else:

        st.success(

            "No spam comments detected."

        )

    st.divider()

    # =====================================================
    # Abusive Insights
    # =====================================================

    st.subheader("🤬 Abusive Language Insights")

    abusive_df = df[

        df["contains_abusive_language"] == True

    ]

    if len(abusive_df):

        st.warning(

            f"""

Abusive Comments : {len(abusive_df)}

Percentage : {(len(abusive_df)/len(df))*100:.2f}%

"""

        )

    else:

        st.success(

            "No abusive comments detected."

        )

    st.divider()

    # =====================================================
    # Comment Length Analysis
    # =====================================================

    st.subheader("📏 Comment Length Analysis")

    shortest = df.loc[

        df["character_count"].idxmin()

    ]

    longest = df.loc[

        df["character_count"].idxmax()

    ]

    left, right = st.columns(2)

    with left:

        st.metric(

            "Shortest Comment",

            shortest["character_count"]

        )

    with right:

        st.metric(

            "Longest Comment",

            longest["character_count"]

        )

    st.divider()

    # =====================================================
    # Business Insights
    # =====================================================

    st.subheader("💡 Business Insights")

    st.markdown(f"""

- **Total Comments:** {len(df)}

- **Positive Comments:** {positive}

- **Neutral Comments:** {neutral}

- **Negative Comments:** {negative}

- **Spam Comments:** {int(df['is_spam'].sum())}

- **Abusive Comments:** {int(df['contains_abusive_language'].sum())}

- **Average Likes:** {round(df['likes'].mean(),2)}

- **Average Word Count:** {round(df['word_count'].mean(),2)}

- **Average Character Count:** {round(df['character_count'].mean(),2)}

- **Most Active Author:** {active_users.iloc[0]['author'] if not active_users.empty else 'N/A'}

""")

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption(

        "InfluenceIQ • Comments Analytics Dashboard"

    )