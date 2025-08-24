from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def suggest_hts_code(description: str) -> str:
    prompt = f"""
    You are a customs classification assistant.
    Based on this product description, suggest the most probable 6-digit HTS/HS code.
    Respond ONLY with the numeric code (no text).

    Product description: "{description}"
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful customs classification assistant.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            max_tokens=20,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI API call failed:", e)
        return "010121"
