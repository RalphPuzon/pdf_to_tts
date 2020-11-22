#pdf to audiobook converter.

"""
turn a pdf of text into an audiobook
code courtesy of this video:
https://www.youtube.com/watch?v=xHyhVIYlFrI&list=LL&index=2&ab_channel=ComputerScience
"""

# IMPORTS:
import pyttsx3
import pdfplumber
import PyPDF2

# Fetch file location:
file = "./input_pdfs/raven.pdf"

# Instantiate pdf as an object:
PDFobj = open(file, 'rb')             #read as bytes

# Make reader object:
reader = PyPDF2.PdfFileReader(PDFobj)

# Fetch number of pages
num_pages = reader.numPages

# Create pdfPlumber object:
with pdfplumber.open(file) as pdf:    # open the pdf
	for i in range(num_pages):        # iterate through pages
		page = pdf.pages[i]           # focus on current page
		text = page.extract_text()    # extract text
		print(text)                   # print text so we can inspect
		voice = pyttsx3.init()        # instantiate voice
		voice.say(text)               # voice speak
		voice.runAndWait()            # run voice

