from dataclasses import dataclass

from src.recommendation.metrics import (
    MetricsExtractor
)

from src.recommendation.scorer import (
    InfluenceScorer
)

from src.recommendation.ranking import (
    RankingEngine,
    RankedInfluencer
)

from src.recommendation.business_rules import (
    BusinessRules,
    RecommendationResult
)


# =====================================================
# Final Report
# =====================================================

@dataclass
class RecommendationReport:

    influencer: RankedInfluencer

    recommendation: RecommendationResult


# =====================================================
# Recommendation Engine
# =====================================================

class RecommendationEngine:

    """
    Final Recommendation Engine

    Responsibilities
    ----------------
    ✔ Extract Metrics
    ✔ Calculate Scores
    ✔ Rank Influencer
    ✔ Apply Business Rules
    ✔ Generate Final Report
    """

    def __init__(

        self,

        channels_df,

        videos_df,

        comments_df

    ):

        self.channels_df = channels_df

        self.videos_df = videos_df

        self.comments_df = comments_df

    # =================================================

    def build(self):

        metrics = MetricsExtractor(

            self.channels_df,

            self.videos_df,

            self.comments_df

        ).extract()

        ranking = RankingEngine(

            [

                metrics

            ]

        )

        best = ranking.best_influencer()

        recommendation = BusinessRules(

            best

        ).evaluate()

        return RecommendationReport(

            influencer=best,

            recommendation=recommendation

        )

    # =================================================

    def as_dict(self):

        report = self.build()

        influencer = report.influencer

        recommendation = report.recommendation

        return {

            "Channel":

                influencer.channel_name,

            "Rank":

                influencer.rank,

            "Influence Score":

                influencer.influence_score,

            "Engagement Score":

                influencer.engagement_score,

            "Audience Score":

                influencer.audience_score,

            "Popularity Score":

                influencer.popularity_score,

            "Brand Safety Score":

                influencer.brand_safety_score,

            "ROI Score":

                influencer.roi_score,

            "Subscribers":

                influencer.subscribers,

            "Views":

                influencer.total_views,

            "Videos":

                influencer.total_videos,

            "Recommendation":

                recommendation.recommendation,

            "Stars":

                recommendation.stars,

            "Brand Safety":

                recommendation.brand_safety,

            "ROI":

                recommendation.roi,

            "Risk":

                recommendation.risk_level,

            "Confidence":

                recommendation.confidence,

            "Summary":

                recommendation.summary

        }

    # =================================================

    def print_report(self):

        report = self.as_dict()

        print()

        print("=" * 60)

        print("        INFLUENCER RECOMMENDATION REPORT")

        print("=" * 60)

        print()

        for key, value in report.items():

            print(f"{key:<22}: {value}")

        print()

        print("=" * 60)