import requests
from typing import Optional

from app.config import settings


class LLMService:

    def __init__(self):
        self.provider = settings.MODEL_PROVIDER
        self.model_name = settings.MODEL_NAME

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
      
        if self.provider == "ollama":
            return self._generate_ollama(prompt, system_prompt)
        elif self.provider == "openai":
            return self._generate_openai(prompt, system_prompt)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def _generate_ollama(self, prompt: str, system_prompt: Optional[str]) -> str:
        url = "http://localhost:11434/api/generate"

        full_prompt = self._build_prompt(prompt, system_prompt)

        response = requests.post(
            url,
            json={
                "model": self.model_name,
                "prompt": full_prompt,
                "stream": False
            }
        )

        if response.status_code != 200:
            raise Exception(f"Ollama error: {response.text}")

        data = response.json()
        return data.get("response", "")

    def _generate_openai(self, prompt: str, system_prompt: Optional[str]) -> str:
        from openai import OpenAI

        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        messages = []

        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content

    def _build_prompt(self, prompt: str, system_prompt: Optional[str]) -> str:
        if system_prompt:
            return f"{system_prompt}\n\nUser:\n{prompt}"
        return prompt


llm_service = LLMService()