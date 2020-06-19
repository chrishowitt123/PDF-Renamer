import fitz
import glob 
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import shutil
import datetime as dt


path = input('\nPaste the path of the PDFs you wish to rename: ')
path = path + '\*.pdf'

files = []

for file in glob.glob(path):
    files.append(file)

for file in files:
    
    doc = fitz.open(file)
    print ("\nnumber of pages: %i" % doc.pageCount)
    print(doc.metadata)
    print('\n')

    page = doc.loadPage(0)
    pagetext = page.getText("text")

    
    tokens = sent_tokenize(pagetext)    
    textList = Text(tokens)
    tokens = [t.replace('\n', ', ') for t in tokens]
    tokens = str(tokens)
    tokens_list = tokens.split(",")

    tokens_list = [t.strip() for t in tokens_list]

    for t, value in enumerate(tokens_list, 0):
        print(t, value)  

cn = input('\nType the number next to company name: ')
cid = input('\nType the number next to company ID: ')


for file in files:
    
    company_name = tokens_list[int(cn)]
    company_id = tokens_list[int(cid)]
    date_today = dt.date.today().strftime('%Y-%m-%d')

    new_filename = date_today + '_' + company_name.title() + '_' + company_id + '.pdf'


    original = file
    target = new_filename

    shutil.copyfile(original, target)
