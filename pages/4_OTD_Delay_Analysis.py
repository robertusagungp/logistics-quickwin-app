import streamlit as st
import plotly.express as px
from pages.common import run_query

st.title("OTD & Delay Analysis")

query = """
SELECT
    destination_region,
    service_type,
    COUNT(*) AS total_shipments,
    ROUND(100.0 * AVG(COALESCE(on_time_delivery_flag, 0)), 2) AS otd_pct
FROM shipment_master
GROUP BY 1,2
ORDER BY 1,2
"""
df = run_query(query)

fig = px.bar(
    df,
    x="destination_region",
    y="otd_pct",
    color="service_type",
    barmode="group",
    title="OTD % by Destination Region and Service Type"
)
st.plotly_chart(fig, use_container_width=True)

delay_query = """
SELECT
    late_reason_bucket,
    COUNT(*) AS total_shipments
FROM shipment_master
WHERE late_reason_bucket IS NOT NULL
  AND late_reason_bucket <> ''
GROUP BY 1
ORDER BY total_shipments DESC
"""
df_delay = run_query(delay_query)

fig2 = px.pie(df_delay, names="late_reason_bucket", values="total_shipments", title="Delay Root Cause Mix")
st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df_delay, use_container_width=True)
