import PyPDF2 as pdf
import re
import nltk
from nltk.corpus import stopwords

def extract_text_from_pdf(file):
    pdf_file = pdf.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_file.pages)):
        page = pdf_file.pages[page_num]
        text += page.extract_text()
    return clean_text(text)

def clean_text(text):
    # Compile patterns for URLs and emails to speed up the cleaning process
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Remove URLs
    clean_text = url_pattern.sub('', text)

    # Remove emails
    clean_text = email_pattern.sub('', clean_text)

    # Remove special characters (keeping only words & whitespace)
    clean_text = re.sub(r'[^\w\s]', '', clean_text)

    # Remove stop words by filtering the split words of the text
    stop_words = set(stopwords.words('english'))
    clean_text = ' '.join(word for word in clean_text.split() if word.lower() not in stop_words)

    return clean_text
