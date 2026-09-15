from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Unlimited Video Generator")


class VideoRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "Unlimited Video Generator is running!",
        "status": "success"
    }


@app.post("/generate")
def generate_video(request: VideoRequest):
    return {
        "message": "Video generation request received",
        "prompt": request.prompt,
        "status": "queued"
    }