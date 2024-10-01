# app/extract.py (alternative)
import json
import logging

logging.basicConfig(level=logging.INFO)

def extract_data():
    logging.info("Extracting data from local files...")
    
    with open("mock_data/crm_data.json") as crm_file:
        crm_data = json.load(crm_file)

    with open("mock_data/sales_data.json") as sales_file:
        sales_data = json.load(sales_file)
    
    logging.info("Data extracted successfully.")
    
    return {"crm_data": crm_data, "sales_data": sales_data}
