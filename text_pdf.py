import fitz
import nltk
from nltk.tokenize import word_tokenize
from nltk import Text

pdf_document = "pdf-sample.pdf"
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
print(doc.metadata)

page1 = doc.loadPage(0)
page1text = page1.getText("text")

tokens = word_tokenize(page1text)    
textList = Text(tokens)
page1text
