# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a lightweight FastAPI web application based on the supplied project documentation.

## Features

- Q&A with Gemini
- Beginner-friendly concept explanation
- 3-question MCQ quiz generation
- Educational text summarization
- Beginner → advanced learning paths
- Simple responsive HTML/CSS interface
- JSON API endpoints
- Optional local LaMini-Flan-T5 explanation model

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## 1. Open in VS Code

Extract/open the `EduGenie` folder in VS Code.

## 2. Create a virtual environment

### Windows PowerShell

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
```

If `py` is unavailable:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Configure Gemini

Copy `.env.example` to `.env`.

Put your Google AI Studio API key in:

```env
GEMINI_API_KEY=your_key_here
```

You can change the model with:

```env
GEMINI_MODEL=gemini-2.5-flash
```

Do not commit `.env` to GitHub.

## 5. Start EduGenie

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

FastAPI API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## 6. Test each feature

### Q&A

Choose **Ask a Question** and enter:

```text
Which is the largest ocean?
```

### Explanation

Choose **Explain a Concept** and enter:

```text
Pythagoras theorem
```

### Quiz

Choose **Generate Quiz** and paste a paragraph. EduGenie returns exactly 3 questions with 4 options each.

### Summary

Paste an educational passage and choose **Summarize**.

### Learning path

Choose **Learning Path**, enter:

```text
SQL
```

and select beginner/intermediate/advanced.

## API examples

### Q&A

```bash
curl -X POST http://127.0.0.1:8000/qa ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"What is photosynthesis?\"}"
```

### Quiz

```bash
curl -X POST http://127.0.0.1:8000/quiz ^
  -H "Content-Type: application/json" ^
  -d "{\"text\":\"Photosynthesis is the process by which green plants use light energy to make food.\"}"
```

## Optional local explanation model

The supplied documentation specifies LaMini-Flan-T5 for explanations.

To enable it:

```env
USE_LOCAL_EXPLAINER=true
```

The first explanation request may download the model and can require substantial RAM/disk space. If it cannot load, EduGenie automatically falls back to Gemini so the `/explain` endpoint remains usable.

## Troubleshooting

### `GEMINI_API_KEY is missing`

Make sure `.env` exists beside `main.py` and contains a valid key.

### API key/quota/model error

Check the model configured in `GEMINI_MODEL` and the API key's access/quota in Google AI Studio.

### Port already in use

Run:

```bash
uvicorn main:app --reload --port 8001
```

Then open `http://127.0.0.1:8001`.

### PowerShell blocks activation

You can run the venv's Python directly:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m uvicorn main:app --reload
```
