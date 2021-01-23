from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from fpdf import FPDF
from threading import *
import webbrowser
from tkinter import * 
from tkinter.ttk import *
import os

pdf = FPDF()
root = Tk()
root.eval('tk::PlaceWindow . center')

fileListBox = Listbox(root, width=75)

fileListBox.grid(row=1, column=0)
imageList = [] 

def openFolder():
    
    with os.scandir(selection) as entries:   
        for entry in entries:
            imageList.append(entry.path) 

    for i in imageList:        
        fileListBox.insert(END, i)        

selection = filedialog.askdirectory()
openFolder()

def threadOpen():
    print("thread 1")
    t1 = Thread(target=openFolder)
    t1.start()

def makePdf():
    pro = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    pro.grid(row=3, column=0)
    for image in imageList:
        pdf.add_page()
        #nned to figure out how to auto fit with diffrent image sizes
        pdf.image(image, x=None, y=None, w=200, h=0)
        pro['value'] += 3
    pdf.output("x.pdf")  
    print("file made")
    webbrowser.open_new(r'x.pdf')
    root.quit()

def threadMakePdf():
    print("thread 2")
    t2 = Thread(target=makePdf)
    t2.start()

btnOpenFolder = Button(root, text="Open Folder")
btnOpenFolder.grid(row=0, column=0)

btnCreatePdf = Button(root, text="Make Pdf", command=threadMakePdf)
btnCreatePdf.grid(row=4, column=0)

root.mainloop()