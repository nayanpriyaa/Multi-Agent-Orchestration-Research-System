from app.services.llm_service import llm_service

response = llm_service.generate(
    prompt="Explain AI in simple terms",
    system_prompt="You are a helpful assistant"
)

print(response)