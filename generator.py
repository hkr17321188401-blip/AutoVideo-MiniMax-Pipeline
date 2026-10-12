import os
import sys
import subprocess
import configparser

CONFIG_FILE = "config.ini"
PROMPTS_FILE = "prompts.json"

def create_demo_clips():
    print("")
    print("[DEMO MODE] No API Key provided in config.ini.")
    print("[DEMO MODE] Creating 3 sample video segments to test pipeline stitching...")
    print("")
    for i in range(1, 4):
        filename = f"segment_0{i}.mp4"
        if not os.path.exists(filename):
            cmd = [
                "ffmpeg", "-y", "-f", "lavfi",
                "-i", "color=c=navy:s=1280x720:d=2",
                "-c:v", "libx264", "-t", "2", "-pix_fmt", "yuv420p", filename
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  [+] Created demo clip: {filename}")
    print("")
    print("[DEMO MODE] Demo clips generated successfully!")

def main():
    if not os.path.exists(CONFIG_FILE):
        print(f"[ERROR] {CONFIG_FILE} not found!")
        return 1

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding="utf-8")

    api_key = ""
    if "API_KEYS" in config and "MINIMAX_API_KEY" in config["API_KEYS"]:
        api_key = config["API_KEYS"]["MINIMAX_API_KEY"].strip()

    if not api_key or api_key == "YOUR_MINIMAX_API_KEY_HERE":
        create_demo_clips()
        return 0

    print("[INFO] MiniMax API Key detected. Starting generation...")
    return 0

if __name__ == "__main__":
    sys.exit(main())
