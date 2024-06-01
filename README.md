# Cribs-Search
A project attempting to facilitate searching for a specific question on Cam Cribs by keywords.

Cam Cribs is a website hosted by engineering student(s) at the University of Cambridge which hosts papers and solutions to supervision questions sheets and past examinations. However; the files are PDF files viewed with Javascript and there exists no search functions for all files on the website, it was difficult to quickly find a paper by question and refer to its solution sheets.

## Table of contents:
- [First Attempt](#first-attempt)
- [Virtual Environment](#virtual-environment)

## First attempt

The first attempt is to scrape (download) all PDF files by year group and subjects using *request* and *BeautifulSoup*, extract all LaTeX expressions and texts using *regular expression* matching and *fitz*, finally index and search using *whoosh*'s index and query.

The attempt is broken down into **pdf_scraping.py**, **indexing.py** and **search.py**.

## Virtual Environment

A virtual environment (venv), cribsSearch, is used which has the following packages installed:
1. BeautifulSoup4
2. fitz
3. whoosh

The virtual environment is included for convenience in distribution, allowing users to activate the virtual environment directly and run the Python files with the necessary packages.