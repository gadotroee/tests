import os
from typing import List


def validate_env_vars(required_vars: List[str]):
    missing_env_vars = [var for var in required_vars if var not in os.environ]
    if missing_env_vars:
        raise AssertionError(f"env-vars missing: {missing_env_vars}")
