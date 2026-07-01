from dataclasses import dataclass

from src.recommendation.ranking import RankedInfluencer


# =====================================================
# Recommendation Result
# =====================================================

@dataclass
class RecommendationResult:

    recommendation: str

    stars: int

    brand_safety: str

    roi: str

    risk_level: str

    confidence: float

    summary: str


# =====================================================
# Business Rules
# =====================================================

class BusinessRules:

    """
    Business decision layer.

    Converts ranking scores into
    human-readable recommendations.
    """

    def __init__(

        self,

        influencer: RankedInfluencer

    ):

        self.data = influencer

    # =================================================

    def brand_safety(self):

        score = self.data.brand_safety_score

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "Good"

        elif score >= 60:

            return "Average"

        return "Poor"

    # =================================================

    def roi(self):

        score = self.data.roi_score

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "High"

        elif score >= 60:

            return "Moderate"

        return "Low"

    # =================================================

    def risk_level(self):

        safety = self.data.brand_safety_score

        influence = self.data.influence_score

        if safety >= 90 and influence >= 90:

            return "Very Low"

        elif safety >= 75:

            return "Low"

        elif safety >= 60:

            return "Medium"

        return "High"

    # =================================================

    def recommendation(self):

        score = self.data.influence_score

        if score >= 90:

            return (

                "Highly Recommended",

                5

            )

        elif score >= 80:

            return (

                "Recommended",

                4

            )

        elif score >= 70:

            return (

                "Good Choice",

                3

            )

        elif score >= 60:

            return (

                "Average Choice",

                2

            )

        return (

            "Avoid",

            1

        )

    # =================================================

    def confidence(self):

        confidence = (

            self.data.influence_score * 0.6

            +

            self.data.brand_safety_score * 0.2

            +

            self.data.roi_score * 0.2

        )

        return round(

            min(confidence, 100),

            2

        )

    # =================================================

    def summary(self):

        recommendation, _ = self.recommendation()

        return (

            f"{self.data.channel_name} has an "

            f"Influence Score of "

            f"{self.data.influence_score:.2f}. "

            f"Brand Safety is "

            f"{self.brand_safety()} "

            f"with "

            f"{self.roi()} ROI potential. "

            f"Final Recommendation: "

            f"{recommendation}."

        )

    # =================================================

    def evaluate(self):

        recommendation, stars = (

            self.recommendation()

        )

        return RecommendationResult(

            recommendation=recommendation,

            stars=stars,

            brand_safety=self.brand_safety(),

            roi=self.roi(),

            risk_level=self.risk_level(),

            confidence=self.confidence(),

            summary=self.summary()

        )