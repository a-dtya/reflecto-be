# src/scripts/init_db.py

import sys
import os

# Add src to the import path so we can import from src.database
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.db import engine
from database.models import Base

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Done.")
