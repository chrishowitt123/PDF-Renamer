import fitz
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk import Text
import pandas as pd

pdf_document = "pdf-sample.pdf"
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

page1 = doc.loadPage(0)
page1text = page1.getText("text")

    
textList = Text(tokens)
list(page1text)
tokens = sent_tokenize(page1text)  
df = pd.DataFrame(tokens).to_csv('text.csv')
