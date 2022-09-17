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

# paste path to files
path = input('\nPaste the path of the PDFs you wish to rename: ') + '\\'

# create glob path that recognizes all PDFs
path1 = path + '*.pdf' 

files = []

# append file names to files list
for file in glob.glob(path1):
    files.append(file)
    
# create list of dictionaries relative to the number of files to rename
list_of_dict = []
list_of_dict = [{} for i in range(0, len(files))]

a = 0
b = 0
    
for file in files:
    doc = fitz.open(files[a])
    # display metadata of PDFs
    print ("\nnumber of pages: %i" % doc.pageCount)
    print(doc.metadata)
    print('\n')
    
    # choose where the rename content is (usually first or second page)
    page = doc.loadPage(0) 
    pagetext = page.getText("text")
    
    # create tokenized word groups by PDF
    tokens = sent_tokenize(pagetext)  
    textList = Text(tokens)
    tokens = [t.replace('\n', ', ') for t in tokens]
    tokens = str(tokens)
    tokens_list = tokens.split(",")
    tokens_list = [t.strip() for t in tokens_list]    
    
    # enumerate word groups and add to list_of_dict
    for t, value in enumerate(tokens_list, 0): 
        list_of_dict[b][t] = value 

    a += +1
    b += +1 
    
# display the enumerated word groups to the user for file name selection      
for dic in list_of_dict: 
    for k, v in dic.items():
        print(k, ' : ', v)
    
# select file name sections by number
cn = input('\nType the number next to company name: ') 
cid = input('\nType the number next to company ID: ')    

company_name = []
company_id = []
date_today = [dt.date.today().strftime('%Y-%m-%d')]

# store file and rename vales in lists
for dic in list_of_dict: 
    company_name.append(dic[int(cn)])
    company_id.append(dic[int(cid)])

# create new file names
df = pd.DataFrame(list(zip(company_name, company_id, files)), 
              columns=['company_name','company_id', 'old_file_names'])

df['date'] = str(pd.to_datetime('today').date())
df.columns=['company_name','company_id', 'old_file_names', 'date']
df['new_file_names'] = df['date'] + '_'  + df['company_name'] + '_' + df['company_id'] + '.pdf'

old_file_names = list(df['old_file_names'])
new_file_names = list(df['new_file_names'])

# copy original files and rename copies as per user definitions
for o, n in zip(old_file_names, new_file_names): 
    shutil.copyfile(o, n)  

# print what has been renamed to what
for o, n in zip(old_file_names, new_file_names): 
    print('\n ' + o + '    ---------->    ' + n)
