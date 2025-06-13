import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    store = store[(store['amount']>500)]

    store = store[['customer_id']].drop_duplicates()

    return pd.DataFrame([len(store)],columns=['rich_count'])