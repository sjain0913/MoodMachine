import os
import subprocess

# Get into the filesystem
for root, dirs, files in os.walk("./model/RAVDESS", topdown = False):
    for file in files:
        if file.endswith('.mp4'):
            print(root)
            print(file)
            conversionCommand = "ffmpeg -i ./" + root[1:] + "/" + file + " " + "-ab 160k -ac 2 -ar 44100 -vn " + "./model/CONVERTED_RAVDESS/" + file[:-3] + "wav"
            
            try:
                subprocess.call(conversionCommand, shell = True)
                
            except ValueError:
                print(ValueError)
                continue