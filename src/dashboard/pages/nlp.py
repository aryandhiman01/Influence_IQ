import streamlit as st
import pandas as pd

from src.dashboard.metrics import (
    format_number
)

from src.dashboard.charts import (
    sentiment_chart,
    spam_chart,
    abusive_chart,
    word_count_chart,
    character_count_chart
)


def show_nlp(

    comments_df: pd.DataFrame,

    filters: dict

):

    st.title("🧠 NLP Analytics Dashboard")

    st.markdown(
        "Analyze audience behaviour using Natural Language Processing."
    )

    st.divider()

    df = comments_df.copy()

    # =====================================================
    # Sentiment Filter
    # =====================================================

    if filters["sentiment"]:

        df = df[

            df["sentiment"].isin(

                filters["sentiment"]

            )

        ]

    # =====================================================
    # Spam Filter
    # =====================================================

    if filters["spam_filter"] == "Spam":

        df = df[

            df["is_spam"]

        ]

    elif filters["spam_filter"] == "Normal":

        df = df[

            ~df["is_spam"]

        ]

    # =====================================================
    # Abusive Filter
    # =====================================================

    if filters["abusive_filter"] == "Abusive":

        df = df[

            df["contains_abusive_language"]

        ]

    elif filters["abusive_filter"] == "Normal":

        df = df[

            ~df["contains_abusive_language"]

        ]

    # =====================================================
    # KPI Calculation
    # =====================================================

    positive = (

        df["sentiment"] == "Positive"

    ).sum()

    neutral = (

        df["sentiment"] == "Neutral"

    ).sum()

    negative = (

        df["sentiment"] == "Negative"

    ).sum()

    spam = int(

        df["is_spam"].sum()

    )

    abusive = int(

        df["contains_abusive_language"].sum()

    )

    # =====================================================
    # KPI Cards
    # =====================================================

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(

        "Comments",

        format_number(

            len(df)

        )

    )

    c2.metric(

        "Positive",

        format_number(

            positive

        )

    )

    c3.metric(

        "Neutral",

        format_number(

            neutral

        )

    )

    c4.metric(

        "Negative",

        format_number(

            negative

        )

    )

    c5.metric(

        "Spam",

        format_number(

            spam

        )

    )

    st.divider()

    # =====================================================
    # Second KPI Row
    # =====================================================

    k1, k2, k3 = st.columns(3)

    k1.metric(

        "Abusive",

        abusive

    )

    k2.metric(

        "Average Words",

        round(

            df["word_count"].mean(),

            2

        )

    )

    k3.metric(

        "Average Characters",

        round(

            df["character_count"].mean(),

            2

        )

    )

    st.divider()

    # =====================================================
    # NLP Pie Charts
    # =====================================================

    st.subheader("📊 NLP Distribution")

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
    # NLP Histograms
    # =====================================================

    st.subheader("📈 Text Statistics")

    left, right = st.columns(2)

    with left:

        st.plotly_chart(

            word_count_chart(

                df

            ),

            use_container_width=True

        )

    with right:

        st.plotly_chart(

            character_count_chart(

                df

            ),

            use_container_width=True

        )

    st.divider()

        # =====================================================
    # Imports (Move these to the top of the file)
    # =====================================================

    from collections import Counter
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # =====================================================
    # Overall Word Cloud
    # =====================================================

    st.subheader("☁️ Overall Word Cloud")

    text = " ".join(

        df["clean_comment"]

        .fillna("")

        .astype(str)

    )

    if text.strip():

        wordcloud = WordCloud(

            width=1200,

            height=500,

            background_color="white"

        ).generate(text)

        fig, ax = plt.subplots(

            figsize=(14,6)

        )

        ax.imshow(wordcloud)

        ax.axis("off")

        st.pyplot(fig)

    else:

        st.info("No comments available.")

    st.divider()

    # =====================================================
    # Positive Word Cloud
    # =====================================================

    st.subheader("😊 Positive Word Cloud")

    positive_text = " ".join(

        df[

            df["sentiment"] == "Positive"

        ]["clean_comment"]

        .fillna("")

    )

    if positive_text.strip():

        wordcloud = WordCloud(

            width=1200,

            height=500,

            background_color="white"

        ).generate(positive_text)

        fig, ax = plt.subplots(

            figsize=(14,6)

        )

        ax.imshow(wordcloud)

        ax.axis("off")

        st.pyplot(fig)

    st.divider()

    # =====================================================
    # Negative Word Cloud
    # =====================================================

    st.subheader("😡 Negative Word Cloud")

    negative_text = " ".join(

        df[

            df["sentiment"] == "Negative"

        ]["clean_comment"]

        .fillna("")

    )

    if negative_text.strip():

        wordcloud = WordCloud(

            width=1200,

            height=500,

            background_color="white"

        ).generate(negative_text)

        fig, ax = plt.subplots(

            figsize=(14,6)

        )

        ax.imshow(wordcloud)

        ax.axis("off")

        st.pyplot(fig)

    st.divider()

    # =====================================================
    # Spam Word Cloud
    # =====================================================

    st.subheader("🚫 Spam Word Cloud")

    spam_text = " ".join(

        df[

            df["is_spam"]

        ]["clean_comment"]

        .fillna("")

    )

    if spam_text.strip():

        wordcloud = WordCloud(

            width=1200,

            height=500,

            background_color="white"

        ).generate(spam_text)

        fig, ax = plt.subplots(

            figsize=(14,6)

        )

        ax.imshow(wordcloud)

        ax.axis("off")

        st.pyplot(fig)

    else:

        st.success("No Spam Comments Found")

    st.divider()

    # =====================================================
    # Top Frequent Words
    # =====================================================

    st.subheader("🔥 Top 20 Frequent Words")

    words = text.split()

    counter = Counter(words)

    top_words = pd.DataFrame(

        counter.most_common(20),

        columns=[

            "Word",

            "Frequency"

        ]

    )

    st.dataframe(

        top_words,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Word Frequency Chart
    # =====================================================

    import plotly.express as px

    fig = px.bar(

        top_words,

        x="Frequency",

        y="Word",

        orientation="h",

        text="Frequency",

        title="Top 20 Most Frequent Words"

    )

    fig.update_layout(

        yaxis=dict(

            autorange="reversed"

        ),

        height=650

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Sentiment Comparison
    # =====================================================

    st.subheader("📈 Sentiment Comparison")

    comparison = pd.DataFrame({

        "Sentiment":[

            "Positive",

            "Neutral",

            "Negative"

        ],

        "Comments":[

            positive,

            neutral,

            negative

        ]

    })

    fig = px.bar(

        comparison,

        x="Sentiment",

        y="Comments",

        text="Comments",

        color="Sentiment",

        title="Sentiment Comparison"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

        # =====================================================
    # NLP Dataset
    # =====================================================

    st.subheader("📋 NLP Dataset")

    display_df = df[
        [
            "author",
            "clean_comment",
            "sentiment",
            "is_spam",
            "contains_abusive_language",
            "word_count",
            "character_count",
            "likes"
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

    ).encode("utf-8")

    st.download_button(

        label="⬇ Download NLP Dataset",

        data=csv,

        file_name="nlp_dataset.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # NLP Statistics
    # =====================================================

    st.subheader("📊 NLP Statistics")

    stats = pd.DataFrame({

        "Metric":[

            "Total Comments",

            "Positive",

            "Neutral",

            "Negative",

            "Spam",

            "Abusive",

            "Average Words",

            "Average Characters",

            "Average Likes"

        ],

        "Value":[

            len(df),

            positive,

            neutral,

            negative,

            spam,

            abusive,

            round(

                df["word_count"].mean(),

                2

            ),

            round(

                df["character_count"].mean(),

                2

            ),

            round(

                df["likes"].mean(),

                2

            )

        ]

    })

    st.dataframe(

        stats,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Highest Liked Positive Comment
    # =====================================================

    st.subheader("🏆 Top Positive Comment")

    positive_df = df[

        df["sentiment"] == "Positive"

    ]

    if not positive_df.empty:

        best_positive = positive_df.loc[

            positive_df["likes"].idxmax()

        ]

        st.success(f"""

Author : **{best_positive['author']}**

Likes : **{best_positive['likes']}**

Comment

{best_positive['comment']}

""")

    st.divider()

    # =====================================================
    # Highest Liked Negative Comment
    # =====================================================

    st.subheader("😡 Top Negative Comment")

    negative_df = df[

        df["sentiment"] == "Negative"

    ]

    if not negative_df.empty:

        best_negative = negative_df.loc[

            negative_df["likes"].idxmax()

        ]

        st.error(f"""

Author : **{best_negative['author']}**

Likes : **{best_negative['likes']}**

Comment

{best_negative['comment']}

""")

    else:

        st.success(

            "No negative comments found."

        )

    st.divider()

    # =====================================================
    # Spam Summary
    # =====================================================

    st.subheader("🚫 Spam Analysis")

    spam_percentage = round(

        (spam / len(df)) * 100,

        2

    )

    st.info(f"""

Spam Comments : **{spam}**

Spam Percentage : **{spam_percentage}%**

""")

    st.divider()

    # =====================================================
    # Abusive Summary
    # =====================================================

    st.subheader("🤬 Abusive Language Analysis")

    abusive_percentage = round(

        (abusive / len(df)) * 100,

        2

    )

    st.warning(f"""

Abusive Comments : **{abusive}**

Abusive Percentage : **{abusive_percentage}%**

""")

    st.divider()

    # =====================================================
    # Business Insights
    # =====================================================

    st.subheader("💡 NLP Business Insights")

    st.markdown(f"""

### Key Findings

- Total Comments Analysed : **{len(df)}**

- Positive Comments : **{positive}**

- Neutral Comments : **{neutral}**

- Negative Comments : **{negative}**

- Spam Comments : **{spam}**

- Abusive Comments : **{abusive}**

- Average Word Count : **{round(df['word_count'].mean(),2)}**

- Average Character Count : **{round(df['character_count'].mean(),2)}**

- Average Likes : **{round(df['likes'].mean(),2)}**

""")

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption(

        "InfluenceIQ • NLP Analytics Dashboard"

    )