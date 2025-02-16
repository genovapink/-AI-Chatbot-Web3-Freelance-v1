from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load API Key dari environment variable atau file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Input Data
class FreelancerData(BaseModel):
    skills: list[str]
    experience: str

class JobData(BaseModel):
    description: str

class ChatData(BaseModel):
    messages: list[str]

# AI Job Matcher 
@app.post("/match_jobs")
def match_jobs(freelancer: FreelancerData):
    prompt = f"Berikan rekomendasi pekerjaan berdasarkan data platform untuk freelancer dengan skill {', '.join(freelancer.skills)} dan pengalaman {freelancer.experience}. Jangan hubungkan langsung dengan klien, hanya sebagai notifikasi."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return {"recommended_jobs": response["choices"][0]["message"]["content"]}

# AI Scam Detector
@app.post("/detect_scam")
def detect_scam(job: JobData):
    prompt = f"Analisis deskripsi pekerjaan ini untuk potensi penipuan: {job.description}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return {"scam_analysis": response["choices"][0]["message"]["content"]}

# AI Resume Builder
@app.post("/generate_resume")
def generate_resume(freelancer: FreelancerData):
    prompt = f"Buatkan resume profesional untuk freelancer dengan skill {', '.join(freelancer.skills)} dan pengalaman {freelancer.experience}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return {"generated_resume": response["choices"][0]["message"]["content"]}

# Chatbot UI Placeholder
@app.get("/chatbot_ui")
def chatbot_ui():
    return {
        "position": "bottom-left",
        "icon": "soft-blue-robot.png",
        "window_size": "medium",
        "behavior": "toggle-on-click",
        "close_on_outside_click": True
    }

# Starting Application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
