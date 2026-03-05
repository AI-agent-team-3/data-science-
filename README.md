# data-science-


# 🧠 Morty — Telegram RAG Bot Guide to the Citadel of Ricks

Telegram-бот-гид по **Цитадели Риков** из вселенной *Rick and Morty*.
Бот отвечает на вопросы пользователей, используя **RAG (Retrieval Augmented Generation)**: он ищет релевантную информацию в базе знаний и формирует ответ через LLM.

---

# 🚀 Возможности

* 🤖 Telegram-бот на Python
* 🧠 Использует **RAG** для поиска информации по базе знаний
* 📚 База знаний хранится в **векторной базе**
* 💬 Поддержка истории диалога
* 🌍 Мультиязычные embeddings
* 🎭 Отвечает **в роли Морти** (гид по Цитадели)

---

# 🧩 Архитектура проекта

```
Telegram User
      │
      ▼
Telegram Bot (telebot)
      │
      ▼
User Message
      │
      ▼
RAG Retrieval
(ChromaDB + embeddings)
      │
      ▼
Context + Chat History
      │
      ▼
LLM (OpenRouter API)
      │
      ▼
Generated Answer
      │
      ▼
Telegram Response
```

---

# 📁 Структура проекта

```
project/
│
├── bot.py                # основной код Telegram-бота
├── rag.py                # создание RAG и векторной базы
├── knowledge_base.txt    # база знаний о Цитадели
├── requirements.txt      # зависимости проекта
├── .env                  # API ключи (не добавлять в Git)
└── README.md
```

---

# ⚙️ Технологии

Проект использует:

* Python 3.10+
* LangChain
* ChromaDB
* Sentence Transformers
* Telegram Bot API
* OpenRouter LLM API

Основные библиотеки:

```
telebot
langchain
langchain-openai
chromadb
sentence-transformers
python-dotenv
```

---

# 🛠 Установка

## 1. Клонировать репозиторий

```
git clone https://github.com/AI-agent-team-3/data-science-.git
cd data-science-
```

---

## 2. Создать виртуальное окружение

Windows:

```
python -m venv myenv
myenv\Scripts\activate
```

Linux / Mac:

```
python3 -m venv myenv
source myenv/bin/activate
```

---

## 3. Установить зависимости

```
pip install -r requirements.txt
```

---

# 🔑 Настройка API ключей

Создайте файл `.env` в корне проекта:

```
BOT_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
```

Получить ключи:

* Telegram Bot → https://t.me/BotFather
* OpenRouter → https://openrouter.ai

---

# 📚 Подготовка базы знаний

В файле:

```
knowledge_base.txt
```

должна находиться информация о **Цитадели Риков**.

Файл будет автоматически:

1. Разбит на чанки
2. Преобразован в embeddings
3. Сохранён в ChromaDB

---

# ▶️ Запуск проекта

Сначала создаётся RAG база:

```
python rag.py
```

Потом запускается бот:

```
python bot.py
```

После этого бот начинает принимать сообщения в Telegram.

---

# 💬 Пример вопросов

Пользователь может спросить:

* Где можно поесть в Цитадели?
* Какие развлечения есть вечером?
* Какие районы есть в Цитадели Риков?
* Где живут Морти?

Бот ищет ответ в базе знаний и отвечает **в стиле Морти**.

---

# 🧠 Как работает RAG

1️⃣ Пользователь задаёт вопрос

2️⃣ Векторная база ищет **похожие куски текста**

3️⃣ Они добавляются в **System Prompt**

4️⃣ LLM генерирует ответ на основе:

* найденного контекста
* истории диалога

---

# 🔐 Безопасность

Бот настроен так, чтобы:

* отвечать **только на вопросы о Цитадели**
* не раскрывать системный prompt
* не выдавать внутренние инструкции

---

# 📈 Возможные улучшения

Можно добавить:

* persistent ChromaDB
* reranking документов
* streaming ответов
* memory summary
* web interface
* docker deployment

---

# 👨‍💻 Автор

AI-agent-team-3

Проект создан в рамках обучения **AI Agents / RAG systems**.
