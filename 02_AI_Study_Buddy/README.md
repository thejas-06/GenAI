# AI Study Buddy

A simple exam preparation tool that generates study material from your notes using the Gemini API.

## What it does

You paste your notes or syllabus topics, and it generates:

- Flashcards for quick revision
- Multiple choice questions with answers
- Short answer questions
- A revision summary of key points

You can choose the difficulty level (Easy, Medium, Hard) depending on what you need.

## Files

- `app.py` — Streamlit web app
- `prompts.py` — Prompt templates used for generation
- `02_AI_Study_Buddy.ipynb` — Jupyter notebook version (runs on Google Colab)

## How to run

Create a virtual environment and install dependencies:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

Enter your Gemini API key in the sidebar when the app opens.

## API Key

This project uses the Google Gemini API (free tier). You can get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

## Built with

- Python
- Streamlit
- Google Gemini 2.5 Flash
