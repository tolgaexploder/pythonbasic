#kutuphaneler
from Tkinter import *
import tkMessageBox
import random
import tkFont

#global degiskenler
Aoyuncusu=""
Boyuncusu=""
En=0
Boy=0
count=0
matrix={}
a1=0
a2=0
b1=0
b2=0
Ascore=0
Bscore=0

#top window
top = Tk()

top.title("Oyuna Hosgeldiniz!")
top.geometry("350x200+500+300")
top.resizable(width=FALSE, height=FALSE)

#fonksiyonlar
def setPlayScreen(en,boy):
    global a1,a2,b1,b2,OyunPenceresi
    OyunPenceresi= Tk()
    OyunPenceresi.title("Matris Oyunu")
    OyunPenceresi.geometry("+700+400")
    OyunPenceresi.resizable(width=FALSE, height=FALSE)

    for i in range(1,en+1):
        for j in range(1,boy+1):
           #lblfont = tkFont.Font(family='Helvetica',size=1, weight='bold')           
           matrix[i,j]=Label(OyunPenceresi, text=random.randint(1,9),font=("Helvetica",30))
           matrix[i,j].grid(row=i,column=j)
    paddinglbl1=Label(OyunPenceresi,width=4, height=2).grid(row=0,column=0)
    paddinglbl2=Label(OyunPenceresi,width=4, height=2).grid(row=en+2,column=boy+2)
    
    def randomize():
        global a1,a2,b1,b2
        a1=random.randint(1,en)
        a2=random.randint(1,boy)
        b1=random.randint(1,en)
        b2=random.randint(1,boy)
        if a1==b1 and a2==b2:
            randomize()
        else:
            matrix[a1,a2].config(text='A',fg='red')
            matrix[b1,b2].config(text='B',fg='blue')

    randomize()
            


    top.withdraw()
    setPlayerScreen(OyunPenceresi)

def playGame(buton):
    global a1,a2,b1,b2,En,Boy,Ascore,Bscore,Aoyuncusu,Boyuncusu,OyunPenceresi

    def toggleWithdraft():
        if buton<5:
            AoyuncuPenceresi.withdraw()
            BoyuncuPenceresi.deiconify()
            BoyuncuPenceresi.lift()
        else:
            BoyuncuPenceresi.withdraw()
            AoyuncuPenceresi.deiconify()
            AoyuncuPenceresi.lift()

        OyunPenceresi.lift()

    def checkFinish():
        #for ndx, member in enumerate(my_list):
        #my_list[ndx] += 42
        for i in range(1,En+1):
            for j in range(1,Boy+1):
                if matrix[i,j].cget("text") != 'A' and matrix[i,j].cget("text") != 'B':
                    if matrix[i,j].cget("text") != '0':
                        return False
        return True
               
    if buton==1:
        if a2-1>0:
            if matrix[a1,a2].cget("text")=="AB":
                matrix[a1,a2].config(text='B',fg='blue')
            else:
                matrix[a1,a2].config(text='0',fg='black')
            a2=a2-1
            if type(matrix[a1,a2].cget("text"))==type(5):
                Ascore=int(matrix[a1,a2].cget("text"))+Ascore
            if matrix[a1,a2].cget("text")=="B":
                matrix[a1,a2].config(text='AB',fg='yellow')
            else:
                matrix[a1,a2].config(text='A',fg='red')
            toggleWithdraft()
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                
    elif buton==2:
        if a2+1<Boy+1:
            if matrix[a1,a2].cget("text")=="AB":
                matrix[a1,a2].config(text='B',fg='blue')
            else:
                matrix[a1,a2].config(text='0',fg='black')
            a2=a2+1
            if type(matrix[a1,a2].cget("text"))==type(5):
                Ascore=int(matrix[a1,a2].cget("text"))+Ascore
            if matrix[a1,a2].cget("text")=="B":
                matrix[a1,a2].config(text='AB',fg='yellow')
            else:
                matrix[a1,a2].config(text='A',fg='red')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()                
                
    elif buton==3:
        if a1-1>0:
            if matrix[a1,a2].cget("text")=="AB":
                matrix[a1,a2].config(text='B',fg='blue')
            else:
                matrix[a1,a2].config(text='0',fg='black')
            a1=a1-1
            if type(matrix[a1,a2].cget("text"))==type(5):
                Ascore=int(matrix[a1,a2].cget("text"))+Ascore
            if matrix[a1,a2].cget("text")=="B":
                matrix[a1,a2].config(text='AB',fg='yellow')
            else:
                matrix[a1,a2].config(text='A',fg='red')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()

    elif buton==4:
        if a1+1<En+1:
            if matrix[a1,a2].cget("text")=="AB":
                matrix[a1,a2].config(text='B',fg='blue')
            else:
                matrix[a1,a2].config(text='0',fg='black')
            a1=a1+1
            if type(matrix[a1,a2].cget("text"))==type(5):
                Ascore=int(matrix[a1,a2].cget("text"))+Ascore
            if matrix[a1,a2].cget("text")=="B":
                matrix[a1,a2].config(text='AB',fg='yellow')
            else:
                matrix[a1,a2].config(text='A',fg='red')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()

    elif buton==5:
        if b2-1>0:
            if matrix[b1,b2].cget("text")=="AB":
                matrix[b1,b2].config(text='A',fg='red')
            else:
                matrix[b1,b2].config(text='0',fg='black')
            b2=b2-1
            if type(matrix[b1,b2].cget("text"))==type(5):
                Bscore=int(matrix[b1,b2].cget("text"))+Bscore
            if matrix[b1,b2].cget("text")=="A":
                matrix[b1,b2].config(text='AB',fg='yellow')
            else:
                matrix[b1,b2].config(text='B',fg='blue')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
    elif buton==6:
        if b2+1<Boy+1:
            if matrix[b1,b2].cget("text")=="AB":
                matrix[b1,b2].config(text='A',fg='red')
            else:
                matrix[b1,b2].config(text='0',fg='black')
            b2=b2+1
            if type(matrix[b1,b2].cget("text"))==type(5):
                Bscore=int(matrix[b1,b2].cget("text"))+Bscore
            if matrix[b1,b2].cget("text")=="A":
                matrix[b1,b2].config(text='AB',fg='yellow')
            else:
                matrix[b1,b2].config(text='B',fg='blue')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()

    elif buton==7:
        if b1-1>0:
            if matrix[b1,b2].cget("text")=="AB":
                matrix[b1,b2].config(text='A',fg='red')
            else:
                matrix[b1,b2].config(text='0',fg='black')
            b1=b1-1
            if type(matrix[b1,b2].cget("text"))==type(5):
                Bscore=int(matrix[b1,b2].cget("text"))+Bscore
            if matrix[b1,b2].cget("text")=="A":
                matrix[b1,b2].config(text='AB',fg='yellow')
            else:
                matrix[b1,b2].config(text='B',fg='blue')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
    elif buton==8:
        if b1+1<En+1:
            if matrix[b1,b2].cget("text")=="AB":
                matrix[b1,b2].config(text='A',fg='red')
            else:
                matrix[b1,b2].config(text='0',fg='black')
            b1=b1+1
            if type(matrix[b1,b2].cget("text"))==type(5):
                Bscore=int(matrix[b1,b2].cget("text"))+Bscore
            if matrix[b1,b2].cget("text")=="A":
                matrix[b1,b2].config(text='AB',fg='yellow')
            else:
                matrix[b1,b2].config(text='B',fg='blue')
            toggleWithdraft()                
            if checkFinish():
                if Ascore>Bscore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Aoyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()
                elif Bscore>Ascore:
                    tkMessageBox.showinfo( "Oyun Bitti", Aoyuncusu+":"+str(Ascore)+" Puan\n"+ Boyuncusu+":"+str(Bscore)+" Puan.\n Kazanan:"+Boyuncusu)
                    top.destroy()
                    OyunPenceresi.destroy()

  

def setPlayerScreen(OyunPenceresi):

    global AoyuncuPenceresi, BoyuncuPenceresi
    AoyuncuPenceresi=Toplevel(OyunPenceresi)
    AoyuncuPenceresi.resizable(width=FALSE, height=FALSE)
    AoyuncuPenceresi.title("A-"+Aoyuncusu)
    AoyuncuPenceresi.geometry("+500+400")

    btnAsol=Button(AoyuncuPenceresi,text ="sol",width=6,height=2,command=lambda:playGame(1)).place(relx=0.1,rely=0.35)
    btnAsag=Button(AoyuncuPenceresi,text ="sag",width=6,height=2,command=lambda:playGame(2)).place(relx=0.605,rely=0.35)
    btnAyukari=Button(AoyuncuPenceresi,text ="yukari",width=6,height=2,command=lambda:playGame(3)).place(relx=0.35,rely=0.15)
    btnAasagi=Button(AoyuncuPenceresi,text ="asagi",width=6,height=2,command=lambda:playGame(4)).place(relx=0.35,rely=0.555)


    BoyuncuPenceresi=Toplevel(OyunPenceresi)
    BoyuncuPenceresi.resizable(width=FALSE, height=FALSE)
    BoyuncuPenceresi.title("B-"+Boyuncusu)
    BoyuncuPenceresi.geometry("+500+400")

    btnBsol=Button(BoyuncuPenceresi,text ="sol",width=6,height=2,command=lambda:playGame(5)).place(relx=0.1,rely=0.35)
    btnBsag=Button(BoyuncuPenceresi,text ="sag",width=6,height=2,command=lambda:playGame(6)).place(relx=0.605,rely=0.35)
    btnByukari=Button(BoyuncuPenceresi,text ="yukari",width=6,height=2,command=lambda:playGame(7)).place(relx=0.35,rely=0.15)
    btnBasagi=Button(BoyuncuPenceresi,text ="asagi",width=6,height=2,command=lambda:playGame(8)).place(relx=0.35,rely=0.555)

    if random.randint(0,1)==0:
        AoyuncuPenceresi.withdraw()
        BoyuncuPenceresi.lift()
    else:
        BoyuncuPenceresi.withdraw()
        AoyuncuPenceresi.lift()

def setGame():
    global En,Boy,Aoyuncusu,Boyuncusu
    Aoyuncusu=entryAoyuncusu.get()
    Boyuncusu=entryBoyuncusu.get()
    En=int(entryOyununEni.get())
    Boy=int(entryOyununBoyu.get())
    
    if Aoyuncusu=="" or Boyuncusu=="" or type(Aoyuncusu)!=type("") or type(Boyuncusu)!=type(""):
        tkMessageBox.showinfo( "Hatali Giris", "Lutfen gecerli oyuncu isimleri giriniz!")
    elif En<2 or En>9 or Boy<2 or Boy>9:
        tkMessageBox.showinfo( "Hatali Giris", "Lutfen gecerli oyun matrisi giriniz!")
    else:
        setPlayScreen(En,Boy)

#top window nesne ayarlari
lblAoyuncusu = Label(top,text="A oyuncusunun Adi")
lblAoyuncusu.place(relx=0.03,rely=0.05)

entryAoyuncusu = Entry(top)
entryAoyuncusu.place(relx=0.40,rely=0.05)

lblBoyuncusu = Label(top,text="B oyuncusunun Adi")
lblBoyuncusu.place(relx=0.03,rely=0.20)

entryBoyuncusu = Entry(top)
entryBoyuncusu.place(relx=0.40,rely=0.20)


lblEn = Label(top,text="Oyunun Boyu")
lblEn.place(relx=0.03,rely=0.35)

entryOyununEni = Entry(top)
entryOyununEni.place(relx=0.40,rely=0.35)

lblBoy = Label(top,text="Oyunun Eni:")
lblBoy.place(relx=0.03,rely=0.50)

entryOyununBoyu = Entry(top)
entryOyununBoyu.place(relx=0.40,rely=0.50)

btnGiris = Button(top,text ="Giris",width=15, command = setGame)
btnGiris.place(relx=0.10,rely=0.75)

btnCikis = Button(top,text ="Cikis",width=15,command = top.destroy)
btnCikis.place(relx=0.60,rely=0.75)

mainloop()
