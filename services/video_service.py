from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_video(prompt: str):
    video_path = OUTPUT_DIR / "generated_video.mp4"

    return {
        "message": "Video generation request received",
        "prompt": prompt,
        "status": "queued",
        "output_path": str(video_path),
    }