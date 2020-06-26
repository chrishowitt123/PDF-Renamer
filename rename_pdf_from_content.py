import fitz
import glob 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import shutil
import datetime as dt
import pandas as pd
from os import listdir
from os.path import isfile, join
from pathlib import Path


path = input('\nPaste the path of the PDFs you wish to rename: ') + '\\'
path1 = path + '*.pdf'

files = []


for file in glob.glob(path1):
    files.append(file)
  
list_of_dict = []
list_of_dict = [{} for i in range(0, len(files))]

a = 0
b = 0
    
for file in files:
    
    doc = fitz.open(files[a])
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
        list_of_dict[b][t] = value 

    a += +1
    b += +1 
    
for dic in list_of_dict:    
    for k, v in dic.items():
        print(k, ' : ', v)
        
    

cn = input('\nType the number next to company name: ')
cid = input('\nType the number next to company ID: ')    


company_name = []
company_id = []
date_today = [dt.date.today().strftime('%Y-%m-%d')]


for dic in list_of_dict:
    company_name.append(dic[int(cn)])
    company_id.append(dic[int(cid)])
    

df = pd.DataFrame(list(zip(company_name, company_id, files)),
              columns=['company_name','company_id', 'old_file_names'])

df['date'] = str(pd.to_datetime('today').date())

df.columns=['company_name','company_id', 'old_file_names', 'date']

df['new_file_names'] = df['date'] + '_'  + df['company_name'] + '_' + df['company_id'] + '.pdf'

old_file_names = list(df['old_file_names'])

new_file_names = list(df['new_file_names'])


for o, n in zip(old_file_names, new_file_names):
    shutil.copyfile(o, n)  

for o, n in zip(old_file_names, new_file_names):
    print('\n ' + o + '    ---------->    ' + n)
