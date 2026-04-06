import streamlit as st
import plotly.express as px
from pages.common import run_query

st.title("Executive Control Tower")

kpi_query = """
SELECT
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN current_status = 'Delivered' THEN 1 ELSE 0 END) AS delivered_shipments,
    ROUND(100.0 * AVG(COALESCE(on_time_delivery_flag, 0)), 2) AS otd_pct,
    ROUND(100.0 * AVG(COALESCE(pickup_on_time_flag, 0)), 2) AS pickup_ontime_pct,
    SUM(CASE WHEN aging_hours > 72 AND current_status <> 'Delivered' THEN 1 ELSE 0 END) AS aging_over_72h,
    SUM(CASE WHEN exception_flag = 1 THEN 1 ELSE 0 END) AS total_exceptions
FROM shipment_master
"""

df_kpi = run_query(kpi_query)

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Shipments", f"{int(df_kpi.loc[0, 'total_shipments']):,}")
col2.metric("Delivered", f"{int(df_kpi.loc[0, 'delivered_shipments']):,}")
col3.metric("OTD %", f"{df_kpi.loc[0, 'otd_pct']}%")
col4.metric("Pickup On Time %", f"{df_kpi.loc[0, 'pickup_ontime_pct']}%")
col5.metric("Aging >72h", f"{int(df_kpi.loc[0, 'aging_over_72h']):,}")
col6.metric("Exceptions", f"{int(df_kpi.loc[0, 'total_exceptions']):,}")

trend_query = """
SELECT
    DATE(order_time) AS order_date,
    COUNT(*) AS shipments,
    ROUND(100.0 * AVG(COALESCE(on_time_delivery_flag, 0)), 2) AS otd_pct
FROM shipment_master
GROUP BY 1
ORDER BY 1
"""
df_trend = run_query(trend_query)

fig1 = px.line(df_trend, x="order_date", y="shipments", title="Daily Shipment Volume")
fig2 = px.line(df_trend, x="order_date", y="otd_pct", title="Daily OTD %")

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

station_query = """
SELECT
    origin_station,
    COUNT(*) AS shipments,
    ROUND(AVG(COALESCE(dwell_hub_hours, 0)), 2) AS avg_dwell_hub_hours,
    ROUND(100.0 * AVG(COALESCE(pickup_on_time_flag, 0)), 2) AS pickup_ontime_pct
FROM shipment_master
GROUP BY 1
ORDER BY shipments DESC
"""
df_station = run_query(station_query)

st.subheader("Origin Station Performance")
st.dataframe(df_station, use_container_width=True)
