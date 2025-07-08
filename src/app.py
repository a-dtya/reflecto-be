from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware #allows our fe to access the be
from .routes import entries, auth, polish

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ], # allows anybody to access the be
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entries.router, prefix="/api/entries")
app.include_router(auth.router, prefix="/api/auth")
app.include_router(polish.router, prefix="/api/polish")
