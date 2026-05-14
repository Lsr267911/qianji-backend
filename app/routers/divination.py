from fastapi import APIRouter, HTTPException
from typing import List
from app.models.questionnaire import Answer
from app.models.results import DivinationResult
from app.services.divination_service import run_full_divination

router = APIRouter()

@router.post("/divinate", response_model=DivinationResult)
async def divinate(answers: List[Answer]):
    """
    Submit 160 questionnaire answers and get full divination results.
    """
    if len(answers) < 10:
        raise HTTPException(status_code=400, detail="At least 10 answers required")
    
    try:
        result = run_full_divination(answers)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
