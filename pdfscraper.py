# -*- coding: utf-8 -*-
"""
ISIS TEXT SCRAPER
"""

import PyPDF2 as pdf
import codecs

files = []
for i in xrange(13):
    files += [str(i+1) + '.pdf']

isistext = {}

for f in files:
    read = pdf.PdfFileReader(open(f, 'rb'))
    add = ''    
    print(f)
    for p in xrange(read.numPages):
        add += read.getPage(p).extractText().replace('\n', '')
        #this isn't consistently getting all the text....
    isistext[f] = add
        
with codecs.open('isistext.txt', encoding='utf-8', mode = 'w') as w:
    for f in files:
        w.write('\n\n' + f.upper() + '\n\n')
        w.write(isistext[f])
