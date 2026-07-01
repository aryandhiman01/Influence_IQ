import streamlit as st

from src.dashboard.loader import load_data
from src.dashboard.metrics import get_dashboard_metrics
from src.dashboard.sidebar import render_sidebar

from src.dashboard.pages.home import show_home
from src.dashboard.pages.videos import show_videos
from src.dashboard.pages.comments import show_comments
from src.dashboard.pages.nlp import show_nlp
from src.dashboard.pages.insights import show_insights


# =====================================================
# Page Config
# =====================================================

st.set_page_config(

    page_title="InfluenceIQ",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded"

)


# =====================================================
# Load Data
# =====================================================

channels_df, videos_df, comments_df = load_data()


# =====================================================
# Dashboard Metrics
# =====================================================

metrics = get_dashboard_metrics(

    channels_df,

    videos_df,

    comments_df

)


# =====================================================
# Sidebar
# =====================================================

filters = render_sidebar(

    channels_df,

    videos_df

)


# =====================================================
# Navigation
# =====================================================

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "🎥 Videos",

        "💬 Comments",

        "🧠 NLP",

        "📈 Insights"

    ]

)


# =====================================================
# Routing
# =====================================================

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