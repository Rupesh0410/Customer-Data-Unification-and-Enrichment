# app/main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.extract import extract_data
from app.transform import transform_data
from app.load import load_data
from apscheduler.schedulers.background import BackgroundScheduler
from app.utils import setup_database

app = FastAPI()

# Setting up template directory for Jinja2
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Create the MySQL table if it doesn't exist
setup_database()

# Scheduler for periodic data pulls
scheduler = BackgroundScheduler()

@app.get("/")
async def home(request: Request):
    # Fetch data from the database
    data = load_data(fetch=True)
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})

# Task scheduling
def run_pipeline():
    data = extract_data()
    unified_data = transform_data(data)
    load_data(unified_data)

# Schedule the pipeline every hour (or modify based on config)
scheduler.add_job(run_pipeline, 'interval', seconds=3600)
scheduler.start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
