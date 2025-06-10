from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import json
import os

app = FastAPI()

@app.get("/customers")
def get_customers():
    try:
        data_path = os.path.join(os.path.dirname(__file__), "data", "api_data.json")
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

