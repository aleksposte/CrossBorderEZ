import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def suggest_hts_code(description: str) -> str:
    """
    Call OpenAI to suggest HTS/HS code for a product description.
    """
    prompt = f"""
    You are a customs classification assistant.
    Based on this product description, suggest the most probable 6-digit HS/HTS code.
    Respond ONLY with the numeric code (no text).

    Product description: "{description}"
    """

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
