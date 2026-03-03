import json
import os
from typing import Dict

# Storage file path
STORAGE_PATH = "app/storage/usage.json"

# Simulated pricing structure (per token)
# These are mock values for learning/demo purposes
MODEL_PRICING = {
    "llama-3.3-70b-versatile": {
        "input_price": 0.000001,
        "output_price": 0.000002
    },
    "llama-3.1-8b-instant": {
        "input_price": 0.0000005,
        "output_price": 0.000001
    }
}


class UsageService:

    def __init__(self):
        self.usage_data: Dict = self._load_usage()

    # -------------------------
    # Load existing usage data
    # -------------------------
    def _load_usage(self):

        if not os.path.exists(STORAGE_PATH):
            os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)
            with open(STORAGE_PATH, "w") as f:
                json.dump({}, f)

        with open(STORAGE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    # -------------------------
    # Save usage data to JSON
    # -------------------------
    def _save_usage(self):

        with open(STORAGE_PATH, "w") as f:
            json.dump(self.usage_data, f, indent=4)

    # -------------------------
    # Calculate cost properly
    # -------------------------
    def _calculate_cost(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int
    ) -> float:

        pricing = MODEL_PRICING.get(model)

        if not pricing:
            pricing = {
                "input_price": 0.000001,
                "output_price": 0.000001
            }

        input_cost = input_tokens * pricing["input_price"]
        output_cost = output_tokens * pricing["output_price"]

        return input_cost + output_cost

    # -------------------------
    # Update user usage
    # -------------------------
    def update_usage(
        self,
        user_id: str,
        model: str,
        input_tokens: int,
        output_tokens: int
    ) -> float:

        if user_id not in self.usage_data:
            self.usage_data[user_id] = {
                "total_requests": 0,
                "total_tokens": 0,
                "total_cost": 0.0
            }

        total_tokens = input_tokens + output_tokens
        cost = self._calculate_cost(model, input_tokens, output_tokens)

        self.usage_data[user_id]["total_requests"] += 1
        self.usage_data[user_id]["total_tokens"] += total_tokens
        self.usage_data[user_id]["total_cost"] += cost

        self._save_usage()

        return cost

    # -------------------------
    # Get user usage summary
    # -------------------------
    def get_usage(self, user_id: str):

        return self.usage_data.get(
            user_id,
            {
                "total_requests": 0,
                "total_tokens": 0,
                "total_cost": 0.0
            }
        )


# Singleton instance
usage_service = UsageService()