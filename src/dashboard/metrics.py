import pandas as pd


def get_dashboard_metrics(
    channels_df: pd.DataFrame,
    videos_df: pd.DataFrame,
    comments_df: pd.DataFrame,
) -> dict:
    """
    Calculate all dashboard KPIs.
    """

    total_subscribers = int(
        channels_df["subscriber_count"].sum()
    )

    total_views = int(
        channels_df["total_views"].sum()
    )

    total_channels = len(channels_df)

    total_videos = len(videos_df)

    total_comments = len(comments_df)

    total_likes = int(
        videos_df["like_count"].sum()
    )

    total_video_comments = int(
        videos_df["comment_count"].sum()
    )

    positive_comments = int(
        (
            comments_df["sentiment"] == "Positive"
        ).sum()
    )

    neutral_comments = int(
        (
            comments_df["sentiment"] == "Neutral"
        ).sum()
    )

    negative_comments = int(
        (
            comments_df["sentiment"] == "Negative"
        ).sum()
    )

    spam_comments = int(
        comments_df["is_spam"].sum()
    )

    abusive_comments = int(
        comments_df[
            "contains_abusive_language"
        ].sum()
    )

    average_views = round(
        videos_df["view_count"].mean(),
        2
    )

    average_likes = round(
        videos_df["like_count"].mean(),
        2
    )

    average_comments = round(
        videos_df["comment_count"].mean(),
        2
    )

    average_words = round(
        comments_df["word_count"].mean(),
        2
    )

    average_characters = round(
        comments_df["character_count"].mean(),
        2
    )

    average_engagement = round(
        (
            (
                videos_df["like_count"]
                +
                videos_df["comment_count"]
            )
            /
            videos_df["view_count"]
        ).mean() * 100,
        2
    )

    return {

        "total_channels": total_channels,

        "total_subscribers": total_subscribers,

        "total_views": total_views,

        "total_videos": total_videos,

        "total_comments": total_comments,

        "total_likes": total_likes,

        "total_video_comments": total_video_comments,

        "positive_comments": positive_comments,

        "neutral_comments": neutral_comments,

        "negative_comments": negative_comments,

        "spam_comments": spam_comments,

        "abusive_comments": abusive_comments,

        "average_views": average_views,

        "average_likes": average_likes,

        "average_comments": average_comments,

        "average_words": average_words,

        "average_characters": average_characters,

        "average_engagement": average_engagement,

    }


def format_number(number: int) -> str:
    """
    Format numbers into K / M / B.
    """

    if number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}B"

    if number >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"

    if number >= 1_000:
        return f"{number / 1_000:.2f}K"

    return str(number)


def sentiment_percentage(
    comments_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Sentiment percentage.
    """

    sentiment = (
        comments_df["sentiment"]
        .value_counts(normalize=True)
        * 100
    ).round(2)

    return sentiment.reset_index().rename(
        columns={
            "index": "Sentiment",
            "sentiment": "Percentage",
        }
    )


def spam_percentage(
    comments_df: pd.DataFrame
) -> float:

    return round(
        comments_df["is_spam"].mean() * 100,
        2
    )


def abusive_percentage(
    comments_df: pd.DataFrame
) -> float:

    return round(
        comments_df[
            "contains_abusive_language"
        ].mean() * 100,
        2
    )