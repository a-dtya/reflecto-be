import os
import json
from openai import OpenAI
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def polish_work_entry(entry: str) -> Dict[str, str]:
    with open("src/prompts/polisher_prompt.txt", "r") as f:
        system_prompt = f.read()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Polish this work summary:\n\n{entry}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.5
        )

        content = response.choices[0].message.content
        # print(f"[AI POLISH CONTENT]: {content}")
        result = json.loads(content)

        if "polished_output" not in result:
            raise ValueError("Missing 'polished_output' in response")

        return result

    except Exception as e:
        print(f"[AI POLISH ERROR]: {str(e)}")
        return {
            "polished_output": entry  # fallback to raw entry if polishing fails
        }
