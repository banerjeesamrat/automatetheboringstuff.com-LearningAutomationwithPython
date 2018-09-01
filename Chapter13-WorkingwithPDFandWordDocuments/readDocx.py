#! /usr/bin/python3.5

import docx

def getText(filename):
    doc=docx.Document(filename)
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(' '+para.text)
    return '\n'.join(fullText)
