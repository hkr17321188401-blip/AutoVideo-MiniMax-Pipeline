import os
import re
import subprocess
import sys

OUTPUT_FILE = "final_stitched_video.mp4"
CONCAT_FILE = "concat_list.txt"
EXCLUDED_FILES = {OUTPUT_FILE, "output.mp4"}

def natural_key(filename):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r"(\d+)", filename)]

def main():
    videos = [
        name for name in os.listdir(".")
        if name.lower().endswith(".mp4") and name not in EXCLUDED_FILES
        and os.path.isfile(name)
    ]
    videos.sort(key=natural_key)

    if not videos:
        print("[INFO] No MP4 video segments found in the current directory to stitch.")
        return 0

    print(f"[INFO] Found {len(videos)} video segment(s):")
    for video in videos:
        print(f"  - {video}")

    try:
        with open(CONCAT_FILE, "w", encoding="utf-8", newline="\n") as list_file:
            for video in videos:
                escaped_name = video.replace("'", "'\\''")
                list_file.write(f"file '{escaped_name}'\n")

        command = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", CONCAT_FILE, "-c", "copy", OUTPUT_FILE,
        ]
        result = subprocess.run(command, check=False)
        if result.returncode != 0:
            print("[INFO] Stream copy failed; retrying with video and audio re-encoding.")
            fallback_command = [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0",
                "-i", CONCAT_FILE, "-c:v", "libx264", "-c:a", "aac", OUTPUT_FILE,
            ]
            result = subprocess.run(fallback_command, check=False)

        if result.returncode != 0:
            print("[ERROR] FFmpeg could not stitch the video segments.", file=sys.stderr)
            return result.returncode

        print(f"[SUCCESS] Stitched video saved as {OUTPUT_FILE}")
        return 0
    except OSError as error:
        print(f"[ERROR] Unable to run FFmpeg or access the required files: {error}", file=sys.stderr)
        return 1
    finally:
        if os.path.exists(CONCAT_FILE):
            os.remove(CONCAT_FILE)

if __name__ == "__main__":
    sys.exit(main())
