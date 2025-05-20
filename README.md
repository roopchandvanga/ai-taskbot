# AI TaskBot

AI TaskBot is a command-line AI agent that can search the web, run Python code, and save outputs to files — all using natural language. It’s powered by LangChain and OpenAI GPT-3.5, with optional tools like SerpAPI and Python REPL.

---

## ✅ Features

- 🔗 **LangChain agent architecture**
- 🧠 **LLM (GPT-3.5 via OpenAI API)**
- 🔍 **Search tool** using SerpAPI 
- 🧮 **Python code execution** using Python REPL
- 📝 **File writing** to `output.txt` 
- 💬 **Command-line interaction loop**

---

## 📦 Prerequisites

- Python 3.10+
- Git
- OpenAI API key (for GPT-3.5)
- SerpAPI key (for web search) *(optional)*

---

## 🛠 Step-by-Step Setup

### 🔧 1. Clone and Set Up Project

```bash
git clone https://github.com/yourusername/ai-taskbot.git
cd ai-taskbot
```

### 🌱 2. Create and Activate Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\Activate  # On PowerShell (Windows)
```

### 📥 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 🔐 4. Set Up Environment Variables

Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
SERPAPI_API_KEY=your-serpapi-key 
```

### 💬 5. Example Prompts

Try commands like:
- Search for current AI trends and save to a file
- What is the factorial of 12?
- Search for top 5 data analyst interview questions and save it to questions.txt
- Find top 3 free courses to learn Python and write them to a pycourses.txt










