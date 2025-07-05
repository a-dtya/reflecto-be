# src/routes/entries.py
from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.schemas import WorkEntryCreate, WorkEntryPublicResponse
from database.crud import create_work_entry, get_daily_entries, get_remaining_quota
from utils import authenticate_and_get_user_id
from datetime import datetime
from ai_polisher import polish_work_entry

router = APIRouter()

def get_db(): #dependency to get db session, the yield is used to return the db session, if no active session is found, it will create a new one
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/entry", response_model=WorkEntryPublicResponse)
async def submit_entry(request: Request, data: WorkEntryCreate, db: Session = Depends(get_db)):
    user = authenticate_and_get_user_id(request)
    quota = get_remaining_quota(db, user["user_id"])
    
    if quota.quota_remaining <= 0:
        raise HTTPException(status_code=403, detail="Daily quota exceeded")

    polished_result = await polish_work_entry(data.entry)

    new_entry = create_work_entry(db, user["user_id"], data.entry, polished_output=polished_result.get("polished_output"))

    # Update quota
    quota.quota_remaining -= 1
    db.commit()

    return WorkEntryPublicResponse.model_validate(new_entry)


@router.get("/entries", response_model=list[WorkEntryPublicResponse])
def get_today_entries(request: Request, db: Session = Depends(get_db)):
    user = authenticate_and_get_user_id(request)
    today = datetime.now()
    return [WorkEntryPublicResponse.model_validate(entry) for entry in get_daily_entries(db, user["user_id"], today)]


@router.get("/quota")
def get_quota(request: Request, db: Session = Depends(get_db)):
    user = authenticate_and_get_user_id(request)
    return get_remaining_quota(db, user["user_id"])

