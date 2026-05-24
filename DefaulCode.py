from openai import OpenAI

client = OpenAI(
    api_key="ваш Api все указано в readme",
    base_url="https://openrouter.ai/api/v1",
)

SYSTEM_PROMPT = "описание персонажа"

history = []

print("🤖Чат с Ботом\n")

while True:

    user_text = input('Запрос: ')

    history.append({"role": "user", "content": user_text})

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history


    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )

    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})

    print(f"🤖Бот: {reply}\n")
