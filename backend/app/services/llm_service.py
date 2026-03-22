from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def ask_gpt(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 노코드 전문가 'My Helper'야. 1.원인 2.해결방법 3.팁 순서로 친절하게 답해줘."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content