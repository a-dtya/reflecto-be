from fastapi import APIRouter, HTTPException
from database.schemas import WorkEntryCreate
from ai_polisher import polish_work_entry

router = APIRouter()

@router.post("/generate")
async def polish_entry(payload: WorkEntryCreate):
    try:
        result = await polish_work_entry(payload.entry)

        if result.get("polished_output") == payload.entry:
            raise HTTPException(status_code=500, detail="AI polishing failed, returning raw input.")

        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
