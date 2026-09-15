from pathlib import Path

from moviepy import ColorClip, TextClip, CompositeVideoClip


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_video(prompt: str):
    video_path = OUTPUT_DIR / "generated_video.mp4"

    background = ColorClip(
        size=(1280, 720),
        color=(0, 0, 0),
        duration=5,
    )

    text = TextClip(
        text=prompt,
        font_size=50,
        color="white",
        size=(1100, 600),
        method="caption",
    ).with_duration(5).with_position("center")

    video = CompositeVideoClip([background, text])

    video.write_videofile(
        str(video_path),
        fps=24,
        codec="libx264",
        audio=False,
    )

    video.close()
    background.close()

    return {
        "message": "Video generated successfully",
        "prompt": prompt,
        "status": "completed",
        "output_path": str(video_path),
    }