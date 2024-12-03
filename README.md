
# Marketing Agent Automation

## Objective

This project implements an AI-powered Marketing Automation Agent to optimize advertising campaigns based on performance data. It uses predefined rules and AI insights to take actions such as pausing campaigns, adjusting budgets, and providing actionable recommendations.

---

## Features

- **Dataset Simulation**: Generates synthetic campaign performance data.
- **Campaign Analysis**: Calculates key metrics like CTR, ROAS, CPA.
- **AI-Powered Insights**: Utilizes Google's Generative AI (Gemini API) for actionable recommendations on improving ad performance.
- **Decision-Making**: Automates campaign optimizations by pausing, increasing, or decreasing budgets based on rules.
- **Dashboard**: A local dashboard visualizes campaign performance and recommendations.

---

## Architecture

1. **Data Generation**:
   - Simulates marketing data for campaigns and saves it as `campaign_data.csv`.
2. **Analysis Pipeline**:
   - Computes metrics such as CTR, ROAS, and CPA from the dataset.
3. **AI Insights**:
   - Leverages a Large Language Model (LLM) to provide improvement suggestions for campaigns.
4. **Automation Agent**:
   - Executes optimization decisions based on predefined rules.
5. **Visualization**:
   - Provides a dashboard for tracking key metrics and decisions.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/AI-Marketing-Automation-Agent.git
   cd AI-Marketing-Automation-Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project pipeline:
   - **Step 1**: Set your gemini api key in the env file

   - **Step 2**: Generate Dataset
     ```bash
     python CreateDataset.py
     ```
   - **Step 3**: Execute the Automation Agent
     ```bash
     jupyter notebook AutomationAgent.ipynb
     ```
   - **Step 4**: Launch the Dashboard
     ```bash
     python Dashboard.py
     ```

4. Open the local dashboard at `http://localhost:8051`.

---

## Example Use Case

- Input: Campaign performance dataset (`campaign_data.csv`).
- Actions:
  - Paused campaigns with low CTR or high CPA.
  - Increased budgets for high-performing campaigns.
  - Decreased budgets for underperforming campaigns.
- Output: Updated dataset with actions logged and visualized in the dashboard.

---

## AI Integration

- **Gemini API**: Generates insights for ad creative and targeting optimizations.
- **Metrics Computed**:
  - CTR: Click-Through Rate.
  - ROAS: Return on Ad Spend.
  - CPA: Cost Per Acquisition.

---

## Extensions for Real-World Scenarios

1. **API Integration**: Connect to real ad platform APIs for live updates and adjustments.
2. **Scalability**: Batch process data for hundreds of campaigns simultaneously.
3. **Improved Insights**: Fine-tune LLMs for domain-specific recommendations.
4. **Real-Time Monitoring**: Extend the dashboard for real-time campaign tracking.

---
