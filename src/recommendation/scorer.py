from dataclasses import dataclass

from src.recommendation.metrics import ChannelMetrics


@dataclass
class ScoreReport:

    influence_score: float

    engagement_score: float

    audience_score: float

    popularity_score: float

    brand_safety_score: float

    roi_score: float


class InfluenceScorer:

    """
    Calculates all recommendation scores
    using extracted metrics.
    """

    def __init__(

        self,

        metrics: ChannelMetrics

    ):

        self.metrics = metrics

    # =====================================================
    # Utility
    # =====================================================

    @staticmethod
    def clamp(

        value: float,

        minimum: float = 0,

        maximum: float = 100

    ) -> float:

        return max(

            minimum,

            min(value, maximum)

        )

    # =====================================================
    # Engagement Score
    # =====================================================

    def engagement_score(self):

        score = self.metrics.engagement_rate * 10

        return round(

            self.clamp(score),

            2

        )

    # =====================================================
    # Audience Score
    # =====================================================

    def audience_score(self):

        score = (

            self.metrics.positive_ratio

            -

            self.metrics.negative_ratio

            -

            (self.metrics.spam_ratio * 0.5)

            -

            (self.metrics.abusive_ratio * 0.5)

        )

        return round(

            self.clamp(score),

            2

        )

    # =====================================================
    # Popularity Score
    # =====================================================

    def popularity_score(self):

        subscriber_score = min(

            (

                self.metrics.subscribers

                /

                10_000_000

            ) * 100,

            100

        )

        views_score = min(

            (

                self.metrics.total_views

                /

                100_000_000

            ) * 100,

            100

        )

        popularity = (

            subscriber_score * 0.6

            +

            views_score * 0.4

        )

        return round(

            self.clamp(popularity),

            2

        )

    # =====================================================
    # Brand Safety
    # =====================================================

    def brand_safety_score(self):

        penalty = (

            self.metrics.spam_ratio * 2

            +

            self.metrics.abusive_ratio * 3

        )

        safety = 100 - penalty

        return round(

            self.clamp(safety),

            2

        )

    # =====================================================
    # ROI Score
    # =====================================================

    def roi_score(self):

        roi = (

            self.engagement_score() * 0.50

            +

            self.audience_score() * 0.30

            +

            self.popularity_score() * 0.20

        )

        return round(

            self.clamp(roi),

            2

        )

    # =====================================================
    # Final Influence Score
    # =====================================================

    def influence_score(self):

        score = (

            self.engagement_score() * 0.35

            +

            self.audience_score() * 0.25

            +

            self.popularity_score() * 0.20

            +

            self.brand_safety_score() * 0.20

        )

        return round(

            self.clamp(score),

            2

        )

    # =====================================================
    # Report
    # =====================================================

    def calculate(self):

        return ScoreReport(

            influence_score=self.influence_score(),

            engagement_score=self.engagement_score(),

            audience_score=self.audience_score(),

            popularity_score=self.popularity_score(),

            brand_safety_score=self.brand_safety_score(),

            roi_score=self.roi_score()

        )