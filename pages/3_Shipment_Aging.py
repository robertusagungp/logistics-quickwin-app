import streamlit as st
import plotly.express as px
from pages.common import run_query

st.title("Shipment Aging & Dwell Time")

aging_query = """
SELECT
    CASE
        WHEN aging_hours <= 24 THEN '0-24h'
        WHEN aging_hours <= 48 THEN '24-48h'
        WHEN aging_hours <= 72 THEN '48-72h'
        ELSE '>72h'
    END AS aging_bucket,
    COUNT(*) AS total_shipments
FROM shipment_master
WHERE current_status <> 'Delivered'
GROUP BY 1
ORDER BY 1
"""
df_aging = run_query(aging_query)

fig = px.bar(df_aging, x="aging_bucket", y="total_shipments", title="Open Shipment Aging Buckets")
st.plotly_chart(fig, use_container_width=True)

dwell_query = """
SELECT
    origin_hub,
    ROUND(AVG(COALESCE(dwell_hub_hours, 0)), 2) AS avg_dwell_hub_hours,
    COUNT(*) AS shipments
FROM shipment_master
GROUP BY 1
ORDER BY avg_dwell_hub_hours DESC
"""
df_dwell = run_query(dwell_query)

fig2 = px.bar(df_dwell, x="origin_hub", y="avg_dwell_hub_hours", title="Average Dwell Hub Hours")
st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df_dwell, use_container_width=True)
