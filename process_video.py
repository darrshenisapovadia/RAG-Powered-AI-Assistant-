#Converts the videos to mp3
import os
import subprocess
files =os.listdir("videos")
print(files)

for f in files:
    print(f)
    tutorial_number = f.split(" [")[0].split(" #")[1]
    print(tutorial_number)
    file_name = f.split(" | ")[0]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{f}", f"audios/{tutorial_number}_{file_name}.mp3"])