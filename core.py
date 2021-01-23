#image to pdf maker

from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()

#list with filenames of the images


imageList = []
with os.scandir("images/chapter2cables/") as entries:
    for entry in entries:
        imageList.append(entry.path) 
        
#imageList.sort()
#print(imageList)

for image in imageList:
    pdf.add_page()
    #nned to figure out how to auto fit with diffrent image sizes
    pdf.image(image, x=None, y=None, w=200, h=0)
pdf.output("x.pdf", "F")    
