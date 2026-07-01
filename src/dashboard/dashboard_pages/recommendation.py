import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from src.recommendation.recommend import (
    RecommendationEngine
)


def show_recommendation(

    channels_df: pd.DataFrame,

    videos_df: pd.DataFrame,

    comments_df: pd.DataFrame

):

    st.title("🎯 AI Investment Advisor")

    st.caption(
        "AI-powered influencer recommendation system for brand collaborations."
    )

    st.divider()

    # =====================================================
    # Recommendation Engine
    # =====================================================

    engine = RecommendationEngine(

        channels_df,

        videos_df,

        comments_df

    )

    report = engine.as_dict()

    # =====================================================
    # KPI Cards
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "⭐ Influence Score",

        f"{report['Influence Score']:.2f}"

    )

    c2.metric(

        "🛡 Brand Safety",

        report["Brand Safety"]

    )

    c3.metric(

        "💰 ROI",

        report["ROI"]

    )

    c4.metric(

        "⚠ Risk",

        report["Risk"]

    )

    st.divider()

    # =====================================================
    # Recommendation Card
    # =====================================================

    st.subheader("🏆 Final Recommendation")

    stars = "⭐" * report["Stars"]

    st.success(

f"""
## {report['Recommendation']}

### {stars}

### Channel

**{report['Channel']}**

### Confidence

**{report['Confidence']}%**

"""
    )

    st.divider()

    # =====================================================
    # Recommendation Details
    # =====================================================

    left, right = st.columns([2,1])

    with left:

        st.subheader("📋 AI Recommendation")

        st.info(

f"""
### Recommendation

**{report['Recommendation']}**

### Brand Safety

**{report['Brand Safety']}**

### ROI Potential

**{report['ROI']}**

### Investment Risk

**{report['Risk']}**
"""
        )

    with right:

        st.subheader("📊 Overall Rating")

        st.metric(

            "Stars",

            stars

        )

        st.metric(

            "Rank",

            report["Rank"]

        )

    st.divider()

    # =====================================================
    # Gauge Chart
    # =====================================================

    st.subheader("🎯 Influence Score")

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=report["Influence Score"],

            title={

                "text":"Influence Score"

            },

            gauge={

                "axis":{

                    "range":[0,100]

                },

                "bar":{

                    "color":"green"

                },

                "steps":[

                    {

                        "range":[0,40],

                        "color":"#ff4d4d"

                    },

                    {

                        "range":[40,70],

                        "color":"#ffc107"

                    },

                    {

                        "range":[70,100],

                        "color":"#00cc66"

                    }

                ]

            }

        )

    )

    fig.update_layout(

        height=450

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

        # =====================================================
    # Radar Chart
    # =====================================================

    st.subheader("📊 Performance Radar")

    radar_labels = [

        "Influence",

        "Engagement",

        "Audience",

        "Popularity",

        "Brand Safety",

        "ROI"

    ]

    radar_values = [

        report["Influence Score"],

        report["Engagement Score"],

        report["Audience Score"],

        report["Popularity Score"],

        report["Brand Safety Score"],

        report["ROI Score"]

    ]

    radar_values.append(

        radar_values[0]

    )

    radar_labels.append(

        radar_labels[0]

    )

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=radar_values,

            theta=radar_labels,

            fill="toself",

            name=report["Channel"]

        )

    )

    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0,100]

            )

        ),

        height=600,

        showlegend=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Score Breakdown
    # =====================================================

    st.subheader("📈 Score Breakdown")

    score_df = pd.DataFrame(

        {

            "Metric":[

                "Influence",

                "Engagement",

                "Audience",

                "Popularity",

                "Brand Safety",

                "ROI"

            ],

            "Score":[

                report["Influence Score"],

                report["Engagement Score"],

                report["Audience Score"],

                report["Popularity Score"],

                report["Brand Safety Score"],

                report["ROI Score"]

            ]

        }

    )

    st.dataframe(

        score_df,

        use_container_width=True,

        hide_index=True

    )

    fig = go.Figure(

        go.Bar(

            x=score_df["Metric"],

            y=score_df["Score"],

            text=score_df["Score"],

            textposition="outside"

        )

    )

    fig.update_layout(

        title="Performance Score Comparison",

        yaxis=dict(

            range=[0,100]

        ),

        height=500

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =====================================================
    # Brand Safety
    # =====================================================

    st.subheader("🛡 Brand Safety Analysis")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(

            "Brand Safety",

            report["Brand Safety"]

        )

        st.metric(

            "Safety Score",

            f"{report['Brand Safety Score']:.2f}"

        )

    with c2:

        fig = go.Figure(

            go.Indicator(

                mode="number+gauge",

                value=report["Brand Safety Score"],

                gauge={

                    "axis":{

                        "range":[0,100]

                    }

                }

            )

        )

        fig.update_layout(

            height=350

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # ROI Analysis
    # =====================================================

    st.subheader("💰 ROI Analysis")

    left, right = st.columns(2)

    with left:

        st.metric(

            "ROI",

            report["ROI"]

        )

        st.metric(

            "ROI Score",

            f"{report['ROI Score']:.2f}"

        )

    with right:

        fig = go.Figure(

            go.Indicator(

                mode="number+gauge",

                value=report["ROI Score"],

                gauge={

                    "axis":{

                        "range":[0,100]

                    }

                }

            )

        )

        fig.update_layout(

            height=350

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.divider()

    # =====================================================
    # Risk Analysis
    # =====================================================

    st.subheader("⚠ Investment Risk")

    st.warning(

f"""
### Risk Level

**{report['Risk']}**

### Confidence

**{report['Confidence']}%**

The recommendation confidence is based on

- Influence Score

- Audience Quality

- Brand Safety

- ROI Potential

"""
    )

    st.divider()

        # =====================================================
    # Executive Recommendation Report
    # =====================================================

    st.subheader("📋 Executive Recommendation Report")

    report_df = pd.DataFrame({

        "Metric":[

            "Channel",

            "Rank",

            "Influence Score",

            "Engagement Score",

            "Audience Score",

            "Popularity Score",

            "Brand Safety Score",

            "ROI Score",

            "Recommendation",

            "Brand Safety",

            "ROI",

            "Risk",

            "Confidence"

        ],

        "Value":[

            report["Channel"],

            report["Rank"],

            report["Influence Score"],

            report["Engagement Score"],

            report["Audience Score"],

            report["Popularity Score"],

            report["Brand Safety Score"],

            report["ROI Score"],

            report["Recommendation"],

            report["Brand Safety"],

            report["ROI"],

            report["Risk"],

            f"{report['Confidence']} %"

        ]

    })

    report_df["Value"] = report_df["Value"].astype(str)

    st.dataframe(

        report_df,

        width="stretch",

        hide_index=True

    )

    st.divider()

    # =====================================================
    # AI Decision Summary
    # =====================================================

    st.subheader("🤖 AI Decision Summary")

    st.info(

        report["Summary"]

    )

    st.divider()

    # =====================================================
    # Why This Influencer?
    # =====================================================

    st.subheader("✅ Why This Influencer?")

    reasons = [

        "High Engagement Rate",

        "Strong Positive Audience Sentiment",

        "Excellent Brand Safety",

        "Low Spam Ratio",

        "Low Abusive Language",

        "High ROI Potential",

        "Consistent Video Performance",

        "Suitable for Long-Term Brand Collaboration"

    ]

    for reason in reasons:

        st.success(reason)

    st.divider()

    # =====================================================
    # Investment Decision
    # =====================================================

    st.subheader("💰 Investment Decision")

    if report["Influence Score"] >= 90:

        decision = "✅ YES"

        color = "success"

        message = """

### Recommended Investment

This influencer demonstrates:

- Excellent audience engagement

- Strong positive community

- Very high brand safety

- High ROI potential

Investment Recommendation:

## YES

"""

    elif report["Influence Score"] >= 75:

        decision = "🟡 CONSIDER"

        color = "warning"

        message = """

### Consider Investment

The influencer performs well overall.

Review campaign objectives before investing.

"""

    else:

        decision = "❌ NO"

        color = "error"

        message = """

### Not Recommended

Current performance metrics indicate

that investment risk is relatively high.

"""

    if color == "success":

        st.success(message)

    elif color == "warning":

        st.warning(message)

    else:

        st.error(message)

    st.metric(

        "Final Decision",

        decision

    )

    st.divider()

    # =====================================================
    # Download Report
    # =====================================================

    csv = report_df.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        label="⬇ Download Recommendation Report",

        data=csv,

        file_name="recommendation_report.csv",

        mime="text/csv"

    )

    st.divider()

    # =====================================================
    # Business Recommendations
    # =====================================================

    st.subheader("📈 Business Recommendations")

    recommendations = [

        "Collaborate with creators having an Influence Score above 85.",

        "Prioritize creators with Excellent Brand Safety.",

        "Avoid creators with high spam or abusive ratios.",

        "Use engagement rate instead of views alone for campaign planning.",

        "Monitor audience sentiment before launching campaigns.",

        "Track ROI after every collaboration.",

        "Re-evaluate influencer performance periodically.",

        "Build long-term partnerships with high-performing creators."

    ]

    for item in recommendations:

        st.markdown(f"• {item}")

    st.divider()

    # =====================================================
    # AI Investment Advisor Summary
    # =====================================================

    st.subheader("🎯 AI Investment Advisor")

    st.markdown(f"""

## Final Recommendation

### {report['Recommendation']}

⭐ **{'⭐' * report['Stars']}**

### Confidence

**{report['Confidence']} %**

### Brand Safety

**{report['Brand Safety']}**

### ROI

**{report['ROI']}**

### Investment Risk

**{report['Risk']}**

### Suggested Action

**{decision}**

""")

    st.divider()

    # =====================================================
    # Footer
    # =====================================================

    st.caption(

        "InfluenceIQ • AI Investment Advisor • Recommendation Engine"

    )