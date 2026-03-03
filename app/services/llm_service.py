import os
import time
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PRIMARY_MODEL = os.getenv("PRIMARY_MODEL", "llama-3.3-70b-versatile")
FALLBACK_MODEL = os.getenv("FALLBACK_MODEL", "llama-3.1-8b-instant")

client = Groq(api_key=GROQ_API_KEY)


class LLMService:

    def generate_response(self, message: str):

        start_time = time.time()

        try:
            response = client.chat.completions.create(
                model=PRIMARY_MODEL,
                messages=[
                    {"role": "user", "content": message}
                ],
            )
            model_used = PRIMARY_MODEL

        except Exception:
            response = client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=[
                    {"role": "user", "content": message}
                ],
            )
            model_used = FALLBACK_MODEL

        latency = time.time() - start_time

        text = response.choices[0].message.content

        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens

        return {
            "response": text,
            "model_used": model_used,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "latency": latency
        }


llm_service = LLMService()