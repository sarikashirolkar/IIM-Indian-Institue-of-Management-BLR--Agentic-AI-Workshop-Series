from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from openai import OpenAI


@dataclass
class ProposalInput:
    company_name: str
    industry: str
    goal: str


class AIBusinessProposalAgent:
    """Generates a research-backed business proposal using only OpenAI's API."""

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing. Set it in your environment.")

        # Default to a faster, lower-cost model. Can be overridden via OPENAI_MODEL.
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
        self.client = OpenAI(api_key=self.api_key)

    def generate_proposal(self, payload: ProposalInput) -> str:
        instructions = (
            "You are an AI business proposal analyst. "
            "Create a practical, specific proposal with real-world reasoning. "
            "When exact recent data is unavailable, clearly state assumptions "
            "and use conservative estimates."
        )

        prompt = f"""
Company Name: {payload.company_name}
Industry: {payload.industry}
Primary Goal: {payload.goal}

Return a complete proposal in markdown with these sections:
1) Executive Summary
2) Company + Industry Snapshot
3) Market Research and Trends
4) Competitor Landscape
5) Opportunity Gaps for this company
6) Strategic Plan (90-day, 6-month, 12-month)
7) Budget Ranges and ROI assumptions
8) Risks and Mitigations
9) KPI Dashboard (what to measure weekly/monthly)
10) Actionable Next Steps (first 14 days)

Rules:
- Be concrete and business-ready.
- Use bullets and tables where useful.
- Include assumptions explicitly.
- End with a short "Questions to clarify" section.
"""

        response = self.client.responses.create(
            model=self.model,
            instructions=instructions,
            input=prompt,
        )

        return response.output_text
