from dataclasses import dataclass

from src.recommendation.metrics import ChannelMetrics
from src.recommendation.scorer import (
    InfluenceScorer,
    ScoreReport
)


# =====================================================
# Ranked Influencer
# =====================================================

@dataclass
class RankedInfluencer:

    rank: int

    channel_name: str

    influence_score: float

    engagement_score: float

    audience_score: float

    popularity_score: float

    brand_safety_score: float

    roi_score: float

    subscribers: int

    total_views: int

    total_videos: int


# =====================================================
# Ranking Engine
# =====================================================

class RankingEngine:

    """
    Rank one or multiple influencers
    based on Influence Score.
    """

    def __init__(

        self,

        metrics_list: list[ChannelMetrics]

    ):

        self.metrics_list = metrics_list

    # =================================================

    def generate_ranking(

        self

    ) -> list[RankedInfluencer]:

        ranking = []

        # -----------------------------

        for metrics in self.metrics_list:

            report: ScoreReport = (

                InfluenceScorer(

                    metrics

                ).calculate()

            )

            ranking.append(

                {

                    "channel_name":

                        metrics.channel_name,

                    "metrics":

                        metrics,

                    "report":

                        report

                }

            )

        # -----------------------------

        ranking.sort(

            key=lambda x:

            x["report"].influence_score,

            reverse=True

        )

        # -----------------------------

        ranked = []

        for index, item in enumerate(

            ranking,

            start=1

        ):

            report = item["report"]

            metrics = item["metrics"]

            ranked.append(

                RankedInfluencer(

                    rank=index,

                    channel_name=

                        metrics.channel_name,

                    influence_score=

                        report.influence_score,

                    engagement_score=

                        report.engagement_score,

                    audience_score=

                        report.audience_score,

                    popularity_score=

                        report.popularity_score,

                    brand_safety_score=

                        report.brand_safety_score,

                    roi_score=

                        report.roi_score,

                    subscribers=

                        metrics.subscribers,

                    total_views=

                        metrics.total_views,

                    total_videos=

                        metrics.total_videos

                )

            )

        return ranked

    # =================================================

    def best_influencer(

        self

    ) -> RankedInfluencer | None:

        ranking = self.generate_ranking()

        if not ranking:

            return None

        return ranking[0]

    # =================================================

    def as_dataframe(self):

        import pandas as pd

        ranking = self.generate_ranking()

        return pd.DataFrame(

            [

                {

                    "Rank":

                        item.rank,

                    "Channel":

                        item.channel_name,

                    "Influence Score":

                        item.influence_score,

                    "ROI Score":

                        item.roi_score,

                    "Brand Safety":

                        item.brand_safety_score,

                    "Subscribers":

                        item.subscribers,

                    "Views":

                        item.total_views,

                    "Videos":

                        item.total_videos

                }

                for item in ranking

            ]

        )