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
path1 = path + '*.pdf' # Create glob path

files = []

for file in glob.glob(path1):
    files.append(file) # Create list of PDF paths
  

list_of_dict = []
list_of_dict = [{} for i in range(0, len(files))] # Create a list of dicts as per the length of the PDF files list

a = 0
b = 0
    
for file in files:
    
    doc = fitz.open(files[a])
    print ("\nnumber of pages: %i" % doc.pageCount)
    print(doc.metadata) # Print metadata for each PDF
    print('\n')
    print('\n')
    
    page = doc.loadPage(0)
    pagetext = page.getText("text") # Import text from chosen page that has the rename strings 
    
    tokens = sent_tokenize(pagetext)  # Tokenize text as list  
    textList = Text(tokens)
    tokens = [t.replace('\n', ', ') for t in tokens]
    tokens = str(tokens)
    tokens_list = tokens.split(",")
    tokens_list = [t.strip() for t in tokens_list]    
    
    for t, value in enumerate(tokens_list, 0): # Enumrrate each token in dicts (text from PDFs)
        list_of_dict[b][t] = value # Assign tokens as dict values
        
    for dic in list_of_dict:    
        for k, v in dic.items():
            print(k, ' : ', v)   # Print text in easy to read format for user to confirm when the strings for renaming are

    a += +1
    b += +1 
    

cn = input('\nType the number next to company name: ')
cid = input('\nType the number next to company ID: ')    

company_name = []
company_id = []
date_today = [dt.date.today().strftime('%Y-%m-%d')]

for dic in list_of_dict:
    company_name.append(dic[int(cn)]) # Create seperate lists for each part of new file name
    company_id.append(dic[int(cid)])

df = pd.DataFrame(list(zip(company_name, company_id, files)), # Create new file names on Pandas
              columns=['company_name','company_id', 'old_file_names'])

df['date'] = str(pd.to_datetime('today').date())

df.columns=['company_name','company_id', 'old_file_names', 'date']

df['new_file_names'] = df['date'] + '_'  + df['company_name'] + '_' + df['company_id'] + '.pdf'

old_file_names = list(df['old_file_names'])

new_file_names = list(df['new_file_names'])

for o, n in zip(old_file_names, new_file_names): # Copy old file as to still have the orignals after prjram termination
    shutil.copyfile(o, n)  

for o, n in zip(old, new):
    print('\n ' + o + '    ---------->    ' + n) # Tell user which files have been changed to what
