# AI Resume Analyzer

A full-stack application that analyzes resumes against job descriptions using Google's Gemini 1.5 Flash AI, providing detailed ATS scoring and feedback.

![Demo](assets/demo.png)

## Tech Stack
- Frontend: HTML5, Tailwind CSS, Vanilla JS
- Backend: FastAPI, PyMuPDF, ReportLab
- AI: Google Gemini 1.5 Flash

## Features
- Drag & Drop PDF resume upload.
- Full ATS evaluation with score, keyword matching, and verdict.
- Automatically rewrite weak bullet points using AI.
- Download a beautifully formatted PDF report of the findings.

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   Add your Gemini API Key directly to the `.env` file at the root of the project:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

3. **Run the backend server:**
   ```bash
   uvicorn backend.main:app --reload
   ```

4. **Open the frontend:**
   Open `frontend/index.html` in your favorite web browser.

## Folder Structure
```
ai-resume-analyzer/
├── backend/
│   ├── main.py              # FastAPI app, all routes
│   ├── parser.py            # PDF text extraction
│   ├── analyzer.py          # Gemini API logic + prompt
│   ├── report.py            # PDF report generator
│   └── requirements.txt
├── frontend/
│   ├── index.html           # Upload page
│   ├── result.html          # Results page
│   └── assets/
│       └── style.css        # Custom styles
├── .env                     # Contains GEMINI_API_KEY
├── .gitignore               
└── README.md
```

## Live Demo
[file:///C:/Users/A/Desktop/New%20folder/PROJECT%202/AI%20RESUME/ai-resume-analyzer/frontend/index.html]
