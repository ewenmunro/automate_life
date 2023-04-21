import difflib
import pdfplumber
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red, black

# Open the first file and read its contents
with pdfplumber.open('file1.pdf') as pdf1:
    file1_contents = ""
    for page in pdf1.pages:
        file1_contents += page.extract_text()

# Open the second file and read its contents
with pdfplumber.open('file2.pdf') as pdf2:
    file2_contents = ""
    for page in pdf2.pages:
        file2_contents += page.extract_text()

# Use difflib to compare the two files and get the differences
differ = difflib.Differ()
differences = list(differ.compare(
    file1_contents.splitlines(), file2_contents.splitlines()))

# Create a new PDF file to store the differences
pdf_output = canvas.Canvas('diff.pdf')

# Set font size and color
pdf_output.setFontSize(20)
pdf_output.setFillColor(black)

# Print the differences to the new PDF file
x = 50
y = 750
for line in file1_contents.splitlines():
    pdf_output.drawString(x, y, 'File 1:')
    y -= 30
    pdf_output.setFontSize(14)
    pdf_output.drawString(x, y, 'Content:')
    y -= 20
    pdf_output.setFontSize(12)

    # Split the line into smaller chunks if it exceeds the page width
    words = line.split()
    line_chunks = []
    chunk = ''
    for word in words:
        word_width = pdf_output.stringWidth(word)
        if pdf_output.stringWidth(chunk + ' ' + word) > 500:
            line_chunks.append(chunk.strip())
            chunk = word
        else:
            chunk += ' ' + word
    line_chunks.append(chunk.strip())

    # Print each line chunk on a separate line
    for chunk in line_chunks:
        pdf_output.drawString(x, y, chunk)
        y -= 20

    y -= 10
    pdf_output.setFontSize(14)
    pdf_output.drawString(x, y, 'Differences:')
    y -= 20
    pdf_output.setFontSize(12)
    for word in difflib.ndiff(line.split(), file2_contents.splitlines()[file1_contents.splitlines().index(line)].split()):
        if word.startswith('-'):
            # If the word is in file1 but not in file2, print it in red
            pdf_output.setFillColor(red)
            word_width = pdf_output.stringWidth(word[2:])
            if x + word_width > 550:
                x = 50
                y -= 20
            pdf_output.drawString(x, y, f'-{word[2:]}')
            pdf_output.setFillColor('black')
            x += word_width + 10
        elif word.startswith('+'):
            # If the word is in file2 but not in file1, print it in red
            pdf_output.setFillColor(red)
            word_width = pdf_output.stringWidth(word[2:])
            if x + word_width > 550:
                x = 50
                y -= 20
            pdf_output.drawString(x, y, f'+{word[2:]}')
            pdf_output.setFillColor('black')
            x += word_width + 10
        else:
            # Otherwise, print the word as is
            word_width = pdf_output.stringWidth(word)
            if x + word_width > 550:
                x = 50
                y -= 20
            pdf_output.drawString(x, y, word)
            x += word_width + 5

x = 50
y -= 75
for line in file2_contents.splitlines():
    pdf_output.setFontSize(20)
    pdf_output.drawString(x, y, 'File 2:')
    y -= 30
    pdf_output.setFontSize(14)
    pdf_output.drawString(x, y, 'Content:')
    y -= 20
    pdf_output.setFontSize(12)

    # Split the line into smaller chunks if it exceeds the page width
    words = line.split()
    line_chunks = []
    chunk = ''
    for word in words:
        word_width = pdf_output.stringWidth(word)
        if pdf_output.stringWidth(chunk + ' ' + word) > 500:
            line_chunks.append(chunk.strip())
            chunk = word
        else:
            chunk += ' ' + word
    line_chunks.append(chunk.strip())

    # Print each line chunk on a separate line
    for chunk in line_chunks:
        pdf_output.drawString(x, y, chunk)
        y -= 20

    y -= 10
    pdf_output.setFontSize(14)
    pdf_output.drawString(x, y, 'Differences:')
    y -= 20
    pdf_output.setFontSize(12)
    for word in difflib.ndiff(line.split(), file1_contents.splitlines()[file2_contents.splitlines().index(line)].split()):
        if word.startswith('-'):
            # If the word is in file2 but not in file1, print it in red
            pdf_output.setFillColor(red)
            word_width = pdf_output.stringWidth(word[2:])
            if x + word_width > 550:
                x = 50
                y -= 20
            pdf_output.drawString(x, y, f'-{word[2:]}')
            pdf_output.setFillColor('black')
            x += word_width + 10
        elif word.startswith('+'):
            # If the word is in file1 but not in file2, print it in red
            pdf_output.setFillColor(red)
            word_width = pdf_output.stringWidth(word[2:])
            if x + word_width > 550:
                x = 50
                y -= 20
            pdf_output.drawString(x, y, f'+{word[2:]}')
            pdf_output.setFillColor('black')
            x += word_width + 10
        else:
            # Otherwise, print the word as is
            word_width = pdf_output.stringWidth(word)
            if x + word_width > 550:
                x = 50
                y -= 20
            pdf_output.drawString(x, y, word)
            x += word_width + 5

# Save the new PDF file
pdf_output.save()
