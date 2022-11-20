import streamlit as st
# import pandas as pd
import gspread
# from google.oauth2 import service_account

# credentials = service_account.Credentials.from_service_account_info(
#     st.secrets["gcp_service_account"],
#     scopes=["https://www.googleapis.com/auth/spreadsheets",],
# )
# gc = gspread.authorize(credentials)
# sh_url = st.secrets["private_gsheets_url"]
# sh = gc.open_by_url(sh_url)
# ws_name = "Sheet1"
# ws = sh.worksheet(ws_name)
# a1 = ws.acell("A1").value
st.markdown(f"# BIMO BI Demo.")
st.markdown(f"{dir(gspread)}")
