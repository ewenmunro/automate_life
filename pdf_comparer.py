import difflib
from PyPDF2 import PdfReader

# Open the first file and read its contents
with open('file1.pdf', 'rb') as file1:
    pdf_reader = PdfReader(file1)
    file1_contents = ""
    for page in pdf_reader.pages:
        file1_contents += page.extract_text()

# Open the second file and read its contents
with open('file2.pdf', 'rb') as file2:
    pdf_reader = PdfReader(file2)
    file2_contents = ""
    for page in pdf_reader.pages:
        file2_contents += page.extract_text()

# Use difflib to compare the two files and get the differences
differ = difflib.Differ()
differences = list(differ.compare(
    file1_contents.splitlines(), file2_contents.splitlines()))

# Print the differences
for line in differences:
    if line.startswith('- '):
        # If the line starts with '-' (i.e., it's in file1 but not in file2),
        # print it in red
        print('\033[31m{}\033[0m'.format(line))
    else:
        # Otherwise, print the line as is
        print(line)
