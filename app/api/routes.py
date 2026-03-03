from fastapi import APIRouter, Depends
from app.models.schemas import ChatRequest, ChatResponse, UsageResponse
from app.services.auth_service import authenticate_user
from app.services.rate_limit_service import rate_limiter
from app.services.llm_service import llm_service
from app.services.usage_service import usage_service

router = APIRouter() 


# -------------------------
# Health Endpoint
# -------------------------
@router.get("/health")
async def health():
    return {"status": "healthy"}


# -------------------------
# Chat Endpoint
# -------------------------
@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    user_id: str = Depends(authenticate_user)
):
    # 1. Rate limit check
    rate_limiter.check_rate_limit(user_id)

    # 2. Call LLM
    result = llm_service.generate_response(request.message)

    # 3. Update usage
    cost = usage_service.update_usage(
        user_id=user_id,
        model=result["model_used"],
        input_tokens=result["input_tokens"],
        output_tokens=result["output_tokens"]
    )

    # 4. Return structured response
    return ChatResponse(
        response=result["response"],
        model_used=result["model_used"],
        total_tokens=result["total_tokens"],
        input_tokens=result["input_tokens"],
        output_tokens=result["output_tokens"],
        latency=result["latency"]
    )


# -------------------------
# Usage Endpoint
# -------------------------
@router.get("/usage", response_model=UsageResponse)
async def get_usage(
    user_id: str = Depends(authenticate_user)
):
    usage = usage_service.get_usage(user_id)

    return UsageResponse(
        user_id=user_id,
        total_requests=usage["total_requests"],
        total_tokens=usage["total_tokens"],
        total_cost=usage["total_cost"]
    )