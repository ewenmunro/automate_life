import re
import moviepy.editor as mp
import speech_recognition as sr
from datetime import timedelta
import os

# Path to the video file
video_path = ''

# Load the video file and extract the audio track
video = mp.VideoFileClip(video_path)
audio = video.audio.to_audiofile('temp.wav')

# Transcribe the audio using speech_recognition
r = sr.Recognizer()
with sr.AudioFile('temp.wav') as source:
    audio = r.record(source)
transcription = r.recognize_google(audio)

# Parse the transcription and generate subtitles
subtitles = []
lines = transcription.splitlines()
for i, line in enumerate(lines):
    start_time = i * 5  # 5 seconds per subtitle
    end_time = start_time + 5
    text = re.sub(r'\s+', ' ', line.strip())
    subtitles.append((i+1, start_time, end_time, text))

# Generate the SRT file
with open('subtitles.srt', 'w', encoding='utf-8') as f:
    for sub in subtitles:
        start_time = str(timedelta(seconds=sub[1]))
        end_time = str(timedelta(seconds=sub[2]))
        text_with_spaces = ' '.join(sub[3].split())
        f.write(
            '{}\n{} --> {}\n{}\n\n'.format(sub[0], start_time, end_time, text_with_spaces))

# Clean up temporary files
os.remove('temp.wav')
