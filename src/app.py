from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware #allows our fe to access the be


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