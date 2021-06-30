# -*- coding: utf-8 -*-
######################################################################
#  Open soruce OCR 기능 구현 
#  1. Python Tesseract 
#    > pytesseract
#     - Document : https://github.com/madmaze/pytesseract
######################################################################
from pytesseract import *
from PIL import Image









######################################################################
fname = "C:\\Mydata_correct\\correct_root\\K-007.png"
fwname = "C:\\Mydata_correct\\correct_root\\K-007_gray.png"

ch_fname = "C:\\Mydata\\svg2png\\0.png"
ch_fwname = "C:\\Mydata_correct\\correct_root\\0.png"

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 

img = Image.open( ch_fname ) # Image to String
text = pytesseract.image_to_string(img,lang='Kor') 

print (text)
