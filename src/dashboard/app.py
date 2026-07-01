import streamlit as st

from loader import load_data
from metrics import get_dashboard_metrics
from sidebar import render_sidebar
from styles import load_css

from dashboard_pages.home import show_home
from dashboard_pages.videos import show_videos
from dashboard_pages.comments import show_comments
from dashboard_pages.nlp import show_nlp
from dashboard_pages.insights import show_insights
from dashboard_pages.recommendation import show_recommendation


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="InfluenceIQ",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# LOAD CSS
# ==========================================================

load_css()

# ==========================================================
# LOAD DATABASE
# ==========================================================

channels_df, videos_df, comments_df = load_data()

# ==========================================================
# DASHBOARD METRICS
# ==========================================================

metrics = get_dashboard_metrics(

    channels_df,

    videos_df,

    comments_df

)

# ==========================================================
# SIDEBAR
# ==========================================================

filters = render_sidebar(

    channels_df,

    videos_df

)

# ==========================================================
# NAVIGATION
# ==========================================================

st.sidebar.markdown("---")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "🎥 Videos",

        "💬 Comments",

        "🧠 NLP",

        "📈 Insights",

        "🎯 Recommendation"

    ]

)

st.sidebar.markdown("---")

st.sidebar.caption(

    "InfluenceIQ v1.0"

)

# ==========================================================
# ROUTING
# ==========================================================

if page == "🏠 Home":

    show_home(

        channels_df,

        videos_df,

        comments_df,

        metrics,

        filters

    )

elif page == "🎥 Videos":

    show_videos(

        videos_df,

        filters

    )

elif page == "💬 Comments":

    show_comments(

        comments_df,

        filters

    )

elif page == "🧠 NLP":

    show_nlp(

        comments_df,

        filters

    )

elif page == "📈 Insights":

    show_insights(

        videos_df,

        comments_df

    )

elif page == "🎯 Recommendation":

    show_recommendation(

        channels_df,

        videos_df,

        comments_df

    )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(

    """
<div style="text-align:center;padding:20px">

<h4>🚀 InfluenceIQ</h4>

<p>
YouTube Analytics & NLP Dashboard
</p>

<p>
Built using
<strong>
Streamlit
</strong>,
<strong>
PostgreSQL
</strong>,
<strong>
SQLAlchemy
</strong>,
<strong>
Pandas
</strong>,
<strong>
Plotly
</strong>
</p>

</div>
""",

    unsafe_allow_html=True

)