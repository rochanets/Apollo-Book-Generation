import pandas as pd
from datetime import datetime


def analyze_dataframe(df: pd.DataFrame):
    # Ensure date columns are datetime
    df['opened_date'] = pd.to_datetime(df['opened_date'])
    df['closed_date'] = pd.to_datetime(df['closed_date'], errors='coerce')
    now = datetime.now()
    current_month = now.month
    current_year = now.year

    opened_this_month = df[(df['opened_date'].dt.month == current_month) & (df['opened_date'].dt.year == current_year)]
    closed_this_month = df[(df['closed_date'].dt.month == current_month) & (df['closed_date'].dt.year == current_year)]

    backlog = df[df['closed_date'].isna()]

    df['open_month'] = df['opened_date'].dt.to_period('M')
    df['close_month'] = df['closed_date'].dt.to_period('M')

    open_history = df.groupby('open_month').size().astype(int).to_dict()
    close_history = df.groupby('close_month').size().astype(int).to_dict()

    aging_days = (now - df['opened_date']).dt.days
    aging = {
        '0-3': int(((aging_days <= 3)).sum()),
        '3-5': int(((aging_days > 3) & (aging_days <= 5)).sum()),
        '5-20': int(((aging_days > 5) & (aging_days <= 20)).sum()),
        '20+': int((aging_days > 20).sum()),
    }

    top_users = df['user'].value_counts().head(10).to_dict()
    top_analysts = df['analyst'].value_counts().head(10).to_dict()
    top_categories = df['category'].value_counts().head(10).to_dict()

    summary = {
        'opened_this_month': int(len(opened_this_month)),
        'closed_this_month': int(len(closed_this_month)),
        'backlog': int(len(backlog)),
        'open_history': {str(k): v for k, v in open_history.items()},
        'close_history': {str(k): v for k, v in close_history.items()},
        'aging': aging,
        'top_users': top_users,
        'top_analysts': top_analysts,
        'top_categories': top_categories,
    }
    return summary
