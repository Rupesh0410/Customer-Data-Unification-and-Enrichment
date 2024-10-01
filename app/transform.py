# app/transform.py
import pandas as pd
from thefuzz import fuzz

def transform_data(data):
    # Unify the data into a master dataset using Pandas
    crm_df = pd.DataFrame(data["crm_data"])
    sales_df = pd.DataFrame(data["sales_data"])
    
    # Perform data cleaning and merging
    merged_data = pd.merge(crm_df, sales_df, how="outer", on="customer_id")
    
    # Handle duplicates using fuzzy matching
    for i, row in merged_data.iterrows():
        # Example fuzzy matching condition
        if fuzz.ratio(row['name_x'], row['name_y']) > 80:
            merged_data.at[i, 'name'] = row['name_x'] if pd.notna(row['name_x']) else row['name_y']
    
    # Dropping unnecessary columns after merging
    merged_data.drop(columns=["name_x", "name_y"], inplace=True)
    
    return merged_data
