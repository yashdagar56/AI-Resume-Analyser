---
title: AI Resume Backend
emoji: 🚀
colorFrom: blue
colorTo: blue
sdk: docker
pinned: false
---

# AI Resume Analyser 🚀

👉 **[Demo](https://ai-resume-frontend.pages.dev/)** 👈

I built this **AI Resume Analyser** to bridge the gap between job seekers and Applicant Tracking Systems (ATS). It's a full-stack solution that evaluates resumes against specific job descriptions using Google's Gemini AI, providing the kind of feedback normally reserved for professional recruiters.

## Why I Built This
Applying for jobs can feel like shouting into a void. I wanted to create a tool that gives instant, actionable feedback—not just a score, but actual AI-rewritten bullet points and keyword analysis to help people actually get interviews.

## The Tech Stack
- **Frontend**: Crafted with clean HTML5 and Vanilla JavaScript, leveraging Tailwind CSS for a premium, responsive look.
- **Backend**: Powering the logic is FastAPI, which handles the file uploads and communication with the AI.
- **AI Intelligence**: I integrated Google Gemini 1.5 Flash to provide fast and accurate ATS breakdowns.
- **Report Generation**: I used ReportLab to generate custom, branded PDF reports that users can download.

## Features I've Implemented
- **Premium Upload Experience**: A custom drag-and-drop interface that locks once a file is uploaded to prevent errors.
- **Real-time ATS Scoring**: Instant calculation of how well a resume matches a job description.
- **Keyword Analysis**: Visual breakdown of matched and missing keywords.
- **AI Bullet Point Rewriting**: The AI suggests better ways to phrase weak parts of a resume.
- **Branded PDF Downloads**: Detailed reports generated on the fly.

## How to Run My Project

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **API Configuration**:
   The project uses a `.env` file for the Gemini API Key. I've structured it like this:
   ```env
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

3. **Start the Backend**:
   ```bash
   uvicorn backend.main:app --reload
   ```

4. **Launch the Frontend**:
   Simply open `frontend/index.html` in any browser to experience the app.

## Project Structure
```
ai-resume-analyzer/
├── backend/
│   ├── main.py              # Application routes & middleware
│   ├── parser.py            # Logic for PDF text extraction
│   ├── analyzer.py          # Gemini AI prompt engineering
│   ├── report.py            # PDF generation logic
├── frontend/
│   ├── index.html           # Main experience & upload UI
│   ├── result.html          # Dynamic analysis results
│   └── assets/
│       └── style.css        # Custom premium styling & animations
├── .env                     # API Credentials
├── .gitignore               # Keeps the repo clean
└── README.md                # That's what you're reading!
```

---
*Created with passion by Yash Dagar*
