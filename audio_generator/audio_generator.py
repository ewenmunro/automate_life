import ffmpeg
from gtts import gTTS
import PyPDF2
import tempfile
import os

# Path to PDF file
pdf_path = 'text.pdf'

# Read PDF file and extract text
pdf_file = open(pdf_path, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

# Convert text to speech using Google Text-to-Speech with British English accent
tts = gTTS(text, lang='en', tld='co.uk')

# Save speech to temporary file
temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
temp_file.close()
tts.save(temp_file.name)

# Convert speech to WAV using ffmpeg
output_path = 'output.wav'
ffmpeg.input(temp_file.name).output(output_path).run()

# Delete temporary file
os.remove(temp_file.name)
