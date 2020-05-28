import tkinter as tk
from tkinter import ttk
import sqlite3 as sqlite
from tkinter import *
def search():
    global liste
    liste.delete(0, tk.END)
    giris1=deger1.get()
    oku=im.execute("select * from ceviri where ingilizce like ?", ('%'+giris1+'%',))
    kayıtlar=oku.fetchall()
    print(kayıtlar)
    for kayıt in kayıtlar:
        liste.insert(tk.END,kayıt[2])

    oku2 = im.execute("select * from ceviri where ingilizce2 like ?", ('%'+giris1+'%',))
    kayıtlar2 = oku2.fetchall()
    print(kayıtlar2)
    for kayıt2 in kayıtlar2:
        liste.insert(tk.END, kayıt2[3])

    oku3 = im.execute("select * from ceviri where turkce like ?", ('%'+giris1+'%',))
    kayıtlar3 = oku3.fetchall()
    print(kayıtlar3)
    for kayıt3 in kayıtlar3:
        liste.insert(tk.END, kayıt3[0])

    oku4 = im.execute("select * from ceviri where turkce2 like ?", ('%'+giris1+'%',))
    kayıtlar4 = oku4.fetchall()
    print(kayıtlar4)
    for kayıt4 in kayıtlar4:
        liste.insert(tk.END, kayıt4[1])


def history():
    pass



def arama():
    global liste2
    liste2.delete(0, tk.END)
    giris1 = deger1.get()
    oku = im.execute("select * from ceviri where ingilizce like ?", (giris1,))
    kayıtlar = oku.fetchall()
    print(kayıtlar)
    for kayıt in kayıtlar:
        liste2.insert(tk.END, kayıt[0], kayıt[1])

    oku2 = im.execute("select * from ceviri where ingilizce2 like ?", (giris1,))
    kayıtlar2 = oku2.fetchall()
    print(kayıtlar2)
    for kayıt2 in kayıtlar2:
        liste2.insert(tk.END, kayıt2[0], kayıt2[1])

    oku3 = im.execute("select * from ceviri where turkce like ?", (giris1,))
    kayıtlar3 = oku3.fetchall()
    print(kayıtlar3)
    for kayıt3 in kayıtlar3:
        liste2.insert(tk.END, kayıt3[2], kayıt3[3])

    oku4= im.execute("select * from ceviri where turkce2 like ?", (giris1,))
    kayıtlar4 = oku4.fetchall()
    print(kayıtlar4)
    for kayıt4 in kayıtlar4:
        liste2.insert(tk.END, kayıt4[2], kayıt4[3])


pen = tk.Tk()
pen.title("Dictionry")



ustframe=tk.LabelFrame(pen,width=100,bg="#b22222")
ustframe.grid(column=0,row=0,padx=60)
butonsearch=tk.Button(ustframe,text="Search",width=25,bg="#bebebe",command=search).grid(column=0,row=0,sticky=tk.W)
butonhistory=tk.Button(ustframe,text="History",width=25,command=history).grid(column=1,row=0,sticky=tk.W)
deger1 =tk.StringVar()
deger1.set("Home")
giris1=tk.Entry(ustframe,width=50,textvariable=deger1).grid(column=3,row=0,sticky=tk.W,padx=40)
butonceviri=tk.Button(ustframe,text="Ceviri Butonu",width=10,command=arama).grid(column=4,row=0)






ortaframe=tk.LabelFrame(pen,bg="#bebebe")
ortaframe.grid(column=0,row=1,padx=60)




turengframe=tk.LabelFrame(ortaframe)
turengframe.grid(column=0,row=0)
foto=PhotoImage(file="turenglogo.gif",width=160,height=40)
etiket=Label(turengframe,text="TURENG",image=foto)
etiket.grid(column=0,row=1,sticky=tk.W)




logoframe=tk.LabelFrame(ortaframe,width=200)
logoframe.grid(column=1,row=0)
#ses logo
foto1=PhotoImage(file="ses.gif",width=20,height=20)
etiket1=Label(logoframe,image=foto1)
etiket1.grid(column=1,row=1,sticky=tk.W)
#bayrak logo
foto2=PhotoImage(file="ingiltere.gif",width=20,height=20)
etiket2=Label(logoframe,image=foto2)
etiket2.grid(column=2,row=1,sticky=tk.W)

foto3=PhotoImage(file="amerika.gif",width=20,height=20)
etiket3=Label(logoframe,image=foto3)
etiket3.grid(column=3,row=1,sticky=tk.W)

foto4=PhotoImage(file="avusturalya.gif",width=20,height=20)
etiket4=Label(logoframe,image=foto4)
etiket4.grid(column=4,row=1,sticky=tk.W)


#ttk.Label(ortaframe,text="LOGO").grid(column=1,row=1,padx=100,sticky=tk.E)






ortaaltframe=tk.LabelFrame(pen,width=100,bg="#bebebe")
ortaaltframe.grid(column=0,row=2,padx=60)







altsolframe=ttk.Label(ortaaltframe,width=75)
altsolframe.grid(column=0,row=1)
liste=tk.Listbox(altsolframe,highlightcolor="red")
liste.grid(column=1, row=1,padx=60,pady=60)








altsagframe=tk.LabelFrame(ortaaltframe,width=100,bd=0)
altsagframe.grid(column=1,row=1)
liste2 = tk.Listbox(altsagframe,highlightcolor="red")
liste2.grid(column=1, row=1,padx=60,pady=60)




vt = sqlite.connect('verit.sqlite')
im = vt.cursor()
tablo_yap = """CREATE TABLE IF NOT EXISTS ceviri(turkçe, ingilizce)"""
im.execute(tablo_yap)
vt.commit()


pen.mainloop()