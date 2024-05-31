import requests
from bs4 import BeautifulSoup
import fitz
import os
import re
from whoosh.fields import Schema, TEXT, ID
from whoosh import index

"""
# Test code for scraping all IB example papers
ib_example = {
    "subjects": ["mechanics", "structures", "materials", "thermofluids", "electrical", "information", "maths"],
    "papers": [4, 5, 5, 6, 7, 9, 8]
}

master_url = "https://cribs-static.netlify.app/IB/examples"
save_dir = "Sheets/IB/example"

for i in range(0,len(ib_example["subjects"])):
    subject_url = "/".join([master_url, ib_example["subjects"][i]])
    for j in range(1,ib_example["papers"][i] + 1):
        paper_url = "/EP".join([subject_url, str(j).rjust(2,"0")]) + ".pdf"

        response = requests.get(paper_url)
        if not (response.status_code == 404):
            pdf_name = os.path.join(save_dir, "-".join(paper_url.split('/')[-4:]))
            with open(pdf_name, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded {pdf_name}")
"""

"""
# Test code for scraping all IB tripos papers
ib_example = {
    "subjects": ["2P1", "2P2", "2P3", "2P4", "2P5", "2P6", "2P7"],
}

master_url = "https://cribs-static.netlify.app/IB/tripos"
save_dir = "Sheets/IB/tripos"

for i in range(0,len(ib_example["subjects"])):
    subject_url = "/".join([master_url, ib_example["subjects"][i]])
    for j in range(1,29):
        year = 1995 + j
        paper_url = "/QP_".join([subject_url, str(year)]) + ".pdf"

        response = requests.get(paper_url)
        if not (response.status_code == 404):
            pdf_name = os.path.join(save_dir, "-".join(paper_url.split('/')[-4:]))
            with open(pdf_name, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded {pdf_name}")
"""

"""
# Test code for downloading a single PDF and extracting its content, which is stored in a txt file Output.txt
paper_url="https://cribs-static.netlify.app/IB/tripos/2P2/QP_2012.pdf"
save_dir="Sheets/IB/tripos"
response = requests.get(paper_url)
if not (response.status_code == 404):
    pdf_name = os.path.join(save_dir, "-".join(paper_url.split('/')[-4:]))
    with open(pdf_name, 'wb') as pdf_file:
        pdf_file.write(response.content)
    print(f"Downloaded {pdf_name}")
    print(response.status_code)

# Extraction code here returns a single string of text, which is stored in a txt file (instead of returning a dictionary)

def extract_text_with_latex(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    latex_pattern = re.compile(r'\$.*?\$|\$\$.*?\$\$')

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        page_text = page.get_text("text")
        text += page_text

        # Extract LaTeX equations
        latex_matches = latex_pattern.findall(page_text)
        for match in latex_matches:
            text += f" {match} "

    return text

def extract_text_from_pdfs(pdf_dir):
    pdf_texts = {}
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            text = extract_text_with_latex(pdf_path)
            #pdf_texts[pdf_file] = text
    #return pdf_texts
    return text

pdf_dir = "Sheets/IB/tripos"
pdf_texts = extract_text_from_pdfs(pdf_dir) + "IB 1B 2P2 Structures"

text_file = open("Output.txt", "w", encoding="utf-8")
text_file.write(pdf_texts)
text_file.close()
"""

ib_example = {
    #"subjects": ["2P1", "2P2", "2P3", "2P4", "2P5", "2P6", "2P7"],
    "subjects": ["2P1"],
}

master_url = "https://cribs-static.netlify.app/IB/tripos"
save_dir = "Sheets/IB/tripos"

for i in range(0,len(ib_example["subjects"])):
    subject_url = "/".join([master_url, ib_example["subjects"][i]])
    for j in range(1,29):
        year = 1995 + j
        paper_url = "/QP_".join([subject_url, str(year)]) + ".pdf"

        response = requests.get(paper_url)
        if not (response.status_code == 404):
            pdf_name = os.path.join(save_dir, " ".join(paper_url.split('/')[-4:]).replace("_", " "))
            with open(pdf_name, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"Downloaded {pdf_name}")

print("All files downloaded")

def check_english(letter):
    ascii_value = ord(letter)
    return (ascii_value >= 32 and ascii_value <= 126)

def extract_text_with_latex(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    latex_pattern = re.compile(r'\$.*?\$|\$\$.*?\$\$')

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        page_text = page.get_text("text")
        text += page_text

        # Extract LaTeX equations
        latex_matches = latex_pattern.findall(page_text)
        for match in latex_matches:
            text += f" {match} ".replace("\"", " ").replace("\'", " ")

        output = ""
        for letter in text:
            if check_english(letter):
                output += letter

    return output

def extract_text_from_pdfs(pdf_dir):
    pdf_texts = {}
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            text = extract_text_with_latex(pdf_path)
            pdf_texts[pdf_file] = text.replace("\n", " ")
    return pdf_texts

pdf_dir = "Sheets/IB/tripos"

pdf_texts = extract_text_from_pdfs(pdf_dir)
print("All texts extracted")
# print(pdf_texts)
# print(type(pdf_texts))

for file in os.listdir(pdf_dir):
    os.remove(os.path.join(pdf_dir, file))

print("All files removed")