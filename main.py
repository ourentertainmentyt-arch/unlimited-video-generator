from fastapi import FastAPI
from pydantic import BaseModel

from services.video_service import generate_video

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
def create_video(request: VideoRequest):
    return generate_video(request.prompt)