from __future__ import annotations

import streamlit as st

from agent import AIBusinessProposalAgent, ProposalInput


st.set_page_config(page_title="AI Business Proposal Agent", page_icon="📈", layout="wide")
st.title("AI Business Proposal Agent")
st.caption("Enter company name, industry, and goal to generate a research-backed proposal.")

with st.form("proposal_form"):
    company_name = st.text_input("Company Name", placeholder="Example: Acme Logistics")
    industry = st.text_input("Industry", placeholder="Example: Supply Chain / Logistics Tech")
    goal = st.text_area(
        "Goal",
        placeholder="Example: Increase B2B lead generation by 30% in 6 months",
        height=120,
    )
    submitted = st.form_submit_button("Generate Proposal")

if submitted:
    if not company_name.strip() or not industry.strip() or not goal.strip():
        st.error("Please fill in company name, industry, and goal.")
    else:
        with st.spinner("Researching and writing proposal..."):
            try:
                agent = AIBusinessProposalAgent()
                result = agent.generate_proposal(
                    ProposalInput(
                        company_name=company_name.strip(),
                        industry=industry.strip(),
                        goal=goal.strip(),
                    )
                )
            except Exception as exc:
                st.exception(exc)
            else:
                st.success("Proposal generated.")
                st.markdown(result)
