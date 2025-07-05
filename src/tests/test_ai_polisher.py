# src/tests/test_ai_polisher.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ai_polisher import polish_work_entry


if __name__ == "__main__":
    entry = "fixed bugs in login and cleaned up some code"
    result = polish_work_entry(entry)
    print("Polished Output:\n", result["polished_output"])
