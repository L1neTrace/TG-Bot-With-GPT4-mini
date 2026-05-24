# 🤖 TG-Bot-With-GPT4-mini

**Телеграм бот с внутренним Chat GPT 4 Mini (или GPT-4o-mini)**

---

## 📦 Используемые библиотеки

1.  **`Telethon`** — стабильная библиотека для работы с Telegram API. Установить: `pip install telethon`
2.  **OpenAI** — библиотека для отправки запросов к GPT-4 mini через API. Установить: `pip install openai`

---

## ⚙️ Настройка и установка

### 1. Получение ключей Telegram
Замените значения в коде:
```python
api_id = 'получите в telegram devs'   #получите на сайте https://my.telegram.org
api_hash = 'получите в telegram devs' #получите на сайтеhttps://my.telegram.org
bot_token = 'токен бота'              #получите на сайте https://t.me/BotFather
```

### 2. Прокси (только для пользователей из РФ)
Если вы находитесь в России, укажите свои прокси-данные:
```python
PROXY_IP = '127.0.0.1'
PROXY_PORT = 1443
SECRET = 'dd31873781a5d45d0f57927e776bb269a0'

proxy = (PROXY_IP, PROXY_PORT, SECRET)

app = TelegramClient('bot_session', api_id, api_hash,
                     connection=connection.ConnectionTcpMTPProxyRandomizedIntermediate,
                     proxy=proxy)
```
> **Если вы НЕ из РФ:** Удалите все упоминания `proxy` и `connection=connection.ConnectionTcpMTPProxyRandomizedIntermediate`.

### 3. Получение OpenAI API ключа
- Зарегистрируйтесь на [https://platform.openai.com](https://platform.openai.com)
- Создайте API ключ в разделе "API Keys"

### 4. Настройка системного промпта
Переменная `SYSTEM_PROMPT` задаёт "личность" и поведение бота при первом запросе.

---

## 🎯 Назначение проекта

Проект создан для **обучения** и может служить **готовой заготовкой** для быстрого запуска бота с бесплатной моделью GPT.

---
## 📝 Лицензия
*Solar Line*
