import pandas as pd
import random

def generate_campaign_data(num_campaigns=10):
    data = []
    for i in range(num_campaigns):
        campaign_id = f"campaign_{i+1}"
        impressions = random.randint(1000, 10000)
        clicks = random.randint(0, impressions)
        conversions = random.randint(1, clicks // 10)
        spend = round(random.uniform(50, 500), 2)
        revenue = round(random.uniform(0, spend * 3), 2)
        status = random.choice(["Active", "Paused"])
        data.append([campaign_id, impressions, clicks, conversions, spend, revenue, status])
    return data

columns = ["Campaign ID", "Impressions", "Clicks", "Conversions", "Spend", "Revenue", "Status"]
data = generate_campaign_data()
df = pd.DataFrame(data, columns=columns)
df.to_csv("campaign_data.csv", index=False)


if __name__=="__main__":
    generate_campaign_data(10)




