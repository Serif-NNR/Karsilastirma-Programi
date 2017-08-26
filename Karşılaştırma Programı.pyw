# -8- coding:utf-8-*-
#######################################################
#######################################################
####        Şerif İnanır                           ####
####                                               ####
####    Alaaddin Keykubat Bilgisayar Mühendisliği  ####
####                                               ####
#######################################################
#######################################################


from tkinter import *
import os
from tkinter import filedialog

pnc = Tk()
pnc.title("Karşılaştırma Programı |   Şerif İnanır")
pnc.geometry("630x330+350+150")
pnc.wm_iconbitmap("resim/simge.ico")
pnc.resizable(False, False)

arka = PhotoImage(file="resim/arka.png")
arkaLogo = Label(image=arka)
arkaLogo.place(x=-5, y=0)













##############################################  Menü Başlangıcı
menu = Menu(pnc)
pnc.config(menu=menu)
menü1 = Menu(menu, tearoff=0)
menu.add_cascade(label="Ana Menü", menu=menü1)
menü2 = Menu(menu, tearoff=0)
menu.add_cascade(label="İletişim", menu=menü2)
menü3 = Menu(menu, tearoff=0)
menu.add_cascade(label="Kullanımı ve Amacı", menu=menü3)

######## Dikkat!!!!  DEĞİŞECEK #################
sonuc = Label(text="| Henüz Dosya Oluşmadı |")##    Dosya İşlem Butonlarına basıldığında bu label
sonuc.place(x=430, y=280)                     ##  oluşturulan dosya ismine göre değişecek.
################################################



##################################################
# SEÇİLEN DOSYA

def dosyaU1():
    dosyau1 = filedialog.askopenfilename()
    dsy1["text"]=dosyau1

dsy1=Label(text="Dosya Seçilmedi")
dsy1.place(x=70,y=180)


def dosyaU2():
    dosyau2 = filedialog.askopenfilename()
    dsy2["text"]=dosyau2

dsy2=Label(text="Dosya Seçilmedi")
dsy2.place(x=70,y=210)

######################################################


#################################################################
# DOSYA SEÇME BUTONLARI
dosya1 = Button(text="İlk Dosya",
                command=dosyaU1,
                bg="black", fg="red")
dosya1.place(x=10, y=150)

dosya2 = Button(text="İkinci Dosya",
                command=dosyaU2,
                bg="black", fg="red")
dosya2.place(x=70, y=150)
#####################################################################



##############   Sıkıldım Amk    #################################

############## Kahve molasının ardından DEVAMMM ##################


##############################################
# DOSYA UZANTI SIRALAMA ETİKETLERİ
dosya1L = Label(text="Dosya 1:", fg="red")
dosya1L.place(x=10, y=180)

dosya2L = Label(text="Dosya 2:", fg="red")
dosya2L.place(x=10, y=210)
###############################################



###########################################################
# DOSYA İŞLEM FONKSİYONLARI
def ilkfarkı():
    d1 = open(dsy1["text"])
    d1_satırlar = d1.readlines()
    d2 = open(dsy2["text"])
    d2_satırlar = d2.readlines()
    kyt1 = open("İlk Dosyaya Özgü.txt", "w")
    for a in d1_satırlar:
        if not a in d2_satırlar:
            print(a, file=kyt1, end="")
    kyt1.close()
    d1.close()
    d2.close()
    sonuc["text"] = "| İlk Dosya Farkları Oluşturuldu |"





def ikincifarkı():
    d1 = open(dsy1["text"])
    d1_satırlar = d1.readlines()
    d2 = open(dsy2["text"])
    d2_satırlar = d2.readlines()
    kyt2 = open("İkinci Dosyaya Özgü.txt", "w")
    for b in d2_satırlar:
        if not b in d1_satırlar:
            print(b, file=kyt2, end="")
    kyt2.close()
    d1.close()
    d2.close()
    sonuc["text"] = "| İkinci Dosya Farkları Oluşturuldu |"


def ortaklar():
    d1 = open(dsy1["text"])
    d1_satırlar = d1.readlines()
    d2 = open(dsy2["text"])
    d2_satırlar = d2.readlines()
    kyt3 = open("Ortak Satırlar.txt", "w")
    for i in d2_satırlar:
        if i in d1_satırlar:
            print(i, file=kyt3, end="")
    kyt3.close()
    d1.close()
    d2.close()
    sonuc["text"] = "| Ortak Satırlar Oluşturuldu |"


def essizdosya():
    d1 = open(dsy1["text"])
    d1_satırlar = d1.readlines()
    d2 = open(dsy2["text"])
    d2_satırlar = d2.readlines()
    kyt4 = open("Eşsiz Dosya.txt", "w")
    for a in d1_satırlar:
        if not a in d2_satırlar:
            print(a, file=kyt4, end="")
    for b in d2_satırlar:
        if not b in d1_satırlar:
            print(b, file=kyt4, end="")
    for i in d2_satırlar:
        if i in d1_satırlar:
            print(i, file=kyt4, end="")
    kyt4.close()
    d1.close()
    d2.close()
    sonuc["text"] = "| Eşsiz Satırlar Oluşturuldu |"


#################################################################################






##################################################################################
# DOSYA İŞLEM BUTONLARI
ilkFark = Button(text="İlk Dosya Farkı", bg="black", fg="red", command=ilkfarkı)
ilkFark.place(x=10, y=250)

ikinciFark = Button(text="İkinci Dosya Farkı", bg="black", fg="red", command=ikincifarkı)
ikinciFark.place(x=100, y=250)

ortak = Button(text="Ortak Satırlar", bg="black", fg="red", command=ortaklar)
ortak.place(x=206, y=250)

essiz = Button(text="Eşsiz Dosya", bg="black", fg="red", command=essizdosya)
essiz.place(x=289, y=250)
######################################################################################



mainloop()
