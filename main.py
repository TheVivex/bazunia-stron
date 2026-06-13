import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
try:
    with open("verified_online.json", "r", encoding="utf-8") as file:
        json_data = json.load(file)
except FileNotFoundError:
    json_data = {"error": "plik nieznaleziony"}

@app.get("/pobierzDane")
def pobierz_dane():
    return JSONResponse(content=json_data)

@app.get("/health")
def health_check():
    return {"status": "OK"}