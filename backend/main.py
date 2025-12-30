from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predictor import StudentPredictor
from typing import List, Dict, Any

app = FastAPI(title="Student Performance API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = StudentPredictor()
predictor.train_models()

class StudentData(BaseModel):
    study_hours: int
    previous_grade: int
    attendance: int
    extracurricular: str
    parent_education: str
    family_support: str
    internet_access: str
    assignments_completed: int

@app.get("/")
async def root():
    return {"message": "Student Performance API is running"}

@app.get("/stats")
async def get_stats():
    stats = predictor.get_stats()
    if not stats:
        raise HTTPException(status_code=404, detail="Stats not found")
    return stats

@app.get("/models")
async def get_models():
    results = []
    for name, info in predictor.models.items():
        results.append({
            "name": name,
            "accuracy": info["accuracy"],
            "auc": info["auc"],
            "roc_data": info["roc_data"]
        })
    return results

@app.post("/predict")
async def predict(data: StudentData):
    try:
        result = predictor.predict(data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
