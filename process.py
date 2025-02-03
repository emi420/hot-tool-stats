import pandas as pd
import requests
from datetime import datetime
from config import MATOMO_API_URL, MATOMO_TOKEN_AUTH, MATOMO_SITES_IDS

def fetch_data(
    title, url, id, start_date, end_date
):
    start_date_obj = datetime.combine(start_date, datetime.min.time())
    end_date_obj = datetime.combine(end_date, datetime.max.time())
    
    # Visitor stats
    stats_url = f"{MATOMO_API_URL}/index.php?module=API&method=VisitsSummary.getUniqueVisitors&idSite={MATOMO_SITES_IDS[url]}&period=month&date=lastMonth&format=json"
    response_stats = requests.post(stats_url, data={"token_auth": MATOMO_TOKEN_AUTH})
    response_obj = response_stats.json()

    df_data = {"Unique users": response_obj["value"]}
    df_data['startDate'] = start_date_obj.isoformat()
    df_data['endDate'] = end_date_obj.isoformat()
    response_df = pd.DataFrame([df_data])
    

    # Add extra columns
    response_df["Title"] = title
    response_df["Map Data ID"] = response_df.apply(lambda row: f"MD-{row['Title']}-{row['endDate']}", axis=1)
    response_df["Project ID (From Finance)"] = id

    # Re-order, rename and remove extra columns
    firstColumns = ["Map Data ID", "Project ID (From Finance)", "Title", "startDate", "endDate"]
    columns = firstColumns + [col for col in response_df.columns if col not in firstColumns]
    response_df = response_df[columns]
    response_df = response_df.rename(columns={
        'startDate': 'Start Date', 
        'endDate': 'End Date'
    })

    return response_df
