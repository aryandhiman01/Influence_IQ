import plotly.express as px
import pandas as pd


# ======================================================
# Top Viewed Videos
# ======================================================

def top_viewed_chart(videos_df: pd.DataFrame, top_n: int = 10):

    df = videos_df.nlargest(top_n, "view_count")

    fig = px.bar(
        df,
        x="view_count",
        y="title",
        orientation="h",
        text="view_count",
        title=f"Top {top_n} Most Viewed Videos"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=550
    )

    return fig


# ======================================================
# Top Liked Videos
# ======================================================

def top_liked_chart(videos_df: pd.DataFrame, top_n: int = 10):

    df = videos_df.nlargest(top_n, "like_count")

    fig = px.bar(
        df,
        x="like_count",
        y="title",
        orientation="h",
        text="like_count",
        title=f"Top {top_n} Most Liked Videos"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=550
    )

    return fig


# ======================================================
# Top Commented Videos
# ======================================================

def top_commented_chart(videos_df: pd.DataFrame, top_n: int = 10):

    df = videos_df.nlargest(top_n, "comment_count")

    fig = px.bar(
        df,
        x="comment_count",
        y="title",
        orientation="h",
        text="comment_count",
        title=f"Top {top_n} Most Commented Videos"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=550
    )

    return fig


# ======================================================
# Sentiment Distribution
# ======================================================

def sentiment_chart(comments_df: pd.DataFrame):

    df = (
        comments_df["sentiment"]
        .value_counts()
        .reset_index()
    )

    df.columns = ["Sentiment", "Count"]

    fig = px.pie(
        df,
        names="Sentiment",
        values="Count",
        title="Sentiment Distribution"
    )

    return fig


# ======================================================
# Spam Distribution
# ======================================================

def spam_chart(comments_df: pd.DataFrame):

    df = (
        comments_df["is_spam"]
        .value_counts()
        .reset_index()
    )

    df.columns = ["Spam", "Count"]

    df["Spam"] = df["Spam"].replace(
        {
            True: "Spam",
            False: "Normal"
        }
    )

    fig = px.pie(
        df,
        names="Spam",
        values="Count",
        title="Spam Detection"
    )

    return fig


# ======================================================
# Abusive Language
# ======================================================

def abusive_chart(comments_df: pd.DataFrame):

    df = (
        comments_df["contains_abusive_language"]
        .value_counts()
        .reset_index()
    )

    df.columns = ["Type", "Count"]

    df["Type"] = df["Type"].replace(
        {
            True: "Abusive",
            False: "Normal"
        }
    )

    fig = px.pie(
        df,
        names="Type",
        values="Count",
        title="Abusive Language Detection"
    )

    return fig


# ======================================================
# Word Count Histogram
# ======================================================

def word_count_chart(comments_df: pd.DataFrame):

    fig = px.histogram(
        comments_df,
        x="word_count",
        nbins=30,
        title="Word Count Distribution"
    )

    return fig


# ======================================================
# Character Count Histogram
# ======================================================

def character_count_chart(comments_df: pd.DataFrame):

    fig = px.histogram(
        comments_df,
        x="character_count",
        nbins=30,
        title="Character Count Distribution"
    )

    return fig


# ======================================================
# Views vs Likes
# ======================================================

def views_vs_likes(videos_df: pd.DataFrame):

    fig = px.scatter(
        videos_df,
        x="view_count",
        y="like_count",
        hover_name="title",
        title="Views vs Likes"
    )

    return fig


# ======================================================
# Views vs Comments
# ======================================================

def views_vs_comments(videos_df: pd.DataFrame):

    fig = px.scatter(
        videos_df,
        x="view_count",
        y="comment_count",
        hover_name="title",
        title="Views vs Comments"
    )

    return fig


# ======================================================
# Likes vs Comments
# ======================================================

def likes_vs_comments(videos_df: pd.DataFrame):

    fig = px.scatter(
        videos_df,
        x="like_count",
        y="comment_count",
        hover_name="title",
        title="Likes vs Comments"
    )

    return fig


# ======================================================
# Engagement Rate
# ======================================================

def engagement_chart(videos_df: pd.DataFrame, top_n: int = 10):

    df = videos_df.copy()

    df["engagement_rate"] = (
        (
            df["like_count"]
            +
            df["comment_count"]
        )
        /
        df["view_count"]
    ) * 100

    df = df.nlargest(top_n, "engagement_rate")

    fig = px.bar(
        df,
        x="engagement_rate",
        y="title",
        orientation="h",
        text="engagement_rate",
        title="Highest Engagement Rate"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        height=550
    )

    return fig


# ======================================================
# Bubble Chart
# ======================================================

def bubble_chart(videos_df: pd.DataFrame):

    fig = px.scatter(
        videos_df,
        x="view_count",
        y="like_count",
        size="comment_count",
        hover_name="title",
        title="Views • Likes • Comments"
    )

    return fig