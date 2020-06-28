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

path = input('\nPaste the path of the PDFs you wish to rename: ') + '\\' # Paste the path to your files
path1 = path + '*.pdf' # create glob path that recognizes all PDFs

files = []


for file in glob.glob(path1):
    files.append(file) # Create list of PDFs to rename
  
list_of_dict = []
list_of_dict = [{} for i in range(0, len(files))] # Create list of dicts as per the number of files to rename

a = 0
b = 0
    
for file in files:
    
    doc = fitz.open(files[a]) # Display metadata of PDFs
    print ("\nnumber of pages: %i" % doc.pageCount)
    print(doc.metadata)
    print('\n')
    
    page = doc.loadPage(0) # Choose where the rename content is (usally first or second page)
    pagetext = page.getText("text")
    
    tokens = sent_tokenize(pagetext) # Create tokenized groups of words seperated by \n in the PDFs    
    textList = Text(tokens)
    tokens = [t.replace('\n', ', ') for t in tokens]
    tokens = str(tokens)
    tokens_list = tokens.split(",")
    tokens_list = [t.strip() for t in tokens_list]    
    
    for t, value in enumerate(tokens_list, 0): # Enumerate word groups and add to the dicts
        list_of_dict[b][t] = value 

    a += +1
    b += +1 
    
for dic in list_of_dict: # Display the enumerated groups of words to the user for file name selection  
    for k, v in dic.items():
        print(k, ' : ', v)
        
    

cn = input('\nType the number next to company name: ') # Select file name sections by number
cid = input('\nType the number next to company ID: ')    


company_name = []
company_id = []
date_today = [dt.date.today().strftime('%Y-%m-%d')]


for dic in list_of_dict: # Store file rename vales in lists
    company_name.append(dic[int(cn)])
    company_id.append(dic[int(cid)])
    

df = pd.DataFrame(list(zip(company_name, company_id, files)), # Create new file names
              columns=['company_name','company_id', 'old_file_names'])

df['date'] = str(pd.to_datetime('today').date())

df.columns=['company_name','company_id', 'old_file_names', 'date']

df['new_file_names'] = df['date'] + '_'  + df['company_name'] + '_' + df['company_id'] + '.pdf'

old_file_names = list(df['old_file_names'])

new_file_names = list(df['new_file_names'])


for o, n in zip(old_file_names, new_file_names): # Copy orignal files and rename copies as per user definitions
    shutil.copyfile(o, n)  

for o, n in zip(old_file_names, new_file_names): # Print what has been renamed to what
    print('\n ' + o + '    ---------->    ' + n)
