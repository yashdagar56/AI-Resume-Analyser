import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def analyze_resume(resume_text: str, job_description: str) -> dict:
    """
    Sends the resume text and job description to Gemini 1.5 flash for analysis.
    Returns the parsed JSON response.
    """
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_key_here":
        return {
            "error": "Gemini API key is missing or invalid. Please setup .env correctly."
        }

    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    prompt = f"""You are an expert ATS resume screener and career coach.

Resume Text:
{resume_text}

Job Description:
{job_description}

Analyze the resume against the job description and return ONLY a valid JSON object with NO markdown, no explanation, no extra text. The JSON must have exactly these keys:

{{
  "score": <integer 0-100>,
  "ats_verdict": "<Excellent | Good | Average | Poor>",
  "matched_keywords": ["keyword1", "keyword2", ...],
  "missing_keywords": ["keyword1", "keyword2", ...],
  "strengths": ["point1", "point2", ...],
  "weaknesses": ["point1", "point2", ...],
  "suggestions": ["suggestion1", "suggestion2", ...],
  "rewritten_bullets": ["improved bullet 1", "improved bullet 2", ...]
}}
"""
    
    try:
        # Dynamically find the best supported model for this specific API key
        valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        preferred = ['models/gemini-2.5-flash', 'models/gemini-2.0-flash', 'models/gemini-1.5-flash-latest', 'models/gemini-flash-latest']
        
        chosen_model = valid_models[0] if valid_models else 'gemini-pro'
        for pref in preferred:
            if pref in valid_models:
                chosen_model = pref
                break

        model = genai.GenerativeModel(chosen_model)
        
        try:
            response = model.generate_content(prompt)
        except Exception as api_e:
            raise Exception(f"Failed to generate content with {chosen_model}. API Error: {str(api_e)}")
        
        # Safely parse JSON response
        response_text = response.text.strip()
        
        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "", 1)
            if response_text.endswith("```"):
                response_text = response_text[:-3]
        elif response_text.startswith("```"):
            response_text = response_text.replace("```", "", 1)
            if response_text.endswith("```"):
                response_text = response_text[:-3]

        response_text = response_text.strip()
        
        try:
            data = json.loads(response_text)
            return data
        except json.JSONDecodeError:
            return {
                "error": "Failed to parse JSON",
                "raw_response": response_text
            }
    except Exception as e:
        return {
            "error": f"AI Analysis failed: {str(e)}"
        }
