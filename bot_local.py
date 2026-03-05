import telebot
from dotenv import load_dotenv
import os
from collections import defaultdict

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage


load_dotenv()

OPENROUTER_BASE = "http://localhost:11434/v1"  # LOCAL_API_URL
MODEL_NAME = "gemma3:4b"  # "qwen/qwen3-coder:free" openai/gpt-oss-20b:free

llm = ChatOpenAI(
    openai_api_key="fake_key",
    openai_api_base=OPENROUTER_BASE,
    model_name=MODEL_NAME,
)

# Храним историю по пользователю: chat_id -> список диктов {"role": "...", "content": "..."}
user_histories = defaultdict(list)
MAX_PAIRS = 5  # количество последних пар вопрос–ответ


def build_history_messages(chat_id: int, new_user_text: str):
    """Построить список сообщений для LLM: последние MAX_PAIRS пар + новый вопрос."""
    history = user_histories[chat_id]
    # Берём последние MAX_PAIRS*2 сообщений (user+bot)
    truncated = history[-MAX_PAIRS * 2 :]

    messages = []
    for item in truncated:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            messages.append(AIMessage(content=item["content"]))

    # Добавляем текущее сообщение пользователя
    messages.append(HumanMessage(content=new_user_text))
    return messages


# Замените 'bot_token' на токен вашего бота, сохранённого в секретах / переменных среды
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_llm_message(message):
    chat_id = message.chat.id
    user_text = message.text or ""

    try:
        print(f"[{chat_id}] USER:", user_text)

        # Готовим историю + новое сообщение
        messages = build_history_messages(chat_id, user_text)

        # Отправляем в LLM
        llm_response = llm.invoke(messages)
        response_text = getattr(llm_response, "content", str(llm_response))
        print(f"[{chat_id}] ASSISTANT:", response_text)

        # Обновляем историю: сначала вопрос, потом ответ
        user_histories[chat_id].append({"role": "user", "content": user_text})
        user_histories[chat_id].append({"role": "assistant", "content": response_text})

        # Отвечаем бота ответом LLM
        bot.reply_to(message, response_text)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}. Попробуйте позже.")


# Запуск бота
bot.polling()