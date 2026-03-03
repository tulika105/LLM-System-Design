from fastapi import Header, HTTPException

# Simple static API keys for demonstration purposes
VALID_API_KEYS = {
    "user1-key": "user_1",
    "user2-key": "user_2", 
    "user3-key": "user_3"
}


def authenticate_user(x_api_key: str = Header(...)):

    if x_api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )

    return VALID_API_KEYS[x_api_key]