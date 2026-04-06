from sqlalchemy import create_engine
import streamlit as st

def get_engine():
    db_url = st.secrets["DB_URL"]
    return create_engine(db_url, pool_pre_ping=True)
