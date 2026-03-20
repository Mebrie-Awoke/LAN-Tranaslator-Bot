# Amharic-English Translator Bot
check it: @lantranslator_bot

A Telegram bot that translates between Amharic and English using Groq's Llama 3.3 70B model.

## Features
- 🤖 Automatic language detection (Amharic/English)
- 🔄 Bidirectional translation
- ⚡ Fast responses via Groq API
- 🚫 Error handling for unsupported languages

## Prerequisites
- Python
- Telegram Bot Token ([@BotFather](https://t.me/botfather))
- Groq API Key ([console.groq.com](https://console.groq.com))

## Quick Start

1. **Clone & Install**
```bash
git clone https://github.com/Mebrie-Awoke/LAN-Tranaslator-Bot
cd LAN-Translator-Bot
pip install python-telegram-bot groq python-dotenv
```

2. **Create `.env` file**
```env
TELEGRAM_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

3. **Run the bot**
```bash
python bot.py
```

## Usage
- `/start` - Welcome message
- Send any text in Amharic or English - Get instant translation

## Built With
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Groq API](https://groq.com)
