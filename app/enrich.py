# app/enrich.py
import random

def enrich_data(data):
    # Simulated enrichment: Adding mock job titles for each customer
    job_titles = ['Software Engineer', 'Product Manager', 'Data Scientist', 'Sales Executive', 'Marketing Specialist']

    for index, row in data.iterrows():
        # Assign a random job title to simulate enrichment
        data.at[index, 'job_title'] = random.choice(job_titles)
    
    return data
