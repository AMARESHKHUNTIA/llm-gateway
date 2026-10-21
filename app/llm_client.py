import httpx

from app.config import settings


async def generate_response(prompt: str) -> str:
    url="https://api.groq.com/openai/v1/chat/completions"

    headers = {
        'Authorization':f'Bearer {settings.groq_api_key}',
        'Content-Type': 'application/json'
    }

    payload={
        'model':settings.llm_model,
        'messages': [
            {
                'role':'user',
                'content':prompt
            }
        ]
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response= await client.post(
            url,
            headers=headers,
            json=payload
        )

    response.raise_for_status()

    data=response.json()
    return data['choices'][0]['message']['content']