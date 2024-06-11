import speech_recognition as sr
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# create a recognizer object
r = sr.Recognizer()

# open the audio file using the recognizer
with sr.AudioFile('.wav') as source:
    audio = r.record(source)

# use the recognizer to transcribe the audio to text
text = r.recognize_google(audio)

# create a PDF file
pdf_file = canvas.Canvas('audio_to_text.pdf', pagesize=letter)

# define the font and font size
font_name = 'Times-Roman'
font_size = 14

# set the font
pdf_file.setFont(font_name, font_size)

# calculate the height of each line
line_height = pdf_file._leading

# initialize the x and y coordinates
x, y = inch, inch*10

# add space at the top of the page
pdf_file.drawString(x, y, " " * 10)

# split the text into words
words = text.split()

# write the words to the PDF file
for word in words:
    # if the word goes beyond the page, start a new line
    if x + pdf_file.stringWidth(word, fontName=font_name, fontSize=font_size) > letter[0]-inch:
        x = inch
        y -= line_height
        # if the line goes beyond the page, start a new page
        if y - line_height < inch:
            pdf_file.showPage()
            y = inch*10
        pdf_file.drawString(x, y, word, charSpace=-1)
        x += pdf_file.stringWidth(word + ' ',
                                  fontName=font_name, fontSize=font_size)
    else:
        pdf_file.drawString(x, y, word, charSpace=-1)
        x += pdf_file.stringWidth(word + ' ',
                                  fontName=font_name, fontSize=font_size)

# save the PDF file
pdf_file.save()
