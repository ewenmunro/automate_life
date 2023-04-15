from moviepy.editor import *

audio_file = ""
image_file = ".png"
video_file = "output.mov"

# Load audio file
audio_clip = AudioFileClip(audio_file)

# Load image file
image_clip = ImageClip(image_file)

# Set the duration of the video to the length of the audio clip
video_clip = image_clip.set_duration(audio_clip.duration)

# Resize the video clip to match the size of the image clip
video_clip = video_clip.resize(image_clip.size)

# Add audio to the video
video_clip = video_clip.set_audio(audio_clip)

# Write the video to a file
video_clip.write_videofile(video_file, fps=24, codec="prores", audio_codec="aac", ffmpeg_params=["-pix_fmt", "yuv420p"])
