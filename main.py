from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/")
def current_time():
    current_utc = datetime.utcnow()
    current_time_gmt_minus_3 = (current_utc - timedelta(hours=3)).strftime("%H:%M:%S")
    current_time_gmt_minus_5 = (current_utc - timedelta(hours=5)).strftime("%H:%M:%S")


    return [{"Current time at GMT -3": current_time_gmt_minus_3,
             "Current time at GMT -5": current_time_gmt_minus_5
             }]