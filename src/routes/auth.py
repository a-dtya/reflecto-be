# src/routes/auth.py
from fastapi import APIRouter, Request
from utils import authenticate_and_get_user_id

router = APIRouter()

@router.get("/me")
def get_current_user(request: Request):
    return authenticate_and_get_user_id(request)
