import streamlit as st
import plotly.express as px
from pages.common import run_query

st.title("Exception & Risk Monitoring")

query = """
SELECT
    exception_type,
    COUNT(*) AS total_cases
FROM shipment_master
WHERE exception_flag = 1
GROUP BY 1
ORDER BY total_cases DESC
"""
df = run_query(query)

fig = px.bar(df, x="exception_type", y="total_cases", title="Exception Breakdown")
st.plotly_chart(fig, use_container_width=True)

risk_query = """
SELECT
    origin_station,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN exception_flag = 1 THEN 1 ELSE 0 END) AS exception_shipments,
    ROUND(100.0 * AVG(COALESCE(exception_flag, 0)), 2) AS exception_rate_pct
FROM shipment_master
GROUP BY 1
ORDER BY exception_rate_pct DESC
"""
df_risk = run_query(risk_query)

st.subheader("Station Risk Ranking")
st.dataframe(df_risk, use_container_width=True)

cost_query = """
SELECT
    exception_type,
    SUM(estimated_cost_idr) AS total_estimated_cost_idr
FROM shipment_master
WHERE exception_flag = 1
GROUP BY 1
ORDER BY total_estimated_cost_idr DESC
"""
df_cost = run_query(cost_query)

fig2 = px.bar(df_cost, x="exception_type", y="total_estimated_cost_idr", title="Estimated Cost Exposure by Exception")
st.plotly_chart(fig2, use_container_width=True)
