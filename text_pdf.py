import fitz
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import shutil

path = r"pdf-sample.pdf"
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
name1 = tokens_list[6]
name2 = tokens_list[5]

new_filename = date_today + '_' + name1 + '_' + name2 + '.pdf'


original = path
target = new_filename

shutil.copyfile(original, target)
