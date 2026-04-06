import streamlit as st
import plotly.express as px
from pages.common import run_query

st.title("First Mile SLA")

query = """
SELECT
    origin_station,
    COUNT(*) AS total_shipments,
    ROUND(100.0 * AVG(COALESCE(pickup_on_time_flag, 0)), 2) AS pickup_ontime_pct,
    ROUND(AVG(COALESCE(first_scan_timeliness_min, 0)), 2) AS avg_first_scan_min,
    ROUND(100.0 * AVG(COALESCE(failed_pickup_flag, 0)), 2) AS failed_pickup_pct
FROM shipment_master
GROUP BY 1
ORDER BY pickup_ontime_pct ASC
"""
df = run_query(query)

fig = px.bar(
    df,
    x="origin_station",
    y="pickup_ontime_pct",
    title="Pickup On-Time % by Origin Station"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("First Mile Summary")
st.dataframe(df, use_container_width=True)

reason_query = """
SELECT
    failed_pickup_reason,
    COUNT(*) AS total_cases
FROM shipment_master
WHERE failed_pickup_flag = 1
GROUP BY 1
ORDER BY total_cases DESC
"""
df_reason = run_query(reason_query)

fig2 = px.bar(df_reason, x="failed_pickup_reason", y="total_cases", title="Failed Pickup Reasons")
st.plotly_chart(fig2, use_container_width=True)
