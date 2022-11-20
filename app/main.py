import streamlit as st  # loaded by streamlit cloud
import pandas as pd  # loaded by streamlit cloud
import gspread
from google.oauth2 import service_account  # module name is google-auth
import altair as alt  # loaded by streamlit cloud

# credentials not saved to Github. Saved in settings in streamlit cloud
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/spreadsheets", ],
)
gc = gspread.authorize(credentials)
sh_url = st.secrets["private_gsheets_url"]
sh = gc.open_by_url(sh_url)
ws_name = "Sheet1"
ws = sh.worksheet(ws_name)
df = pd.DataFrame(ws.get_all_records())

st.markdown(f"# Episode of Care Count")
st.markdown(f"## By Length of Stay")
_df = df.groupby("length_of_stay", as_index=False).agg({"episode_id": "count", "satisfaction_rating": "mean"})
_base = alt.Chart(_df).encode(
    alt.X("length_of_stay",
          axis=alt.Axis(title="Length of Stay"))
)
_bar = _base.mark_bar(color='#4c78a8').encode(
    alt.Y("episode_id",
          axis=alt.Axis(title="Episode Count", titleColor="#4c78a8"))
)
_line = _base.mark_line(color='#F18727').encode(
    alt.Y("satisfaction_rating",
          axis=alt.Axis(title="Average Satisfaction Rating", titleColor="#F18727"))
)
_chart = alt.layer(_bar, _line).resolve_scale(y="independent")
st.altair_chart(_chart, use_container_width=True)

st.markdown(f"## By Comorbidity Count")
_df = df.groupby("comorbidity_count", as_index=False).agg({"episode_id": "count", "satisfaction_rating": "mean"})
_base = alt.Chart(_df).encode(
    alt.X("comorbidity_count",
          axis=alt.Axis(title="Comorbidity Count"))
)
_bar = _base.mark_bar(color='#4c78a8').encode(
    alt.Y("episode_id",
          axis=alt.Axis(title="Episode Count", titleColor="#4c78a8"))
)
_line = _base.mark_line(color='#F18727').encode(
    alt.Y("satisfaction_rating",
          axis=alt.Axis(title="Average Satisfaction Rating", titleColor="#F18727"))
)
_chart = alt.layer(_bar, _line).resolve_scale(y="independent")
st.altair_chart(_chart, use_container_width=True)

st.markdown(f"## By Age")
_df = df.groupby("age", as_index=False).agg({"episode_id": "count", "satisfaction_rating": "mean"})
_base = alt.Chart(_df).encode(
    alt.X("age",
          axis=alt.Axis(title="Age"))
)
_bar = _base.mark_bar(color='#4c78a8').encode(
    alt.Y("episode_id",
          axis=alt.Axis(title="Episode Count", titleColor="#4c78a8"))
)
_line = _base.mark_line(color='#F18727').encode(
    alt.Y("satisfaction_rating",
          axis=alt.Axis(title="Average Satisfaction Rating", titleColor="#F18727"))
)
_chart = alt.layer(_bar, _line).resolve_scale(y="independent")
st.altair_chart(_chart, use_container_width=True)

st.markdown(f"## By Gender")
_df = df.groupby("gender", as_index=False).agg({"episode_id": "count", "satisfaction_rating": "mean"})
_base = alt.Chart(_df).encode(
    alt.X("gender",
          axis=alt.Axis(title="Gender"))
)
_bar = _base.mark_bar(color='#4c78a8').encode(
    alt.Y("episode_id",
          axis=alt.Axis(title="Episode Count", titleColor="#4c78a8"))
)
_line = _base.mark_line(color='#F18727').encode(
    alt.Y("satisfaction_rating",
          axis=alt.Axis(title="Average Satisfaction Rating", titleColor="#F18727"))
)
_chart = alt.layer(_bar, _line).resolve_scale(y="independent")
st.altair_chart(_chart, use_container_width=True)
