import time
from fastapi import HTTPException

RATE_LIMIT = 10      # 10 requests
WINDOW_SIZE = 60     # 60 seconds


class RateLimitService:

    def __init__(self):
        # Store user request data in memory
        self.user_requests = {}

    def check_rate_limit(self, user_id: str):

        current_time = time.time()

        user_data = self.user_requests.get(user_id)

        # First request from user
        if not user_data:
            self.user_requests[user_id] = {
                "count": 1,
                "window_start": current_time
            }
            return

        elapsed_time = current_time - user_data["window_start"]

        # If time window expired → reset
        if elapsed_time > WINDOW_SIZE:
            self.user_requests[user_id] = {
                "count": 1,
                "window_start": current_time
            }
            return

        # If still inside window
        if user_data["count"] >= RATE_LIMIT:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded (10 requests per minute)"
            )

        # Otherwise increment count
        user_data["count"] += 1


# Single instance
rate_limiter = RateLimitService()