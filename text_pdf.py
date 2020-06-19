import fitz
import glob 
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import shutil
import datetime as dt


path = r'C:\Users\chris\Desktop\pdf' #input('\nPaste the location of the files you wish to rename: ')
path = path + '\*.pdf'

files = []

for file in glob.glob(path):
    files.append(file)

for file in files:
    
    doc = fitz.open(file)
    print ("number of pages: %i" % doc.pageCount)
    print(doc.metadata)

    page = doc.loadPage(0)
    pagetext = page.getText("text")

    
    tokens = sent_tokenize(pagetext)    
    textList = Text(tokens)
    tokens = [t.replace('\n', ', ') for t in tokens]
    tokens = str(tokens)
    tokens_list = tokens.split(",")

    tokens_list = [t.strip() for t in tokens_list]

    for t, value in enumerate(tokens_list, 1):
        print(t, value)

    date_today = dt.date.today().strftime('%Y-%m-%d')
    
#company_name_index = tokens_list.index('Holísticos – Serviços')
#company_id_index = tokens_list.index('Código')

    company_name = tokens_list[82]
    company_id = tokens_list[22]

    new_filename = date_today + '_' + company_name + '_' + company_id + '.pdf'


    original = file
    target = new_filename

    shutil.copyfile(original, target)
