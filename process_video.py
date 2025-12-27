# Converts videos from the 'videos' folder into MP3 audio files using FFmpeg
import os
import subprocess

# Read all video files from videos directory
files = os.listdir("videos")
print(files)

# Loop through each video file and convert it to mp3
for f in files:
    print(f)

    # Extract tutorial number from the filename
    tutorial_number = f.split(" [")[0].split(" #")[1]
    print(tutorial_number)

    # Extract readable file title
    file_name = f.split(" | ")[0]
    print(tutorial_number, file_name)

    # Run FFmpeg to convert video to mp3
    subprocess.run(["ffmpeg", "-i", f"videos/{f}", f"audios/{tutorial_number}_{file_name}.mp3"])
