import streamlit as st  # loaded by streamlit cloud
import pandas as pd  # loaded by streamlit cloud
import gspread
from google.oauth2 import service_account  # module name is google-auth
import altair as alt

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
_df = df.groupby("length_of_stay", as_index=False).agg({"episode_id": "count"})
st.bar_chart(
    _df,
    x="length_of_stay",
    y="episode_id",
)
st.markdown(f"## By Age")
_df = df.groupby("age", as_index=False).agg({"episode_id": "count"})
st.bar_chart(
    _df,
    x="age",
    y="episode_id",
)
st.markdown(f"## By Age (Altair)")
_df = df.groupby("age", as_index=False).agg({"episode_id": "count"})
_chart = alt.Chart(_df).mark_bar().encode(
    x="age",
    y="episode_id",
)
st.altair_chart(_chart)

