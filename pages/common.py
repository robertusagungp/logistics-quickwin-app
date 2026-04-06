import pandas as pd
import streamlit as st
from sqlalchemy import text
from scripts.db_utils import get_engine

@st.cache_data(ttl=300)
def run_query(query: str) -> pd.DataFrame:
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)
