# 🎓 C++ CodeExplainer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange.svg)](https://groq.com)

A **beginner-friendly AI-powered service** that explains C++ code.

> Built with **Groq API** (free), **Gradio** (web UI), and **Python** (backend)

## ✨ Features

- 🎯 **Beginner-Focused**: Explains code simply, without technical jargon
- ⚡ **Fast**: Groq API provides responses in < 1 second
- 🆓 **Free**: 14,400+ free API requests/day
- 🏗️ **Clean Architecture**: Modular design (UI, Core Logic, LLM layers)
- 🧪 **Well-Tested**: Includes verification script


## Prerequisites

- Python 3.6+
- Free [Groq API key](https://console.groq.com/keys)

## Install & Deploy

```bash
# 1. Clone repository
git clone https://github.com/yourusername/CodeExplainer.git
cd CodeExplainer

# 2. Run setup script
chmod +x setup.sh
./setup.sh
```


## 🏗️ Architecture

### Three-Layer Design

```
┌─────────────────────────────────────────┐
│  Presentation (Gradio UI)               │
│  src/main.py                            │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Core Logic (Processing)                │
│  src/core/processor.py                  │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  Infrastructure (Groq API + Prompting)  │
│  src/llm/client.py, src/llm/prompts.py  │
└─────────────────────────────────────────┘
```

### Key Components

| File | Purpose |
|------|---------|
| `src/main.py` | Gradio UI + orchestration |
| `src/core/processor.py` | Input validation & output formatting |
| `src/llm/client.py` | Groq API gateway |
| `src/llm/prompts.py` | RTCCF prompt engineering |


## 🎯 Tech Stack

- **Frontend**: [Gradio](https://www.gradio.app/) - Easy web UI
- **Backend**: Python 3.8+
- **LLM**: [Groq API](https://groq.com) - Fast inference
- **Model**: Kimi k2 (or alternatives)
- **Prompt Engineering**: RTCCF framework with few-shot learning

## 🔧 Configuration

### Environment Variables (.env)

See `.env.example` for template.


## 📊 Project Structure

```
CodeExplainer/
├── src/
│   ├── main.py                 # Entry point
│   ├── core/
│   │   └── processor.py        # Input/output processing
│   └── llm/
│       ├── client.py           # Groq API client
│       └── prompts.py          # Prompt templates
├── .env.example                # Configuration template
├── requirements.txt            # Dependencies
├── setup.sh                    # Automated setup
├── README.md                   # GitHub README
```

## 🆘 Troubleshooting

### "GROQ_API_KEY not found"
1. Copy `.env.example` → `.env`
2. Add your Groq API key

### "Model decommissioned"
1. Find other model on Groq webiste
2. Update model in `.env`
3. Restart app

### Port 7860 in use
Edit `src/main.py`:
```python
app.launch(server_port=7861)  # Change port
```

## 🎓 Learn From This Project

Topics covered:
- ✅ Layered architecture
- ✅ Design patterns (Facade, Adapter, Strategy)
- ✅ Prompt engineering (RTCCF framework)
- ✅ API integration
- ✅ Python best practices
- ✅ Error handling

---

**Built with ❤️ for C++ learners everywhere**

⭐ If you find this helpful, please star the repository!

# Code-Explainer
# Code-Explainer
# Code-Explainer
