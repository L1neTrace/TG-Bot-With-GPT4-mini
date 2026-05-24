from openai import OpenAI
import logging
from telethon import TelegramClient, events, connection
from tqdm.contrib import telegram

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_id = 'получите в telegram devs'
api_hash = 'получите в telegram devs'
bot_token = 'токен бота'

PROXY_IP = '127.0.0.1'
PROXY_PORT = 1443
SECRET = 'dd31873781a5d45d0f57927e776bb269a0'

proxy = (PROXY_IP, PROXY_PORT, SECRET)

app = TelegramClient(
    'bot_session',
    api_id,
    api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=proxy
)

client = OpenAI(
    api_key="ващ API ключ",
    base_url="https://openrouter.ai/api/v1",
)

SYSTEM_PROMPT = (
    "Ты умный IT-чат бот умеющий помогать по коду и обучать также ты знаешь много информации чтобы отвечать не только на вопросы по коду, твой разработчик сделавший тебя под телеграмм бота @SolarMyNone")

histories = {}


@app.on(events.NewMessage(pattern="/start"))
async def hello_user(event):
    await event.reply("🥰Привет я ии-чат бот!\n\n"
                      "🛠Мой разработчик @User\n"
                      "🎭Я основан на модели openai/gpt-4o-mini \n\n"
                      "🤖Версия бота V1")


@app.on(events.NewMessage)
async def gpt_request(event):
    if not event.text:
        return

    if event.text.startswith('/'):
        return

    chat_id = event.chat_id

    if chat_id not in histories:
        histories[chat_id] = []

    histories[chat_id].append({"role": "user", "content": event.text})

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + histories[chat_id]
    wait_message = await event.reply("🤖 Готовлю ответ, подождите...")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages,
            max_tokens=990,
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()

        histories[chat_id].append({"role": "assistant", "content": reply})

        await wait_message.delete()
        await event.reply(reply)

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        await event.reply("Что-то пошло не так...")


if __name__ == "__main__":
    logging.info("Бот запущен...")
    app.start(bot_token=bot_token)
    app.run_until_disconnected()
