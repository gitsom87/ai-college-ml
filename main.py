from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize app
app = FastAPI(
    title="AI College ML Service",
    description="Simple ML prediction API",
    version="1.0"
)

# =========================
# Request Model
# =========================
class PredictionRequest(BaseModel):
    value: float


# =========================
# Response Model
# =========================
class PredictionResponse(BaseModel):
    input: float
    prediction: float


# =========================
# Health Check
# =========================
@app.get("/")
def home():
    return {
        "message": "ML Service is running 🚀"
    }


# =========================
# Prediction API
# =========================
@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):
    try:
        # Dummy ML logic (replace later with real model)
        result = data.value * 10

        return PredictionResponse(
            input=data.value,
            prediction=result
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# Optional: Health endpoint
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}