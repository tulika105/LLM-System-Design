from pydantic import BaseModel, Field


# Request model for /chat
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)


# Response model for /chat
class ChatResponse(BaseModel):
    response: str
    model_used: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    latency: float


# Response model for /usage
class UsageResponse(BaseModel):
    user_id: str
    total_requests: int
    total_tokens: int
    total_cost: float