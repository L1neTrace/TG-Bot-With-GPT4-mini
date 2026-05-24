# TG-Bot-With-GPT4-mini
# Телеграмм бот с внутренним Chat GPT4 Mini

 # -- КАК НАСТРОИТЬ И КАКИЕ БИБЛИОТЕКИ ИСПОЛЬЗУЮТЬСЯ --
  #1. Бот написан на стабильной библиотеки telethon
  #2. Используеться openai специальная библиотека которая с помощью API ключа отправляет запрос GPT модели

  #1. в строках api_id = 'получите в telegram devs'
api_hash = 'получите в telegram devs'
bot_token = 'токен бота' вам надо указать информацию для api_hash и api_id надо зарегистрироваться под аккаунтом в телеграмм в  https://my.telegram.org, а bot_token в https://t.me/BotFather
 #2. Если вы в России то в строках  PROXY_IP = '127.0.0.1'
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
 указываете свои прокси данные если вы не из РФ то убираете все упоминание proxy и connection=connection.ConnectionTcpMTProxyRandomizedIntermediate

 #3. вам нужно получить api openai ключ  https://platform.openai.com
 #4. SYSTEM_PROMPT это переменная будет отправлять самый 1 запрос gpt для создания персонажа по описанию

 # Проект сделан для моего обучения и для заготовки бота с бесплатной моделью GPT
