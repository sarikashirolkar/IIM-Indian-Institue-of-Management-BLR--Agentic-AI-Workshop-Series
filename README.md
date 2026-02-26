# 🚀 AI Business Proposal Agent

A practical **Agentic AI project** built after attending the **IIM Bangalore (IIM-B) AI Workshop Series**.

In the workshop, we designed the concept using **Make.com** workflows. I implemented the full working version in **Python + Streamlit + OpenAI ChatGPT API**.

## ✨ What This Project Does

This app asks for just 3 inputs:
1. **Company Name**
2. **Industry**
3. **Business Goal**

Then it generates a structured business proposal including:
- Executive summary
- Company and industry snapshot
- Market trends
- Competitor landscape
- Opportunity gaps
- Strategy roadmap (90 days, 6 months, 12 months)
- Budget and ROI assumptions
- Risks and mitigations
- KPI dashboard
- Action steps for the first 14 days

## 🧠 Why This Is Useful

- Great for founders, consultants, and strategy teams
- Fast first-draft proposals in minutes
- Consistent structure across different business scenarios
- Easy to customize and extend

## 🛠 Tech Stack

- **Python 3**
- **Streamlit** (frontend)
- **OpenAI Python SDK**
- **ChatGPT models** via OpenAI API

## 🔒 API & Security Notes

- This project uses **only OpenAI API** for AI generation.
- API keys are loaded from environment variables.
- `.env`, virtual environments, and cache folders are ignored via `.gitignore`.
- Never hardcode or commit your API key.

## 📁 Project Structure

```text
.
├── agent.py            # Core proposal generation logic
├── streamlit_app.py    # Streamlit UI (3 input fields + output)
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules (secrets/venv/cache)
└── README.md
```

## ⚙️ Setup

```bash
# 1) Clone
git clone https://github.com/sarikashirolkar/IIM-Indian-Institue-of-Management-BLR--Agentic-AI-Workshop-Series.git
cd IIM-Indian-Institue-of-Management-BLR--Agentic-AI-Workshop-Series

# 2) Create virtual env (example)
python3 -m venv myenv
source myenv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Add API key
cp .env.example .env
# then set OPENAI_API_KEY in .env or export it in your shell
```

## ▶️ Run the App

```bash
export OPENAI_API_KEY="your_key_here"
# Optional: choose model
export OPENAI_MODEL="gpt-4.1-mini"

streamlit run streamlit_app.py
```

Open the local URL shown by Streamlit in your browser.

## 🧪 Example Input

- Company Name: `Acme Logistics`
- Industry: `Supply Chain / Logistics Tech`
- Goal: `Increase B2B lead generation by 30% within 6 months`

## 📌 Notes on Model Choice

Default model is set to **`gpt-4.1-mini`** for speed and lower cost.
You can switch models anytime with:

```bash
export OPENAI_MODEL="gpt-4.1"
```

## 🚧 Future Improvements

- Download proposal as PDF
- Add editable proposal templates by industry
- Add memory/history of generated proposals
- Add team collaboration and approval workflows

## 🙌 Workshop Context

This repository reflects a hands-on build inspired by the **IIM-B Agentic AI Workshop Series**.
Conceptual workflow exploration was done with **Make.com**, while this implementation is fully coded in Python for flexibility and control.

## 📜 License

Use this project for learning, prototyping, and internal strategy work.
