import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Seed Database", layout="wide")
st.title("Seed Dummy Data to Neon")

def get_engine():
    db_url = st.secrets["DB_URL"]
    return create_engine(db_url, pool_pre_ping=True)

st.write("Gunakan halaman ini sekali saja untuk upload dummy CSV dari repo GitHub ke Neon.")

if st.button("Upload Dummy Data to Neon"):
    try:
        engine = get_engine()

        st.info("Reading CSV files from repo...")
        df_master = pd.read_csv(
            "data/shipment_master_dummy.csv",
            parse_dates=[
                "order_time", "pickup_requested_time", "courier_assigned_time",
                "pickup_actual_time", "first_scan_time",
                "arrived_origin_station_time", "departed_origin_station_time",
                "arrived_hub_time", "departed_hub_time",
                "out_for_delivery_time", "delivered_time", "promised_delivery_time"
            ]
        )

        df_event = pd.read_csv(
            "data/shipment_event_log_dummy.csv",
            parse_dates=["event_time"]
        )

        st.info("Uploading shipment_master...")
        df_master.to_sql(
            "shipment_master",
            engine,
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=1000
        )

        st.info("Uploading shipment_event_log...")
        df_event.to_sql(
            "shipment_event_log",
            engine,
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=2000
        )

        st.success("Dummy data successfully uploaded to Neon.")

        with engine.connect() as conn:
            count_master = pd.read_sql("SELECT COUNT(*) AS cnt FROM shipment_master", conn)
            count_event = pd.read_sql("SELECT COUNT(*) AS cnt FROM shipment_event_log", conn)

        st.write("shipment_master rows:", int(count_master.iloc[0]["cnt"]))
        st.write("shipment_event_log rows:", int(count_event.iloc[0]["cnt"]))

    except Exception as e:
        st.error(f"Upload failed: {e}")
        raise
