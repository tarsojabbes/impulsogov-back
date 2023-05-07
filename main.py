from typing import List, Dict
from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/")
async def current_time() -> List[Dict[str, str]]:
    """
    Endpoint que retorna a hora atual em GMT-3 e GMT-5.
    """
    current_utc = datetime.utcnow()
    current_time_gmt_minus_3 = (current_utc - timedelta(hours=3)).strftime("%H:%M:%S")
    current_time_gmt_minus_5 = (current_utc - timedelta(hours=5)).strftime("%H:%M:%S")

    return [{"Current time at GMT -3": current_time_gmt_minus_3,
             "Current time at GMT -5": current_time_gmt_minus_5}]