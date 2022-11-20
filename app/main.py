import streamlit as st  # loaded by streamlit cloud
import pandas as pd  # loaded by streamlit cloud
import gspread
from google.oauth2 import service_account  # module name is google-auth

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

st.markdown(f"# Episode of Care Count by Length of Stay")
_df = df.groupby("length_of_stay", as_index=False).agg({"episode_id": "count"})
st.bar_chart(
    _df,
    x="length_of_stay",
    y="episode_id",
)