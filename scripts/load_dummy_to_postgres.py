import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")

MASTER_CSV = "data/shipment_master_dummy.csv"
EVENT_CSV = "data/shipment_event_log_dummy.csv"
CREATE_SQL = "sql/001_create_tables.sql"
INDEX_SQL = "sql/002_indexes.sql"

def main():
    if not DB_URL:
        raise ValueError("DB_URL tidak ditemukan di environment variable")

    engine = create_engine(DB_URL, pool_pre_ping=True)

    print("Reading CSV...")
    df_master = pd.read_csv(MASTER_CSV, parse_dates=[
        "order_time", "pickup_requested_time", "courier_assigned_time",
        "pickup_actual_time", "first_scan_time",
        "arrived_origin_station_time", "departed_origin_station_time",
        "arrived_hub_time", "departed_hub_time",
        "out_for_delivery_time", "delivered_time", "promised_delivery_time"
    ])

    df_event = pd.read_csv(EVENT_CSV, parse_dates=["event_time"])

    print("Creating tables...")
    with engine.begin() as conn:
        with open(CREATE_SQL, "r", encoding="utf-8") as f:
            conn.execute(text(f.read()))
        with open(INDEX_SQL, "r", encoding="utf-8") as f:
            conn.execute(text(f.read()))

    print("Loading shipment_master...")
    df_master.to_sql(
        "shipment_master",
        engine,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=1000
    )

    print("Loading shipment_event_log...")
    df_event.to_sql(
        "shipment_event_log",
        engine,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=2000
    )

    print("Recreating indexes after replace...")
    with engine.begin() as conn:
        with open(INDEX_SQL, "r", encoding="utf-8") as f:
            conn.execute(text(f.read()))

    print("Done.")

if __name__ == "__main__":
    main()
