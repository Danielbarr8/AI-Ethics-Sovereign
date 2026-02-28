import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import datetime

st.set_page_config(page_title="AI Ethics Sovereign", layout="wide", page_icon="⚖️")

# High-Stakes Professional Styling
st.markdown("""<style> .stApp { background-color: #000000; color: #d4af37; } </style>""", unsafe_allow_code=True)

st.title("⚖️ AI Ethics Sovereign")
st.subheader("Autonomous Governance & Veto Engine")

# The Veto Simulation
st.write("### 🧠 Live Decision Engine")
input_text = st.text_area("Simulated AI Output to Audit:", placeholder="Enter the AI's response here...")

if input_text:
    # Logic: Checking for specific ethical failures
    is_biased = any(word in input_text.lower() for word in ["unfair", "stereotypical", "biased"])
    is_unsafe = any(word in input_text.lower() for word in ["harm", "illegal", "exploit"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Sovereign Assessment**")
        score = 100
        if is_biased: score -= 40
        if is_unsafe: score -= 60
        
        st.metric("Ethics Alignment Score", f"{score}%", delta="-40%" if score < 100 else "Stable")
        
    with col2:
        st.write("**Veto Status**")
        if score < 70:
            st.error("🚫 VETO ACTIVE: Response Blocked")
            st.write("Reason: High Probability of Regulatory Non-Compliance.")
        else:
            st.success("✅ CLEARED: Response Released")

# Data Visualization of Compliance
st.divider()
st.write("### 📈 Cumulative Governance Metrics")
df = pd.DataFrame({
    "Category": ["Bias", "Safety", "Hallucination", "PII"],
    "Risk Level": [15, 5, 25, 2]
})
fig = px.pie(df, values='Risk Level', names='Category', title='System-Wide Risk Distribution', template="plotly_dark")
st.plotly_chart(fig)

# Audit Report
if st.button("Generate Official Sovereign Audit"):
    pdf = FPDF()
    pdf.add_page(); pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="OFFICIAL AI ETHICS SOVEREIGN REPORT", ln=True, align='C')
    pdf.set_font("Arial", size=12); pdf.ln(10)
    pdf.cell(200, 10, txt=f"Timestamp: {datetime.datetime.now()}", ln=True)
    pdf.cell(200, 10, txt=f"Compliance Mode: 2026 EU AI Act", ln=True)
    report = pdf.output(dest='S').encode('latin-1')
    st.download_button("Download Report", data=report, file_name="Sovereign_Audit.pdf")

st.caption("AI Ethics Sovereign | Project by Daniel Barr | 2026")