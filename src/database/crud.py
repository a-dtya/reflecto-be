#here goes the db query/ operations
# src/database/crud.py

from sqlalchemy.orm import Session
from . import models
from datetime import datetime

def create_work_entry(db: Session, user_id: str, entry: str, polished_output: str):
    new_entry = models.WorkEntry(
        user_id=user_id,
        entry=entry,
        polished_output=polished_output,
        created_at=datetime.utcnow()
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

def get_daily_entries(db: Session, user_id: str, date: datetime):
    return db.query(models.WorkEntry)\
             .filter(models.WorkEntry.user_id == user_id)\
             .filter(models.WorkEntry.created_at >= date.date())\
             .all()

def get_remaining_quota(db: Session, user_id: str):
    today = datetime.now().date()
    quota = db.query(models.DailyQuota)\
             .filter(models.DailyQuota.user_id == user_id)\
             .filter(models.DailyQuota.date == today)\
             .first()
    if not quota: #to reset the quota every day
        quota = create_daily_quota(db, user_id)
    return quota
    
def create_daily_quota(db: Session, user_id: str):
    today = datetime.now().date()
    new_quota = models.DailyQuota(
        user_id=user_id,
        date=today,
        quota_remaining=3,
        last_reset_at=datetime.now()
    )
    db.add(new_quota)
    db.commit()
    db.refresh(new_quota)
    return new_quota
    
