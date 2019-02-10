from tkinter import Tk,Frame,Menu
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter as tk
#from winsound import *
# platform
#os = platform.system()

class simpul():
    '''membuat kelas simpul'''
    def __init__(self, data=None):
        self.data = data
        self.link = None

class _Gui(Frame):
    '''Second Gui dari 24 Solver by : Putu - Bram - Valent'''
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.UI()
        self.list = None
        #membuat main canvas
        #self.canvas = Canvas(parent, background="white")
        #self.frame = Frame(self.canvas, background="blue")
    #gui
    def UI(self):
        self.parent.title("24 Solver dengan Algoritma Greedy")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar, bg="green")

        #buat button
        self._btnExit = Button(self.parent, text="EXIT", relief=RIDGE, bd = 5,bg = 'red', fg='black',command=self.onExit)
        self._btnExit.grid(column=2,row=0,columnspan=2,rowspan=2)
        
        self._btnImport = Button(self.parent, text="IMPORT", relief=RIDGE, bd=5,bg='red', fg='black', command=self.onImport)
        self._btnImport.grid(column=0, row=0, columnspan=2, rowspan=2)
    
        self._btnShow = Button(self.parent, text="SHOW CARD",relief=RIDGE, bd=5, bg='red',fg='black')
        self._btnShow.grid(column=0,row=2, columnspan=2, rowspan=2)

    #import file
    def onImport(self):
        try:
            tipeFile = fd.askopenfilename(filetypes = (("TEXT files","*.txt"),("All files","*.*")))
            openFile = open(tipeFile)
            openFile.readline()
            cardData = openFile.readlines()

            cardDataInt = []
            for i in range (len(cardData)):
                cardDataInt.append(int(cardData[i]))
            print(cardDataInt)

            mb.showinfo("Notification!","Import Succeed")
            openFile.close()
            self._showList = self.list
        except IOError:
            mb.showwarning("Warning!","Import canceled")
        except:
            mb.showwarning("Warning!","File doesn't match")

    #Exit program        
    def onExit(self):
        if mb.askyesno("Warning!", "Are you sure to exit?"):
            self.parent.destroy()
        else:
            mb.showinfo("Notification!","Exit canceled")

if __name__ =='__main__':
    root = Tk()
    root.geometry("600x400")
    root.resizable(False,False)
    app = _Gui(root)
    root.mainloop()