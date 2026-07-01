from dataclasses import dataclass
import pandas as pd


@dataclass
class ChannelMetrics:
    """
    Stores all raw metrics required by the Recommendation Engine.
    """

    channel_name: str

    subscribers: int

    total_views: int

    total_videos: int

    total_video_comments: int

    total_likes: int

    total_comment_records: int

    positive_comments: int

    neutral_comments: int

    negative_comments: int

    spam_comments: int

    abusive_comments: int

    engagement_rate: float

    positive_ratio: float

    neutral_ratio: float

    negative_ratio: float

    spam_ratio: float

    abusive_ratio: float

    average_views: float

    average_likes: float

    average_comments: float

    average_word_count: float

    average_character_count: float


class MetricsExtractor:

    def __init__(

        self,

        channels_df: pd.DataFrame,

        videos_df: pd.DataFrame,

        comments_df: pd.DataFrame

    ):

        self.channels = channels_df

        self.videos = videos_df

        self.comments = comments_df

    # =====================================================
    # Extract Metrics
    # =====================================================

    def extract(self) -> ChannelMetrics:

        channel_name = self.channels.iloc[0]["channel_name"]

        subscribers = int(

            self.channels["subscriber_count"].sum()

        )

        total_views = int(

            self.videos["view_count"].sum()

        )

        total_likes = int(

            self.videos["like_count"].sum()

        )

        total_video_comments = int(

            self.videos["comment_count"].sum()

        )

        total_videos = len(

            self.videos

        )

        total_comment_records = len(

            self.comments

        )

        positive = (

            self.comments["sentiment"]

            ==

            "Positive"

        ).sum()

        neutral = (

            self.comments["sentiment"]

            ==

            "Neutral"

        ).sum()

        negative = (

            self.comments["sentiment"]

            ==

            "Negative"

        ).sum()

        spam = int(

            self.comments["is_spam"].sum()

        )

        abusive = int(

            self.comments["contains_abusive_language"].sum()

        )

        # -------------------------------------------------

        engagement_rate = 0

        if total_views > 0:

            engagement_rate = (

                (

                    total_likes

                    +

                    total_video_comments

                )

                /

                total_views

            ) * 100

        # -------------------------------------------------

        def ratio(value):

            if total_comment_records == 0:

                return 0

            return round(

                (

                    value

                    /

                    total_comment_records

                ) * 100,

                2

            )

        return ChannelMetrics(

            channel_name=channel_name,

            subscribers=subscribers,

            total_views=total_views,

            total_videos=total_videos,

            total_video_comments=total_video_comments,

            total_likes=total_likes,

            total_comment_records=total_comment_records,

            positive_comments=int(positive),

            neutral_comments=int(neutral),

            negative_comments=int(negative),

            spam_comments=spam,

            abusive_comments=abusive,

            engagement_rate=round(

                engagement_rate,

                2

            ),

            positive_ratio=ratio(

                positive

            ),

            neutral_ratio=ratio(

                neutral

            ),

            negative_ratio=ratio(

                negative

            ),

            spam_ratio=ratio(

                spam

            ),

            abusive_ratio=ratio(

                abusive

            ),

            average_views=round(

                self.videos["view_count"].mean(),

                2

            ),

            average_likes=round(

                self.videos["like_count"].mean(),

                2

            ),

            average_comments=round(

                self.videos["comment_count"].mean(),

                2

            ),

            average_word_count=round(

                self.comments["word_count"].mean(),

                2

            ),

            average_character_count=round(

                self.comments["character_count"].mean(),

                2

            )

        )