import fitz
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import shutil



path = r"Proformas_0406181628.pdf"
doc = fitz.open(path)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

page = doc.loadPage(0)
pagetext = page.getText("text")

    
textList = Text(tokens)
tokens = sent_tokenize(pagetext)    
tokens = [t.replace('\n', ', ') for t in tokens]
tokens = str(tokens)
tokens_list = tokens.split(",")

tokens_list = [t.strip() for t in tokens_list]

tokens_list

date_today = datetime.today().strftime('%Y-%m-%d')

#company_name_index = tokens_list.index('Holísticos – Serviços')
#company_id_index = tokens_list.index('Código')

company_name = tokens_list[82]
company_id = tokens_list[22]

new_filename = date_today + '_' + company_name + '_' + company_id + '.pdf'


original = path
target = new_filename

shutil.copyfile(original, target)
