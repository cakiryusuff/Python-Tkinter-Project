from datetime import datetime,timedelta
import pandas as pd
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk

win = tkinter.Tk()
win.title("Araba Kiralama Otomasyonu")
win.geometry("890x575")

class araba_kirala():
    def __init__(self):

        self.aracfiyat = {
            "Bmw":150,
            "Renault":100,
            "Doğan":175,
            "Şahin":50,
            "Toyota":125,
            "Audi":200,
            "Tesla":250
        }
        self.mevcutarabalar = {"Bmw","Renault","Doğan","Şahin","Toyota","Audi","Tesla"}
        #mevcutarabalar listesini oluşturmamın nedeni araç sayısını gösterebilmek için len() methodunu kullandım
        #bu yüzden araba kiralandığında listeden çıkıyor araç sayısı 1 azalıyor. iade edildiğinde artıyor.

    def araclarıgoster(self):
# arabalar ve fiyatlarını terminalde gösterme
        print("Arabalar ve Saatlik Ücretleri:")
        for key,value in self.aracfiyat.items():
            print(key,value,"TL")

############################## ARABALAR VE FİYATLARINI TKİNTER DA TABLO OLARAK GÖSTERME #########################
        self.top = Toplevel()
        self.top.geometry("600x180")
        
        self.columns = ("Arabalar","fiyat","gunluk")
        self.tree = ttk.Treeview(self.top, columns=self.columns, show='headings')
        self.tree.heading('Arabalar', text='Arabalar')
        self.tree.heading('fiyat', text='Saatlik kiralama ücretleri')
        self.tree.heading('gunluk', text='Günlük kiralama ücretleri')


        self.a = ["BMW",150,150*24]
        self.b = ["Renault",100,100*24]
        self.c = ["Doğan",175,175*24]
        self.d = ["Şahin",50,50*24]
        self.e = ["Toyota",125,125*24]
        self.f = ["Audi",200,200*24]
        self.g = ["Tesla",250,250*24]

        self.tree.insert('', tk.END, values=self.a)
        self.tree.insert('', tk.END, values=self.b)
        self.tree.insert('', tk.END, values=self.c)
        self.tree.insert('', tk.END, values=self.d)
        self.tree.insert('', tk.END, values=self.e)
        self.tree.insert('', tk.END, values=self.f)
        self.tree.insert('', tk.END, values=self.g)

        self.tree.grid(row=0, column=0, sticky='nsew')

        self.top.mainloop()
#####################################################################################################################
    
    def kiralamasuresi(self,gun,saat,arac):
        self.mevcutarabalar.remove(arac) #mevcut araçlardan kiralanan aracı çıkartıyor
        self.result = datetime.now() + timedelta(days=gun,hours=saat) #girilen gün ve saati şuanki tarihe ekleyip ne zamana kadar kiralanacağını buluyor
        self.zaman = datetime.strftime(self.result,'%Y %B %A %X') #Yukarıda oluşan yeni tarihi düzenleyerek yazdırıyor
        print(f"{self.zaman}'a kadar kiralanacak")
        if gun != 0:                                                 #|
            self.time = 24*gun + saat                                #|Bu kısımda eğer gün girilirse onu saat hesabına
        else:                                                        #|çeviriyor ve girilen saatle toplayıp hangi araba 
            self.time = saat                                         #|kiralandıysa onun saatlik ücretiyle çarpıp
        self.fiyat = f"{self.time*(self.aracfiyat[arac])} TL"        #|fiyatı yazdırıyor.
        print("Fiyatı ",self.fiyat)                                  #|


class araba(araba_kirala):
    def __init__(self):
        araba_kirala.__init__(self)

    def arabaozellikleri(self):
        #PANDAS'LA OLUŞTURULAN ÖZELLİKLER TABLOSU TERMİNALDE GÖZÜKÜYOR
        self.list = [["VAR","YOK","VAR","YOK","VAR"],["YOK","YOK","YOK","YOK","YOK"],["VAR","YOK","VAR","YOK","VAR"],["YOK","YOK","YOK","YOK","YOK"],["YOK","VAR","VAR","VAR","YOK"],["VAR","VAR","VAR","YOK","VAR"],["VAR","VAR","VAR","VAR","VAR"]]
        self.df = pd.DataFrame(self.list,index=["Bmw","Renault","Doğan","Şahin","Toyota","Audi","Tesla"],columns=["Klima","ısıtma","Otovites","elektrik","Hybrit"])
        print(self.df)

############################### ARABA ÖZELLİKLERİ TKİNTER TABLO KISMI #####################################
        self.top = Toplevel()
        self.top.geometry("1200x200")
        self.columns = ("Arabalar","Klima","ısıtma","Otovites","elektrik","Hybrit")
        self.tree = ttk.Treeview(self.top, columns=self.columns, show='headings')
        self.tree.heading('Arabalar', text='Arabalar')
        self.tree.heading('Klima', text='Klima')
        self.tree.heading('ısıtma', text='Koltuk Isıtma')
        self.tree.heading('Otovites', text='Otomatik Vites')
        self.tree.heading('elektrik', text='Dokunmatik Arayüz')
        self.tree.heading('Hybrit', text='Hybrit')

        self.a = ["BMW","VAR","YOK","VAR","YOK","YOK"]
        self.b = ["Renault","YOK","YOK","YOK","YOK","YOK"]
        self.c = ["Doğan","VAR","YOK","VAR","YOK","YOK"]
        self.d = ["Şahin","VAR","YOK","VAR","YOK","VAR"]
        self.e = ["Toyota","YOK","VAR","VAR","VAR","YOK"]
        self.f = ["Audi","VAR","VAR","VAR","YOK","VAR"]
        self.g = ["Tesla","VAR","VAR","VAR","VAR","VAR"]

        self.tree.insert('', tk.END, values=self.a)
        self.tree.insert('', tk.END, values=self.b)
        self.tree.insert('', tk.END, values=self.c)
        self.tree.insert('', tk.END, values=self.d)
        self.tree.insert('', tk.END, values=self.e)
        self.tree.insert('', tk.END, values=self.f)
        self.tree.insert('', tk.END, values=self.g)

        self.tree.grid(row=0, column=0, sticky='nsew')
        self.top.mainloop()
#######################################################################################################################
    
    def aracgerigetirme(self,arac): #geri getirilen aracı mevcutarabalar listesine ekler
        self.mevcutarabalar.add(arac)

    def arabasayisi(self): #araba sayısını return eder
        msg.showinfo(title="Araba Sayısı", message=f"{len(self.mevcutarabalar)} Tane Kiralanabilir Araba Var.")
        return print(f"{len(self.mevcutarabalar)} tane kiralanabilir araba var.")
        

class musteri(araba):
    def __init__(self):
        araba.__init__(self)
        
#################################################TKİNTER ARAYÜZ KISMI##########################################
        self.mystr = StringVar() 
        self.mystr.set("Kaç Gün ?(sadece sayı giriniz.)") # Araç kiralamak için gerekli olan bilgilerin alındığı yere ne yazılacağını söyler.

        self.mystr2 = StringVar()
        self.mystr2.set("Kaç Saat ?(sadece sayı giriniz.)")# Araç kiralamak için gerekli olan bilgilerin alındığı yere ne yazılacağını söyler.

        self.mystr3 = StringVar()
        self.mystr3.set("Arabanın Markası ?")# Araç kiralamak için gerekli olan bilgilerin alındığı yere ne yazılacağını söyler.

        myFrame1 = Frame(win)
        myFrame1.pack(side=TOP,fill=X)  #ilk 3 butonu içine alan frame

        myFrame2 = Frame(win)
        myFrame2.pack(side=TOP,fill=X) # 3 veri giriş ve araç kirala butonunu içine alan frame

        myFrame3 = Frame(win) # son 4 butonu içine alan frame
        myFrame3.pack(side=TOP,fill=X)

        self.label = Label(myFrame1,text="Yusuf Çakır Oto Kiralamaya Hoşgeldiniz",font="GOTHAM 25 bold",fg="white",bg="black")
        self.label.pack(fill=X) # başlık kısmı

        self.myButton1=Button(myFrame1,text="1. Arabaları Göster",command=self.araclarıgoster,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton1.pack(fill=BOTH)# 1. buton ve araclarıgoster fonksiyonunun çalıştırıldığı yer
 
        self.myButton2=Button(myFrame1,text="2. Araba Sayısı",command=self.arabasayisi,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton2.pack(fill=BOTH)# 2. buton ve arabasayisi fonksiyonunun çalıştırıldığı yer

        self.myButton3=Button(myFrame1,text="3. Arabaların Özellikleri",command=self.arabaozellikleri,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton3.pack(fill=BOTH)# 3. buton ve arabaozellikleri fonksiyonunun çalıştırıldığı yer

        self.b2 = Entry(myFrame2,textvariable=self.mystr,width="30")
        self.b2.pack(side=LEFT,fill=BOTH)# kaç gün kiralanacak bilgisini alan 1. entry

        self.b3 = Entry(myFrame2,textvariable=self.mystr2,width="30")
        self.b3.pack(side=LEFT,fill=BOTH)# kaç saat kiralanacak bilgisini alan 2. entry

        self.b4 = Entry(myFrame2,textvariable=self.mystr3,width="30")
        self.b4.pack(side=LEFT,fill=BOTH)# hangi araba kiralanacak bilgisini alan 3. entry

        
        self.myButton4=Button(myFrame2,text="4. Araba Kirala ",command=self.arackirala,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton4.pack(fill=BOTH)# 3 entry nin yanındaki,arackirala fonksiyonunun çalıştırıldığı 4. buton

        self.myButton5=Button(myFrame3,text="5. Araba İade",command=self.araciade,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton5.pack(fill=BOTH)# 5. buton ve araciade fonksiyonunun çalıştırıldığı yer

        self.myButton6=Button(myFrame3,text="6. Kiralanan Araba",command=self.kiralananarac,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton6.pack(fill=BOTH)# 6. buton ve kiralananarac fonksiyonunun çalıştırıldığı yer

        self.myButton7=Button(myFrame3,text="7. Kiralama Süresi",command=self.kirasuresi,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton7.pack(fill=BOTH)# 7. buton ve kirasuresi fonksiyonunun çalıştırıldığı yer

        self.myButton8=Button(myFrame3,text="8. Çıkış",command=quit,font="GOTHAM 25 bold",fg="white",bg="gray")
        self.myButton8.pack(fill=BOTH)# 8. buton ve quit komutunun çalıştırıldığı yer

#######################################################################################################################################
    
    def arackirala(self):
        if len(self.b4.get()) == 0: # eğer araba markası yerine bilgi girilmezse gönderilicek hata
            print("Bilgileri düzgün girin")
            msg.showerror(title="HATA", message=f"Bilgileri düzgün girin")
        else: #eğer araba markası girilirse alınan entry ler kiralamasuresi fonksiyonuna gönderilicek         
            self.kiralamasuresi(int(self.b2.get()),int(self.b3.get()),self.b4.get().lower().capitalize().strip()) #self.b4.get() in yanında yazılanlar müşteri büyük,küçük harf yada boşluk girdiği zaman düzelticek 
            msg.showinfo(title="Araba Kiralama", message=f"{self.b4.get().lower().capitalize().strip()} Markalı Araba Kiralanmıştır.\nFiyatı {self.fiyat}\n{self.zaman}'a kadar kiralanacak.")

    def araciade(self):
        if len(self.b4.get()) == 0:# eğer araba markası yerine bilgi girilmezse gönderilicek hata
            print("Kiralanan araba yok")
            msg.showerror(title="HATA", message=f"Kiralanan araba yok")
        else: # eğer araba markası girilirse aracgerigetirme fonksiyonu çalışıcak ve yeni araba sayısı değerini return edecek. tekrar Araba Sayısı butonuna bakarak görebilirsiniz.
            self.aracgerigetirme(self.b4.get().lower().capitalize().strip())
            print("Araba Başarılı Şekilde İade Edildi.")
            msg.showinfo(title="Araba İade", message="Araba Başarılı Şekilde İade Edildi.")
            
    def kiralananarac(self):
        if len(self.b4.get()) == 0: # eğer araba kiralanmazsa gönderilicek hata
            print("Kiralanan araba yok")
            msg.showerror(title="HATA", message=f"Kiralanan araba yok")
        else:#eğer araba kiralanmışsa, kiralanan arabayı gösteririr
            print(f"{self.b4.get().lower().capitalize().strip()} markalı arabamız kiralanmıştır.")
            msg.showinfo(title="Kiralanan araba", message=f"Kiralanan arabamız = {self.b4.get().lower().capitalize().strip()}")

    def kirasuresi(self):
        if len(self.b4.get()) == 0: # eğer araba kiralanmazsa gönderilicek hata
            print("Kiralanan araba yok")
            msg.showerror(title="HATA", message=f"Kiralanan araba yok")
        else:#eğer araba kiralanmışsa arabanın markasıyla kan gün ve kaç saat kiralanmıştır onu gösterir
            print(f"Kiralama süresi= {self.b4.get()} markalı araba; {self.b2.get()} gün ve {self.b3.get()} saat kiralanmıştır.")
            msg.showinfo(title="Kiralama süresi", message=f"Kiralama süresi= {self.b4.get()} markalı araba; {self.b2.get()} gün ve {self.b3.get()} saat kiralanmıştır.")

a3 = musteri()  
win.mainloop()

