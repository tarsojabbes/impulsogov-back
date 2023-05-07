from typing import Dict
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Adiciona middleware para permitir CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_current_time_gmt_minus3_minus5() -> tuple[str, str]:
    """Retorna a hora atual em GMT-3 e GMT-5 no formato HH:MM:SS"""
    current_utc = datetime.utcnow()
    current_time_gmt_minus3 = (current_utc - timedelta(hours=3)).strftime("%H:%M:%S")
    current_time_gmt_minus5 = (current_utc - timedelta(hours=5)).strftime("%H:%M:%S")
    return (current_time_gmt_minus3, current_time_gmt_minus5)

@app.get("/")
async def current_time(gmt: int = None) -> Dict[str, str]:
    """
    Endpoint que retorna a hora atual em GMT-3 e GMT-5.

    Parâmetros:
    - gmt (int): GMT desejado. Se não informado, retorna ambos os horários.
    - Retorno:
      - Current time at GMT -3 (str): horário atual em GMT-3 no formato HH:MM:SS.
      - Current time at GMT -5 (str): horário atual em GMT-5 no formato HH:MM:SS.
    """
    current_time_gmt_minus3, current_time_gmt_minus5 = get_current_time_gmt_minus3_minus5()

    if gmt == -3: 
        return {"Current time at GMT -3": current_time_gmt_minus3}
    
    if gmt == -5:
        return {"Current time at GMT -5": current_time_gmt_minus5}
    
    if gmt is None:
        return {"Current time at GMT -3": current_time_gmt_minus3,
             "Current time at GMT -5": current_time_gmt_minus5}
    
    raise HTTPException(status_code=400, detail=f"GMT {gmt} not supported")
