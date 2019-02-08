from tkinter import*
import tkinter.messagebox
import math

listOfBool = []     #Array untuk menyimpan boolean dari setiap elemen   
chosenCard = []     #Array untuk menyimpan kartu yang dipilih


for i in range (52):
    listOfBool.insert(i, False)

def updatePic(pic,column,row): #Masih Belom Bener
    if (column == 1):
        if (row == 1):
            pic.config(image = photodA)
        elif (row == 2):
            pic.config(image = photocA)
        elif (row == 3):
            pic.config(image = photohA)
        else :
            pic.config(image = photosA)
    elif (column == 2):
        if (row == 1):
            pic.config(image = photod2)
        elif (row == 2):
            pic.config(image = photoc2)
        elif (row == 3):
            pic.config(image = photoh2)
        else :
            pic.config(image = photos2)
    elif (column == 3):
        if (row == 1):
            pic.config(image = photod3)
        elif (row == 2):
            pic.config(image = photoc3)
        elif (row == 3):
            pic.config(image = photoh3)
        else :
            pic.config(image = photos3)
    elif (column == 4):
        if (row == 1):
            pic.config(image = photod4)
        elif (row == 2):
            pic.config(image = photoc4)
        elif (row == 3):
            pic.config(image = photoh4)
        else :
            pic.config(image = photos4)
    elif (column == 5):
        if (row == 1):
            pic.config(image = photod5)
        elif (row == 2):
            pic.config(image = photoc5)
        elif (row == 3):
            pic.config(image = photoh5)
        else :
            pic.config(image = photos5)
    elif (column == 6):
        if (row == 1):
            pic.config(image = photod6)
        elif (row == 2):
            pic.config(image = photoc6)
        elif (row == 3):
            pic.config(image = photoh6)
        else :
            pic.config(image = photos6)
    elif (column == 7):
        if (row == 1):
            pic.config(image = photod7)
        elif (row == 2):
            pic.config(image = photoc7)
        elif (row == 3):
            pic.config(image = photoh7)
        else :
            pic.config(image = photos7)
    elif (column == 8):
        if (row == 1):
            pic.config(image = photod8)
        elif (row == 2):
            pic.config(image = photoc8)
        elif (row == 3):
            pic.config(image = photoh8)
        else :
            pic.config(image = photos8)
    elif (column == 9):
        if (row == 1):
            pic.config(image = photod9)
        elif (row == 2):
            pic.config(image = photoc9)
        elif (row == 3):
            pic.config(image = photoh9)
        else :
            pic.config(image = photos9)
    elif (column == 10):
        if (row == 1):
            pic.config(image = photod10)
        elif (row == 2):
            pic.config(image = photoc10)
        elif (row == 3):
            pic.config(image = photoh10)
        else :
            pic.config(image = photos10)
    elif (column == 11):
        if (row == 1):
            pic.config(image = photodJ)
        elif (row == 2):
            pic.config(image = photocJ)
        elif (row == 3):
            pic.config(image = photohJ)
        else :
            pic.config(image = photosJ)
    elif (column == 12):
        if (row == 1):
            pic.config(image = photodQ)
        elif (row == 2):
            pic.config(image = photocQ)
        elif (row == 3):
            pic.config(image = photohQ)
        else :
            pic.config(image = photosQ)
    elif (column == 0):
        if (row == 2):
            pic.config(image = photodK)
        elif (row == 3):
            pic.config(image = photocK)
        elif (row == 4):
            pic.config(image = photohK)
        else :
            pic.config(image = photosK)


def clickButton(angka,lambang):
    global listOfBool
    global listOfValue
    global chosenCard
    if len(chosenCard) == 4 and not ((angka+((lambang-1)*13)) in chosenCard):
        tkinter.messagebox.showwarning("Chosen Card Limit","You can only choose 4 cards")
    elif (listOfBool[(angka-1)+((lambang-1)*13)] == True):
        tkinter.messagebox.showwarning("Card has been chosen","You have picked this card")
    elif (angka+((lambang-1)*13)) in chosenCard:
        chosenCard.remove((angka)+((lambang-1)*13))
    else:
        chosenCard.append(angka+((lambang-1)*13))
    if (len(chosenCard)>=1):
        card.config(text="Cards :")
        updatePic(pic1,(chosenCard[0] % 13),math.floor(chosenCard[0]/13)+1)
    if (len(chosenCard)>=2):
        updatePic(pic2,(chosenCard[1] % 13),math.floor(chosenCard[1]/13)+1)
    if (len(chosenCard)>=3):
        updatePic(pic3,(chosenCard[2] % 13),math.floor(chosenCard[2]/13)+1)
    if (len(chosenCard)>=4):
        updatePic(pic4,(chosenCard[3] % 13),math.floor(chosenCard[3]/13)+1)
    if (len(chosenCard)==0):
        card.config(text="")
        pic1.config(image="")
        pic2.config(image="")
        pic3.config(image="")
        pic4.config(image="")
    if (len(chosenCard)==1):
        pic2.config(image="")
        pic3.config(image="")
        pic4.config(image="")
    if (len(chosenCard)==2):
        pic3.config(image="")
        pic4.config(image="")
    if (len(chosenCard)==3):
        pic4.config(image="")

root = Tk()
root.config(bg = "green")
root.title("24 Solver with Greedy Algorithm")
root.iconbitmap("../resources/ico/honor_heart-14.ico")
#root.geometry("500x500") Ini buat resize window kalo perlu
root.resizable(False,False)

title = Label(root, text="    24 CARD GAME SOLVER", fg ="red",bg="green",font = "Verdana 30 bold")
title.grid(column =3, columnspan=7)

card = Label(root,fg ="white",bg="green",font = "Verdana 20 bold")
card.grid(column = 13, row = 0 )

#AS

bdA = Button(root)
photodA = PhotoImage(file="../resources/PNG/AD.png")
bdA.config(image=photodA,width="79",height="120",command=lambda: clickButton(1,1))
bdA.grid(column = 0, row = 1)

bcA = Button(root)
photocA = PhotoImage(file="../resources/PNG/AC.png")
bcA.config(image=photocA,width="79",height="120",command=lambda: clickButton(1,2))
bcA.grid(column = 0, row = 2)

bhA = Button(root)
photohA = PhotoImage(file="../resources/PNG/AH.png")
bhA.config(image=photohA,width="79",height="120",command=lambda: clickButton(1,3))
bhA.grid(column = 0, row = 3)

bsA = Button(root)
photosA = PhotoImage(file="../resources/PNG/AS.png")
bsA.config(image=photosA,width="79",height="120",command=lambda: clickButton(1,4))
bsA.grid(column = 0, row = 4)

#2

bd2 = Button(root)
photod2 = PhotoImage(file="../resources/PNG/2D.png")
bd2.config(image=photod2,width="79",height="120",command=lambda: clickButton(2,1))
bd2.grid(column = 1, row = 1)

bc2 = Button(root)
photoc2 = PhotoImage(file="../resources/PNG/2C.png")
bc2.config(image=photoc2,width="79",height="120",command=lambda: clickButton(2,2))
bc2.grid(column = 1, row = 2)

bh2 = Button(root)
photoh2 = PhotoImage(file="../resources/PNG/2H.png")
bh2.config(image=photoh2,width="79",height="120",command=lambda: clickButton(2,3))
bh2.grid(column = 1, row = 3)

bs2 = Button(root)
photos2 = PhotoImage(file="../resources/PNG/2S.png")
bs2.config(image=photos2,width="79",height="120",command=lambda: clickButton(2,4))
bs2.grid(column = 1, row = 4)

#3

bd3 = Button(root)
photod3 = PhotoImage(file="../resources/PNG/3D.png")
bd3.config(image=photod3,width="79",height="120",command=lambda: clickButton(3,1))
bd3.grid(column = 2, row = 1)

bc3 = Button(root)
photoc3 = PhotoImage(file="../resources/PNG/3C.png")
bc3.config(image=photoc3,width="79",height="120",command=lambda: clickButton(3,2))
bc3.grid(column = 2, row = 2)

bh3 = Button(root)
photoh3 = PhotoImage(file="../resources/PNG/3H.png")
bh3.config(image=photoh3,width="79",height="120",command=lambda: clickButton(3,3))
bh3.grid(column = 2, row = 3)

bs3 = Button(root)
photos3 = PhotoImage(file="../resources/PNG/3S.png")
bs3.config(image=photos3,width="79",height="120",command=lambda: clickButton(3,4))
bs3.grid(column = 2, row = 4)

#4

bd4 = Button(root)
photod4 = PhotoImage(file="../resources/PNG/4D.png")
bd4.config(image=photod4,width="79",height="120",command=lambda: clickButton(4,1))
bd4.grid(column = 3, row = 1)

bc4 = Button(root)
photoc4 = PhotoImage(file="../resources/PNG/4C.png")
bc4.config(image=photoc4,width="79",height="120",command=lambda: clickButton(4,2))
bc4.grid(column = 3, row = 2)

bh4 = Button(root)
photoh4 = PhotoImage(file="../resources/PNG/4H.png")
bh4.config(image=photoh4,width="79",height="120",command=lambda: clickButton(4,3))
bh4.grid(column = 3, row = 3)

bs4 = Button(root)
photos4 = PhotoImage(file="../resources/PNG/4S.png")
bs4.config(image=photos4,width="79",height="120",command=lambda: clickButton(4,4))
bs4.grid(column = 3, row = 4)


#5

bd5 = Button(root)
photod5 = PhotoImage(file="../resources/PNG/5D.png")
bd5.config(image=photod5,width="79",height="120",command=lambda: clickButton(5,1))
bd5.grid(column = 4, row = 1)

bc5 = Button(root)
photoc5 = PhotoImage(file="../resources/PNG/5C.png")
bc5.config(image=photoc5,width="79",height="120",command=lambda: clickButton(5,2))
bc5.grid(column = 4, row = 2)

bh5 = Button(root)
photoh5 = PhotoImage(file="../resources/PNG/5H.png")
bh5.config(image=photoh5,width="79",height="120",command=lambda: clickButton(5,3))
bh5.grid(column = 4, row = 3)

bs5 = Button(root)
photos5 = PhotoImage(file="../resources/PNG/5S.png")
bs5.config(image=photos5,width="79",height="120",command=lambda: clickButton(5,4))
bs5.grid(column = 4, row = 4)

#6

bd6 = Button(root)
photod6 = PhotoImage(file="../resources/PNG/6D.png")
bd6.config(image=photod6,width="79",height="120",command=lambda: clickButton(6,1))
bd6.grid(column = 5, row = 1)

bc6 = Button(root)
photoc6 = PhotoImage(file="../resources/PNG/6C.png")
bc6.config(image=photoc6,width="79",height="120",command=lambda: clickButton(6,2))
bc6.grid(column = 5, row = 2)

bh6 = Button(root)
photoh6 = PhotoImage(file="../resources/PNG/6H.png")
bh6.config(image=photoh6,width="79",height="120",command=lambda: clickButton(6,3))
bh6.grid(column = 5, row = 3)

bs6 = Button(root)
photos6 = PhotoImage(file="../resources/PNG/6S.png")
bs6.config(image=photos6,width="79",height="120",command=lambda: clickButton(6,4))
bs6.grid(column = 5, row = 4)


#7

bd7 = Button(root)
photod7 = PhotoImage(file="../resources/PNG/7D.png")
bd7.config(image=photod7,width="79",height="120",command=lambda: clickButton(7,1))
bd7.grid(column = 6, row = 1)

bc7 = Button(root)
photoc7 = PhotoImage(file="../resources/PNG/7C.png")
bc7.config(image=photoc7,width="79",height="120",command=lambda: clickButton(7,2))
bc7.grid(column = 6, row = 2)

bh7 = Button(root)
photoh7 = PhotoImage(file="../resources/PNG/7H.png")
bh7.config(image=photoh7,width="79",height="120",command=lambda: clickButton(7,3))
bh7.grid(column = 6, row = 3)

bs7 = Button(root)
photos7 = PhotoImage(file="../resources/PNG/7S.png")
bs7.config(image=photos7,width="79",height="120",command=lambda: clickButton(7,4))
bs7.grid(column = 6, row = 4)

#8

bd8 = Button(root)
photod8 = PhotoImage(file="../resources/PNG/8D.png")
bd8.config(image=photod8,width="79",height="120",command=lambda: clickButton(8,1))
bd8.grid(column = 7, row = 1)

bc8 = Button(root)
photoc8 = PhotoImage(file="../resources/PNG/8C.png")
bc8.config(image=photoc8,width="79",height="120",command=lambda: clickButton(8,2))
bc8.grid(column = 7, row = 2)

bh8 = Button(root)
photoh8 = PhotoImage(file="../resources/PNG/8H.png")
bh8.config(image=photoh8,width="79",height="120",command=lambda: clickButton(8,3))
bh8.grid(column = 7, row = 3)

bs8 = Button(root)
photos8 = PhotoImage(file="../resources/PNG/8S.png")
bs8.config(image=photos8,width="79",height="120",command=lambda: clickButton(8,4))
bs8.grid(column = 7, row = 4)

#9

bd9 = Button(root)
photod9 = PhotoImage(file="../resources/PNG/9D.png")
bd9.config(image=photod9,width="79",height="120",command=lambda: clickButton(9,1))
bd9.grid(column = 8, row = 1)

bc9 = Button(root)
photoc9 = PhotoImage(file="../resources/PNG/9C.png")
bc9.config(image=photoc9,width="79",height="120",command=lambda: clickButton(9,2))
bc9.grid(column = 8, row = 2)

bh9 = Button(root)
photoh9 = PhotoImage(file="../resources/PNG/9H.png")
bh9.config(image=photoh9,width="79",height="120",command=lambda: clickButton(9,3))
bh9.grid(column = 8, row = 3)

bs9 = Button(root)
photos9 = PhotoImage(file="../resources/PNG/9S.png")
bs9.config(image=photos9,width="79",height="120",command=lambda: clickButton(9,4))
bs9.grid(column = 8, row = 4)

#10

bd10 = Button(root)
photod10 = PhotoImage(file="../resources/PNG/10D.png")
bd10.config(image=photod10,width="79",height="120",command=lambda: clickButton(10,1))
bd10.grid(column = 9, row = 1)

bc10 = Button(root)
photoc10 = PhotoImage(file="../resources/PNG/10C.png")
bc10.config(image=photoc10,width="79",height="120",command=lambda: clickButton(10,2))
bc10.grid(column = 9, row = 2)

bh10 = Button(root)
photoh10 = PhotoImage(file="../resources/PNG/10H.png")
bh10.config(image=photoh10,width="79",height="120",command=lambda: clickButton(10,3))
bh10.grid(column = 9, row = 3)

bs10 = Button(root)
photos10 = PhotoImage(file="../resources/PNG/10S.png")
bs10.config(image=photos10,width="79",height="120",command=lambda: clickButton(10,4))
bs10.grid(column = 9, row = 4)

#J

bdJ = Button(root)
photodJ = PhotoImage(file="../resources/PNG/JD.png")
bdJ.config(image=photodJ,width="79",height="120",command=lambda: clickButton(11,1))
bdJ.grid(column = 10, row = 1)

bcJ = Button(root)
photocJ = PhotoImage(file="../resources/PNG/JC.png")
bcJ.config(image=photocJ,width="79",height="120",command=lambda: clickButton(11,2))
bcJ.grid(column = 10, row = 2)

bhJ = Button(root)
photohJ = PhotoImage(file="../resources/PNG/JH.png")
bhJ.config(image=photohJ,width="79",height="120",command=lambda: clickButton(11,3))
bhJ.grid(column = 10, row = 3)

bsJ = Button(root)
photosJ = PhotoImage(file="../resources/PNG/JS.png")
bsJ.config(image=photosJ,width="79",height="120",command=lambda: clickButton(11,4))
bsJ.grid(column = 10, row = 4)

#Q

bdQ = Button(root)
photodQ = PhotoImage(file="../resources/PNG/QD.png")
bdQ.config(image=photodQ,width="79",height="120",command=lambda: clickButton(12,1))
bdQ.grid(column = 11, row = 1)

bcQ = Button(root)
photocQ = PhotoImage(file="../resources/PNG/QC.png")
bcQ.config(image=photocQ,width="79",height="120",command=lambda: clickButton(12,2))
bcQ.grid(column = 11, row = 2)

bhQ = Button(root)
photohQ = PhotoImage(file="../resources/PNG/QH.png")
bhQ.config(image=photohQ,width="79",height="120",command=lambda: clickButton(12,3))
bhQ.grid(column = 11, row = 3)

bsQ = Button(root)
photosQ = PhotoImage(file="../resources/PNG/QS.png")
bsQ.config(image=photosQ,width="79",height="120",command=lambda: clickButton(12,4))
bsQ.grid(column = 11, row = 4)

#K

bdK = Button(root)
photodK = PhotoImage(file="../resources/PNG/KD.png")
bdK.config(image=photodK,width="79",height="120",command=lambda: clickButton(13,1))
bdK.grid(column = 12, row = 1)

bcK = Button(root)
photocK = PhotoImage(file="../resources/PNG/KC.png")
bcK.config(image=photocK,width="79",height="120",command=lambda: clickButton(13,2))
bcK.grid(column = 12, row = 2)

bhK = Button(root)
photohK = PhotoImage(file="../resources/PNG/KH.png")
bhK.config(image=photohK,width="79",height="120",command=lambda: clickButton(13,3))
bhK.grid(column = 12, row = 3)

bsK = Button(root)
photosK = PhotoImage(file="../resources/PNG/KS.png")
bsK.config(image=photosK,width="79",height="120",command=lambda: clickButton(13,4))
bsK.grid(column = 12, row = 4)

#ChosenCard

pic1 = Label(root,bg = "green")
pic2 = Label(root,bg = "green")
pic3 = Label(root,bg = "green")
pic4 = Label(root,bg = "green")
pic1.grid(column = 13, row = 1)
pic2.grid(column = 13, row = 2)
pic3.grid(column = 13, row = 3)
pic4.grid(column = 13, row = 4)

#Button Solve, Random, dan Reset
solveButton = Button(root)
photoSolve = PhotoImage(file="../resources/solveButton.png")
solveButton.config(image = photoSolve, width = "158", height = "70")
solveButton.grid(column = 0, row = 5, columnspan = 2,rowspan = 2)

randButton = Button(root)
photoRand = PhotoImage(file="../resources/diceButton.png")
randButton.config(image = photoRand, width = "79", height = "70")
randButton.grid(column = 2, row = 5,rowspan = 2)

resetButton = Button(root)
photoReset = PhotoImage(file="../resources/resetButton.png")
resetButton.config(image = photoReset, width = "79", height="70")
resetButton.grid(column = 12, row = 5, rowspan = 2)


#Label Hasil
textHasil = Label(root,text = "Result :", bg = "green", fg = "white",font = "Verdana 13 bold")
textHasil.grid(column=3, row= 5,rowspan = 2)


hasil = Label(root,text = "Nothing", bg = "green", fg = "white",font = "Verdana 20 bold")
hasil.grid(column =4, row = 5, columnspan = 6,rowspan = 2)

#Label Score dan Total Score
score = Label(root,text = "Score :", bg = "green", fg = "white",font = "Verdana 13 bold")
score.grid(column = 10, row = 5)
total = Label(root,text = "Total :", bg = "green", fg = "white",font = "Verdana 13 bold")
total.grid(column = 10, row = 6)

scorePoint = Label(root,text = "###", bg = "green", fg = "white",font = "Verdana 13 bold")
scorePoint.grid(column = 11, row = 5)
totalPoint = Label(root,text = "###", bg = "green", fg = "white",font = "Verdana 13 bold")
totalPoint.grid(column = 11, row = 6)

root.mainloop()
