import streamlit as st

MATOMO_TOKEN_AUTH = st.secrets["MATOMO_TOKEN_AUTH"]
MATOMO_API_URL = st.secrets["MATOMO_API_URL"]

MATOMO_SITES_IDS = {
    "openaerialmap.org": st.secrets.MATOMO_SITE_IDS.openaerialmap_org,
    "tasks.hotosm.org": st.secrets.MATOMO_SITE_IDS.tasks_hotosm_org,
    "export.hotosm.org": st.secrets.MATOMO_SITE_IDS.export_hotosm_org,
    "chatmap.hotosm.org": st.secrets.MATOMO_SITE_IDS.chatmap_hotosm_org,
    "umap.hotosm.org": st.secrets.MATOMO_SITE_IDS.umap_hotosm_org,
    "dronetm.org": st.secrets.MATOMO_SITE_IDS.dronetm_org,
    "fair.hotosm.org": st.secrets.MATOMO_SITE_IDS.fair_hotosm_org,
    "fmtm.hotosm.org": st.secrets.MATOMO_SITE_IDS.fmtm_hotosm_org,
}

SITES_LIST = [
    {
        "Project Id (from finance)": "",
        "Title": "Open Aerial Map",
        "URL": "openaerialmap.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "Tasking Manager",
        "URL": "tasks.hotosm.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "Export Tool",
        "URL": "export.hotosm.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "Drone Tasking Manager",
        "URL": "dronetm.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "fAIr",
        "URL": "fair.hotosm.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "Field Mapping Tasking Manager",
        "URL": "fmtm.hotosm.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "ChatMap",
        "URL": "chatmap.hotosm.org"
    },
    {
        "Project Id (from finance)": "",
        "Title": "uMap",
        "URL": "umap.hotosm.org"
    },
]


