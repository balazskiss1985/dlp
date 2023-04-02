
from tkinter import *                           #Meghívjuk a tkinter-t
import math
import pyperclip
import tkinter.messagebox as msg

win = Tk()                                      #Létrehozunk egy Tk()objektumot
win.title("Effektív dózis kalkulátor ver. 1.0")          #Elnevezzük
win.geometry("1000x550")                         #Megadjuk a méretét
win.configure(bg="#f5edec")

#meg kell adni mit akarok, és azt a mit hova akarom

#változók
vizsgalat=0
kor=0

kt=0
kn=0
kk=0
mt=0
mn=0
mk=0
hkm=0
prem=0
mon=0
kkism=0
haskm=0
mht=0
ha=0
mhk=0
mhkt=0
mhkk=0
kop=0
mell=0
melfh=0
melhkm=0

koponya_DLP=0
mell_DLP=0 
mell_has_DLP=0 
mell_has_km_DLP=0
 
eff_dose_kop_mell_newborn=0
eff_dose_kop_mell_baby=0
eff_dose_kop_mell_toddler=0
eff_dose_kop_mell_child=0
eff_dose_kop_mell_adult=0

eff_dose_kop_mell_has_newborn=0 
eff_dose_kop_mell_has_baby=0 
eff_dose_kop_mell_has_toddler=0 
eff_dose_kop_mell_has_child=0 
eff_dose_kop_mell_has_adult=0 

eff_dose_kop_mell_has_km_newborn=0 
eff_dose_kop_mell_has_km_baby=0 
eff_dose_kop_mell_has_km_toddler=0 
eff_dose_kop_mell_has_km_child=0 
eff_dose_kop_mell_has_km_adult=0 

eff_dose_kop_newborn=0 
eff_dose_kop_baby=0 
eff_dose_kop_toddler=0 
eff_dose_kop_child=0 
eff_dose_kop_adult=0 

eff_dose_mell_newborn=0 
eff_dose_mell_baby=0 
eff_dose_mell_toddler=0 
eff_dose_mell_child=0 
eff_dose_mell_adult=0 

eff_dose_mell_has_km_newborn=0 
eff_dose_mell_has_km_baby=0 
eff_dose_mell_has_km_toddler=0 
eff_dose_mell_has_km_child=0 
eff_dose_mell_has_km_adult=0

eff_dose_has_km_newborn= 0
eff_dose_has_km_baby= 0
eff_dose_has_km_toddler= 0
eff_dose_has_km_child= 0
eff_dose_has_km_adult= 0 

total_DLP=0
   
#beköszönő szöveg
Label0 = Label(win, text="Üdvözlöm!", font="Helvetica 14 bold")
Label0.grid(row=0, column=0)

#szünet
Label_szunet1 = Label(win, text="", font="Helvetica 10", bg="#f5edec")
Label_szunet1.grid(row=1,column=0)

examination_type_row_1 = "koponya: k, koponya-mellkas: km, koponya-mellkas-has: kmh, koponya-mellkas-has-kismedence: kmhk, "
examination_type_row_2 = "mellkas: m, mellkas-has-kismedence: mhk, has-kismedence: hkm"

#BEKÉREM A VIZSGÁLAT TÍPUSÁT
Label1= Label(win, text="Kérem, adja meg a vizsgálat típusát", font="Helvetica 12 bold", bg="#f5edec")
Label1.grid(row=4, column=0)
Label2= Label(win, text=examination_type_row_1, font="Helvetica 12 bold", bg="#f5edec")
Label2.grid(row=5, column=0)
Label2b= Label(win, text=examination_type_row_2, font="Helvetica 12 bold", bg="#f5edec")
Label2b.grid(row=6, column=0) 

vizsgalat= Entry(win, font="Helvetica 12 bold", borderwidth=3)
vizsgalat.grid(row=4, column=1)
vizsgalat.get()   

#BEKÉREM AZ ÉLETKORT
Label3= Label(win, text="Kérem, adja meg a beteg életkorát", font="Helvetica 12 bold", bg="#f5edec")
Label3.grid(row=8, column=0)                                                                                

kor= Entry(win, font="Helvetica 12 bold", borderwidth=3)
kor.grid(row=8, column=1)
kor.get()

vizsgalat.focus()
vizsgalat.bind("<Return>", lambda funct1:kor.focus())
kor.bind("<Return>", lambda funct1:gomb.focus())

"""tovább gombra kattintva, megjelenik a vizsgálatnak megfelelő ablak def_myClick mondja meg, mit csináljon a tovább feliratú gomb
a global kulcsszóval valamennyi függvény számára elérhetővé teszem a vizsgalat, kor, koponya_DLP, mell_DLP, stb. értékeit a későbbi számoláshoz"""

def myClick():
    global vizsgalat
    global kor
    global kt
    global kn
    global kk
    global mt
    global mn
    global mk
    global mht
    global ha
    global mhk
    global mhkt
    global mhkk
    global kop
    global mell
    global melfh
    global melhkm
    global haskm
    global prem
    global mon
    global kkism
    
#tüntesse el a korábbi dolgokat az ablakból
    Label0.grid_forget()
    Label1.grid_forget()
    Label2.grid_forget()
    Label2b.grid_forget()
    Label3.grid_forget()
    kor.grid_forget()
    vizsgalat.grid_forget()
    gomb.grid_forget()
    
    my_label= Label(win, text="Kérem adja meg az alábbi adatokat", font= "Helvetica 16 bold", bg="#f5edec")
    my_label.grid(row=0, column=0, columnspan=2)
    
#BEKÉREM A VIZSÁLATNAK MEGFELELŐ DLP ÉRTÉKEKET 
#koponya-mellkas  
    if vizsgalat.get()=="km":
        Label4= Label(win, text="Kérem, adja meg a koponya topogram DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        kt= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kt.grid(row=2, column=1)
        
        Label5= Label(win, text="Kérem, adja meg a koponya nativ sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label5.grid(row=3, column=0)    
        kn=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kn.grid(row=3, column=1)

        Label7= Label(win, text="Kérem, adja meg a mellkas topogram DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label7.grid(row=4, column=0) 
        mt=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mt.grid(row=4, column=1)

        Label8= Label(win, text="Kérem, adja meg a mellkas nativ sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label8.grid(row=5, column=0)
        mn= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mn.grid(row=5, column=1)

        Label9= Label(win, text="Kérem, adja meg a mellkas kontrasztos sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label9.grid(row=6, column=0)
        mk=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mk.grid(row=6, column=1) 
        
        Label6= Label(win, text="Kérem, adja meg a koponya kontrasztos sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label6.grid(row=7, column=0)
        kk=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kk.grid(row=7, column=1)
       
        kt.focus()
        kt.bind("<Return>", lambda funct1:kn.focus())
        kn.bind("<Return>", lambda funct1:mt.focus())
        mt.bind("<Return>", lambda funct1:mn.focus())
        mn.bind("<Return>", lambda funct1:mk.focus())
        mk.bind("<Return>", lambda funct1:kk.focus())
        kk.bind("<Return>", lambda funct1:gomb_szamol.focus())

#koponya-mellkas-has    
    elif vizsgalat.get()=="kmh":
        Label4= Label(win, text="Kérem, adja meg a koponya topogram DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        kt= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kt.grid(row=2, column=1)
        
        Label5= Label(win, text="Kérem, adja meg a koponya nativ sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label5.grid(row=3, column=0)    
        kn=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kn.grid(row=3, column=1)
    
        Label7= Label(win, text="Kérem, adja meg a mellkas-has topogram DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label7.grid(row=4, column=0) 
        mht=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mht.grid(row=4, column=1)
        
        Label71= Label(win, text="Kérem, adja meg a premonitoring DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label71.grid(row=5, column=0) 
        prem=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        prem.grid(row=5, column=1)
        
        Label72= Label(win, text="Kérem, adja meg a monitoring DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label72.grid(row=6, column=0) 
        mon=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mon.grid(row=6, column=1)

        Label8= Label(win, text="Kérem, adja meg az artériás has sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label8.grid(row=7, column=0)
        ha= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        ha.grid(row=7, column=1)

        Label9= Label(win, text="Kérem, adja meg a mellkas-has kontrasztos sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label9.grid(row=8, column=0)
        mhk=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mhk.grid(row=8, column=1) 
        
        Label6= Label(win, text="Kérem, adja meg a koponya kontrasztos sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label6.grid(row=9, column=0)
        kk=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kk.grid(row=9, column=1)
        
        kt.focus()
        kt.bind("<Return>", lambda funct1:kn.focus())
        kn.bind("<Return>", lambda funct1:mht.focus())
        mht.bind("<Return>", lambda funct1:prem.focus())
        prem.bind("<Return>", lambda funct1:mon.focus())
        mon.bind("<Return>", lambda funct1:ha.focus())
        ha.bind("<Return>", lambda funct1:mhk.focus())
        mhk.bind("<Return>", lambda funct1:kk.focus())
        kk.bind("<Return>", lambda funct1:gomb_szamol.focus())

#koponya-mellkas-has-kismedence
    elif vizsgalat.get()=="kmhk":
        Label4= Label(win, text="Kérem, adja meg a koponya topogram DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        kt= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kt.grid(row=2, column=1)
        
        Label5= Label(win, text="Kérem, adja meg a koponya nativ sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label5.grid(row=3, column=0)    
        kn=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kn.grid(row=3, column=1)

        Label7= Label(win, text="Kérem, adja meg a mellkas-has-kismedece topogram DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label7.grid(row=4, column=0) 
        mhkt=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mhkt.grid(row=4, column=1)
        
        Label71= Label(win, text="Kérem, adja meg a premonitoring DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label71.grid(row=5, column=0) 
        prem=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        prem.grid(row=5, column=1)
        
        Label72= Label(win, text="Kérem, adja meg a monitoring DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label72.grid(row=6, column=0) 
        mon=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mon.grid(row=6, column=1)
        
        Label8= Label(win, text="Kérem, adja meg az artériás has sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label8.grid(row=7, column=0)
        ha= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        ha.grid(row=7, column=1)

        Label9= Label(win, text="Kérem, adja meg a mellkas-has-kismedece kontrasztos sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label9.grid(row=8, column=0)
        mhkk=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mhkk.grid(row=8, column=1) 
        
        Label6= Label(win, text="Kérem, adja meg a koponya kontrasztos sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label6.grid(row=9, column=0)
        kk=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kk.grid(row=9, column=1)
        
        Label6= Label(win, text="Kérem, adja meg a késői kismedence sorozat DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label6.grid(row=10, column=0)
        kkism=Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kkism.grid(row=10, column=1)
       
        kt.focus()
        kt.bind("<Return>", lambda funct1:kn.focus())
        kn.bind("<Return>", lambda funct1:mhkt.focus())
        mhkt.bind("<Return>", lambda funct1:prem.focus())
        prem.bind("<Return>", lambda funct1:mon.focus())
        mon.bind("<Return>", lambda funct1:ha.focus())
        ha.bind("<Return>", lambda funct1:mhkk.focus())
        mhkk.bind("<Return>", lambda funct1:kk.focus())
        kk.bind("<Return>", lambda funct1:kkism.focus())
        kkism.bind("<Return>", lambda funct1:gomb_szamol.focus())
        

#koponya        
    elif vizsgalat.get()=="k":
        Label4= Label(win, text="Kérem, adja meg a total DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        kop= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        kop.grid(row=2, column=1)
        
        kop.focus()
        kop.bind("<Return>", lambda funct1:gomb_szamol.focus()) 
        
#mellkas
    elif vizsgalat.get()=="m":
        Label4= Label(win, text="Kérem, adja meg a total DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        mell= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        mell.grid(row=2, column=1)
        
        mell.focus()
        mell.bind("<Return>", lambda funct1:gomb_szamol.focus())
        
#mellkas-has-kismedence
    elif vizsgalat.get()=="mhk":
        Label4= Label(win, text="Kérem, adja meg a total DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        melhkm= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        melhkm.grid(row=2, column=1)
        
        melhkm.focus()
        melhkm.bind("<Return>", lambda funct1:gomb_szamol.focus())
        
#mellkas-felhas
    elif vizsgalat.get()=="mh":
        Label4= Label(win, text="Kérem, adja meg a total DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        melfh= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        melfh.grid(row=2, column=1)
        
        melfh.focus()
        melfh.bind("<Return>", lambda funct1:gomb_szamol.focus())  
        
#has-kismedence        
    elif vizsgalat.get()=="hkm":
        Label4= Label(win, text="Kérem, adja meg a total DLP értékét", font="Helvetica 12 bold", bg="#f5edec")
        Label4.grid(row=2, column=0) 
        haskm= Entry(win, font="Helvetica 12 bold", borderwidth=5)
        haskm.grid(row=2, column=1)
        
        haskm.focus()
        haskm.bind("<Return>", lambda funct1:gomb_szamol.focus())

def myClick2():
    global koponya_DLP
    global mell_DLP
    global mell_has_DLP
    global mell_has_km_DLP
    
    gomb_szamol.grid_forget()
    
#koponya-mellkas    
    if vizsgalat.get()=="km":
        koponya_DLP= int(kt.get()) + int(kn.get()) + int(kk.get())
        koponya_DLP_label = Label(win, text="A koponya DLP értéke: ")
        koponya_DLP_label.config( text= "A koponya DLP értéke: " + str(koponya_DLP) , bg="#f5edec")
        koponya_DLP_label.grid(row=10, column=0, columnspan=2)

        mell_DLP= int(mt.get()) + int(mn.get()) + int(mk.get()) 
        mell_DLP_label = Label(win, text="A mellkas DLP értéke: ")
        mell_DLP_label.config( text= "A mellkas DLP értéke: " + str(mell_DLP), bg="#f5edec")
        mell_DLP_label.grid(row=11, column=0, columnspan=2)
        
#koponya-mellkas-has    
    elif vizsgalat.get()=="kmh":
        koponya_DLP= int(kt.get()) + int(kn.get()) + int(kk.get())
        koponya_DLP_label = Label(win, text="A koponya DLP értéke: ")
        koponya_DLP_label.config( text= "A koponya DLP értéke: " + str(koponya_DLP), bg="#f5edec")
        koponya_DLP_label.grid(row=10, column=0, columnspan=2)
        
        mell_has_DLP= int(mht.get()) + int(ha.get()) + int(mhk.get()) + int(prem.get())+ int(mon.get()) 
        mell_has_DLP_label = Label(win, text="A mellkas-has DLP értéke: ")
        mell_has_DLP_label.config( text= "A mellkas-has DLP értéke: " + str(mell_has_DLP), bg="#f5edec")
        mell_has_DLP_label.grid(row=11, column=0, columnspan=2)
        
#koponya-mellkas-has-kismedence        
    elif vizsgalat.get()=="kmhk":
        koponya_DLP= int(kt.get()) + int(kn.get()) + int(kk.get())
        koponya_DLP_label = Label(win, text="A koponya DLP értéke: ")
        koponya_DLP_label.config( text= "A koponya DLP értéke: " + str(koponya_DLP), bg="#f5edec")
        koponya_DLP_label.grid(row=11, column=0, columnspan=2)
        
        mell_has_km_DLP= int(mhkt.get()) + int(ha.get()) + int(mhkk.get())+ int(prem.get())+ int(mon.get())+ int(kkism.get())
        mell_has_km_DLP_label = Label(win, text="A mellkas-has-kismedence DLP értéke: ")
        mell_has_km_DLP_label.config( text= "A mellkas-has-kismedence DLP értéke: " + str(mell_has_km_DLP), bg="#f5edec")
        mell_has_km_DLP_label.grid(row=12, column=0, columnspan=2)      
      
def myClick3():
    global eff_dose_kop_mell_newborn
    global eff_dose_kop_mell_baby
    global eff_dose_kop_mell_toddler
    global eff_dose_kop_mell_child
    global eff_dose_kop_mell_adult
    
    global eff_dose_kop_mell_has_newborn
    global eff_dose_kop_mell_has_baby
    global eff_dose_kop_mell_has_toddler
    global eff_dose_kop_mell_has_child
    global eff_dose_kop_mell_has_adult
    
    global eff_dose_kop_mell_has_km_newborn
    global eff_dose_kop_mell_has_km_baby
    global eff_dose_kop_mell_has_km_toddler
    global eff_dose_kop_mell_has_km_child
    global eff_dose_kop_mell_has_km_adult
    
    global eff_dose_kop_newborn
    global eff_dose_kop_baby
    global eff_dose_kop_toddler
    global eff_dose_kop_child
    global eff_dose_kop_adult
    
    global eff_dose_mell_newborn
    global eff_dose_mell_baby
    global eff_dose_mell_toddler
    global eff_dose_mell_child
    global eff_dose_mell_adult
    
    global eff_dose_mell_has_km_newborn
    global eff_dose_mell_has_km_baby
    global eff_dose_mell_has_km_toddler
    global eff_dose_mell_has_km_child
    global eff_dose_mell_has_km_adult
    
    global eff_dose_has_km_newborn
    global eff_dose_has_km_baby
    global eff_dose_has_km_toddler
    global eff_dose_has_km_child
    global eff_dose_has_km_adult

    global koponya_DLP
    global mell_DLP
    global mell_has_DLP
    global mell_has_km_DLP
    global total_DLP
    
    gomb_dose.grid_forget()
      
    if (vizsgalat.get()=="km") & (kor.get()== "0"):
        eff_dose_kop_mell_newborn= (int(koponya_DLP) * 0.011) + (int(mell_DLP) * 0.039)
        eff_dose_kop_mell_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_newborn), bg="#f5edec")
        eff_dose_kop_mell_newborn_label.grid(row=12, column=0, columnspan=2)
        
        total_DLP= int(koponya_DLP) + int(mell_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="km") & (kor.get()<="1"):
        eff_dose_kop_mell_baby= int(koponya_DLP) * 0.0067 + int(mell_DLP) * 0.026
        eff_dose_kop_mell_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_baby), bg="#f5edec")
        eff_dose_kop_mell_baby_label.grid(row=12, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="km") & (kor.get()<="5"):
        eff_dose_kop_mell_toddler=int(koponya_DLP) * 0.004 + int(mell_DLP) * 0.018
        eff_dose_kop_mell_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_toddler), bg="#f5edec")
        eff_dose_kop_mell_toddler_label.grid(row=12, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="km") & (kor.get()<="10"):    
        eff_dose_kop_mell_child= int(koponya_DLP) * 0.003+int(mell_DLP) * 0.013
        eff_dose_kop_mell_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_child), bg="#f5edec")
        eff_dose_kop_mell_child_label.grid(row=12, column=0, columnspan=2)
        
        total_DLP= int(koponya_DLP) + int(mell_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)  
        
    elif (vizsgalat.get()=="km") & (kor.get()>"10"):
        eff_dose_kop_mell_adult= int(koponya_DLP) * 0.0021 + int(mell_DLP) * 0.014
        eff_dose_kop_mell_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_adult), bg="#f5edec")
        eff_dose_kop_mell_adult_label.grid(row=12, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
#koponya-mellkas-has    
    elif (vizsgalat.get()=="kmh") & (kor.get()== "0"):
        eff_dose_kop_mell_has_newborn= int(koponya_DLP) * 0.011 + int(mell_has_DLP)*0.044
        eff_dose_kop_mell_has_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_newborn), bg="#f5edec")
        eff_dose_kop_mell_has_newborn_label.grid(row=12, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmh") & (kor.get()<="1"):
        eff_dose_kop_mell_has_baby= (int(koponya_DLP) * 0.0067)+(int(mell_has_DLP)*0.028)
        eff_dose_kop_mell_has_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_baby), bg="#f5edec")
        eff_dose_kop_mell_has_baby_label.grid(row=12, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmh") & (kor.get()<="5"):
        eff_dose_kop_mell_has_toddler=(int(koponya_DLP) * 0.004)+(int(mell_has_DLP)*0.019)
        eff_dose_kop_mell_has_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_toddler), bg="#f5edec")
        eff_dose_kop_mell_has_toddler_label.grid(row=12, column=0, columnspan=2)
        
        total_DLP= int(koponya_DLP) + int(mell_has_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)    
        
    elif (vizsgalat.get()=="kmh") & (kor.get()<="10"):    
        eff_dose_kop_mell_has_child= (int(koponya_DLP) * 0.0032)+(int(mell_has_DLP)*0.014) 
        eff_dose_kop_mell_has_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_child), bg="#f5edec")
        eff_dose_kop_mell_has_child_label.grid(row=12, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmh") & (kor.get()>"10"):
        eff_dose_kop_mell_has_adult= (int(koponya_DLP) * 0.0021)+(int(mell_has_DLP)*0.015)
        eff_dose_kop_mell_has_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_adult), bg="#f5edec")
        eff_dose_kop_mell_has_adult_label.grid(row=12, column=0, columnspan=2)    
       
        total_DLP= int(koponya_DLP) + int(mell_has_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=13, column=0, columnspan=2)     
        
#koponya-mellkas-has-kismedence        
    elif (vizsgalat.get()=="kmhk") & (kor.get()== "0"):
        eff_dose_kop_mell_has_km_newborn= (int(koponya_DLP) * 0.011)+(int(mell_has_km_DLP)*0.044)
        eff_dose_kop_mell_has_km_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_km_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_km_newborn), bg="#f5edec")
        eff_dose_kop_mell_has_km_newborn_label.grid(row=13, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_km_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=14, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()<="1"):
        eff_dose_kop_mell_has_km_baby= (int(koponya_DLP) * 0.0067)+(int(mell_has_km_DLP)*0.028)
        eff_dose_kop_mell_has_km_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_km_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_km_baby), bg="#f5edec")
        eff_dose_kop_mell_has_km_baby_label.grid(row=13, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_km_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=14, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()<="5"):
        eff_dose_kop_mell_has_km_toddler=(int(koponya_DLP) * 0.004)+(int(mell_has_km_DLP)*0.019) 
        eff_dose_kop_mell_has_km_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_km_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_km_toddler), bg="#f5edec")
        eff_dose_kop_mell_has_km_toddler_label.grid(row=13, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_km_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=14, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()<="10"):    
        eff_dose_kop_mell_has_km_child= (int(koponya_DLP) * 0.0032)+(int(mell_has_km_DLP)*0.014)
        eff_dose_kop_mell_has_km_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_km_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_km_child), bg="#f5edec")
        eff_dose_kop_mell_has_km_child_label.grid(row=13, column=0, columnspan=2)

        total_DLP= int(koponya_DLP) + int(mell_has_km_DLP)
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=14, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()>"10"):
        eff_dose_kop_mell_has_km_adult=(int(koponya_DLP) * 0.0021)+(int(mell_has_km_DLP)*0.015)
        eff_dose_kop_mell_has_km_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_mell_has_km_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_mell_has_km_adult), bg="#f5edec")
        eff_dose_kop_mell_has_km_adult_label.grid(row=13, column=0, columnspan=2) 

        total_DLP= int(mell_has_km_DLP)+ int(koponya_DLP) 
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=14, column=0, columnspan=2)
        
#koponya
    elif (vizsgalat.get()=="k") & (kor.get()== "0"):
        eff_dose_kop_newborn= int(kop.get())* 0.011 
        eff_dose_kop_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_newborn), bg="#f5edec")
        eff_dose_kop_newborn_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(kop.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="k") & (kor.get()<="1"):
        eff_dose_kop_baby= int(kop.get())* 0.0067
        eff_dose_kop_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_baby), bg="#f5edec")
        eff_dose_kop_baby_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(kop.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="k") & (kor.get()<="5"):
        eff_dose_kop_toddler=int(kop.get()) * 0.004
        eff_dose_kop_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_toddler), bg="#f5edec")
        eff_dose_kop_toddler_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(kop.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="k") & (kor.get()<="10"):    
        eff_dose_kop_child= int(kop.get())* 0.0032
        eff_dose_kop_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_child), bg="#f5edec")
        eff_dose_kop_child_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(kop.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="k") & (kor.get()>"10"):
        eff_dose_kop_adult=int(kop.get()) * 0.0021
        eff_dose_kop_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_kop_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_kop_adult), bg="#f5edec")
        eff_dose_kop_adult_label.grid(row=10, column=0, columnspan=2) 

        total_DLP= int(kop.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
#mellkas        
    elif (vizsgalat.get()=="m") & (kor.get()== "0"):
        eff_dose_mell_newborn= int(mell.get())* 0.039 
        eff_dose_mell_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_newborn), bg="#f5edec")
        eff_dose_mell_newborn_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(mell.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="m") & (kor.get()<="1"):
        eff_dose_mell_baby= int(mell.get())* 0.026
        eff_dose_mell_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_baby), bg="#f5edec")
        eff_dose_mell_baby_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(mell.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="m") & (kor.get()<="5"):
        eff_dose_mell_toddler=int(mell.get()) * 0.018
        eff_dose_mell_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_toddler), bg="#f5edec")
        eff_dose_mell_toddler_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(mell.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="m") & (kor.get()<="10"):    
        eff_dose_mell_child= int(mell.get())* 0.013
        eff_dose_mell_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_child), bg="#f5edec")
        eff_dose_mell_child_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(mell.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="m") & (kor.get()>"10"):
        eff_dose_mell_adult=int(mell.get()) * 0.014
        eff_dose_mell_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_adult), bg="#f5edec")
        eff_dose_mell_adult_label.grid(row=10, column=0, columnspan=2) 

        total_DLP= int(mell.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
#mellkas-has-kismedence
    elif (vizsgalat.get()=="mhk") & (kor.get()== "0"):
        eff_dose_mell_has_km_newborn= int(melhkm.get())* 0.044 
        eff_dose_mell_has_km_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_has_km_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_has_km_newborn), bg="#f5edec")
        eff_dose_mell_has_km_newborn_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(melhkm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()<="1"):
        eff_dose_mell_has_km_baby= int(melhkm.get())* 0.028
        eff_dose_mell_has_km_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_has_km_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_has_km_baby), bg="#f5edec")
        eff_dose_mell_has_km_baby_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(melhkm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()<="5"):
        eff_dose_mell_has_km_toddler=int(melhkm.get()) * 0.019
        eff_dose_mell_has_km_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_has_km_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_has_km_toddler), bg="#f5edec")
        eff_dose_mell_has_km_toddler_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(melhkm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()<="10"):    
        eff_dose_mell_has_km_child= int(melhkm.get())* 0.014
        eff_dose_mell_has_km_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_has_km_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_has_km_child), bg="#f5edec")
        eff_dose_mell_has_km_child_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(melhkm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()>"10"):
        eff_dose_mell_has_km_adult=int(melhkm.get()) * 0.015
        eff_dose_mell_has_km_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_mell_has_km_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_mell_has_km_adult), bg="#f5edec")
        eff_dose_mell_has_km_adult_label.grid(row=10, column=0, columnspan=2) 

        total_DLP= int(melhkm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
#has-kismedence
    elif (vizsgalat.get()=="hkm") & (kor.get()== "0"):
        eff_dose_has_km_newborn= int(haskm.get())* 0.049 
        eff_dose_has_km_newborn_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_has_km_newborn_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_has_km_newborn), bg="#f5edec")
        eff_dose_has_km_newborn_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(haskm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()<="1"):
        eff_dose_has_km_baby= int(haskm.get())* 0.03
        eff_dose_has_km_baby_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_has_km_baby_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_has_km_baby), bg="#f5edec")
        eff_dose_has_km_baby_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(haskm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()<="5"):
        eff_dose_has_km_toddler= int(haskm.get()) * 0.02
        eff_dose_has_km_toddler_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_has_km_toddler_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_has_km_toddler), bg="#f5edec")
        eff_dose_has_km_toddler_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(haskm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()<="10"):    
        eff_dose_has_km_child= int(haskm.get())* 0.015
        eff_dose_has_km_child_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_has_km_child_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_has_km_child), bg="#f5edec")
        eff_dose_has_km_child_label.grid(row=10, column=0, columnspan=2)

        total_DLP= int(haskm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()>"10"):
        eff_dose_has_km_adult=int(haskm.get()) * 0.015
        eff_dose_has_km_adult_label = Label(win, text="Az effektív dózis értéke: ")
        eff_dose_has_km_adult_label.config( text= "Az effektív dózis értéke: " + str(eff_dose_has_km_adult), bg="#f5edec")
        eff_dose_has_km_adult_label.grid(row=10, column=0, columnspan=2)
        
        total_DLP= int(haskm.get())
        total_DLP_label = Label(win, text="A total DLP értéke: ")
        total_DLP_label.config( text= "A total DLP értéke: " + str(total_DLP), bg="#f5edec")
        total_DLP_label.grid(row=11, column=0, columnspan=2)
        
        
Label_szunet1 = Label(win, text="", font="Helvetica 6", bg="#f5edec")
Label_szunet1.grid(row=15,column=0)
  
gomb = Button(win, text="Tovább", padx=50, bg="#f4f1f0", command=myClick)
gomb.grid(row=16, column=0, columnspan=3)

Label_szunet1 = Label(win, text="", font="Helvetica 6", bg="#f5edec")
Label_szunet1.grid(row=17,column=0)

gomb_szamol = Button(win, text="DLP számolása", padx=50, bg="#f4f1f0", command=myClick2) 
gomb_szamol.grid(row=18, column=0, columnspan=3)

Label_szunet1 = Label(win, text="", font="Helvetica 6", bg="#f5edec")
Label_szunet1.grid(row=19,column=0)

gomb_dose = Button (win, text="Dózis számolása", padx=50, bg="#f4f1f0", command=myClick3) 
gomb_dose.grid(row=20, column=0, columnspan=3)
    
def open_popup():

    popup= Toplevel(win)
    popup.title= ("Eredmény")
    popup.geometry("700x400")
    popup.config(bg="#f6efee")
       
    Label0= Label(popup, text="A kalkuláció eredménye:", font="Helvetica 16 bold")
    Label0.grid(row=0, column=0)
    
    Label_szunet2 = Label(popup, text="", font="Helvetica 12", bg="#f5edec")
    Label_szunet2.grid(row=1,column=0)
    
# MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) és kiírom az eredményt
#koponya-mellkas
    if (vizsgalat.get()=="km") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_kop_mell_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
        
    elif (vizsgalat.get()=="km") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="km") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="km") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="km") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=2, column=0)
        
#koponya-mellkas-has        
    elif (vizsgalat.get()=="kmh") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_kop_mell_has_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="kmh") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="kmh") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="kmh") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="kmh") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
#koponya-mellkas-has-kismedence        
    elif (vizsgalat.get()=="kmhk") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_kop_mell_has_km_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_km_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_km_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_km_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="kmhk") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_mell_has_km_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
#koponya    
    elif (vizsgalat.get()=="k") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_kop_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="k") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="k") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="k") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="k") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_kop_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
#mellkas    
    elif (vizsgalat.get()=="m") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_mell_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="m") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="m") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="m") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="m") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 

#mellkas-has-kismedence
    elif (vizsgalat.get()=="mhk") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_mell_has_km_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_has_km_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_has_km_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="mhk") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_has_km_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="mhk") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_mell_has_km_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)

#has-kismedence
    elif (vizsgalat.get()=="hkm") & (kor.get()== "0"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis: " + str(eff_dose_has_km_newborn) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()<="1"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_has_km_baby) + " mSv.", font="Helvetica 14 bold", bg="#f6efee") 
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()<="5"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_has_km_toddler) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)
        
    elif (vizsgalat.get()=="hkm") & (kor.get()<="10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_has_km_child) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0) 
        
    elif (vizsgalat.get()=="hkm") & (kor.get()>"10"):
        Label1a= Label(popup, text="A total DLP: " + str(total_DLP) + " mGycm.", font="Helvetica 14 bold", bg="#f6efee")
        Label1a.grid(row=2, column=0)
        
        Label1= Label(popup, text="A kalkulált effektív dózis " + str(eff_dose_has_km_adult) + " mSv.", font="Helvetica 14 bold", bg="#f6efee")
        Label1.grid(row=3, column=0)         
        
    Label_szunet3 = Label(popup, text="", font="Helvetica 20", bg="#f5edec")
    Label_szunet3.grid(row=5,column=0)
    
    Label_hivatkozas1= Label(popup, text="A kalkulátor által számolt értékek megközelítőlegesek.", font="Helvetica 10 bold", bg="#f6efee") 
    Label_hivatkozas1.grid(row=5, column=0)
    Label_hivatkozas_text= "A kalkulátor által számolt értékek megközelítőlegesek. A számításhoz szükséges k konverziós faktor a The Measurement, Reporting, and Management of Radiation Dose in CT- Report of AAPM Task Group 23: CT Dosimetry-Diagnostic Imaging Council CT Committee alapján lett beállítva"
    Label_hivatkozas2= Label(popup, text="A számításhoz szükséges k konverziós faktor a", font="Helvetica 10 bold", bg="#f6efee") 
    Label_hivatkozas2.grid(row=6, column=0)
    Label_hivatkozas3= Label(popup, text="The Measurement, Reporting, and Management of Radiation Dose in CT- Report of AAPM Task Group 23: ", font="Helvetica 10 bold", bg="#f6efee")
    Label_hivatkozas3.grid(row=7, column=0)
    Label_hivatkozas4= Label(popup, text="CT Dosimetry-Diagnostic Imaging Council CT Committee alapján lett beállítva", font="Helvetica 10 bold", bg="#f6efee")
    Label_hivatkozas4.grid(row=8, column=0)
    
    Label_szunet4 = Label(popup, text="", font="Helvetica 20", bg="#f5edec")
    Label_szunet4.grid(row=9,column=0)
    
    
    """
    def copy_to_clipboard(popup):
        root = Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(popup)
        root.update()  
    
    def copy_to_clipboard(popup):
        win.clipboard_append(popup)

        text = Label(popup, text= popup.cget())
        copy_to_clipboard(text)


    copy_button = Button(popup, text="Másolás a vágólapra", command=copy_to_clipboard(popup))
    copy_button.grid(row=11, column=0, columnspan=3) 
    """
    print(popup)
    gomb_quit = Button(popup, text="Kilépés a programból", padx=50, bg="#f4f1f0", command=popup.quit) 
    gomb_quit.grid(row=12, column=0, columnspan=3)        
        
    popup.mainloop()
                   
Label_szunet5 = Label(win, text="", font="Helvetica 12", bg="#f5edec")
Label_szunet5.grid(row=22,column=0)

gomb2= Button(win, text="Eredmény", padx=50,  bg="#f4f1f0", command=open_popup)
gomb2.grid(row=23, column=0, columnspan=3)

Label_szunet6 = Label(win, text="", font="Helvetica 12", bg="#f5edec")
Label_szunet6.grid(row=24,column=0)
              
gomb_quit = Button(win, text="Kilépés a programból", padx=50,  bg="#f4f1f0", command=win.quit) 
gomb_quit.grid(row=25, column=0, columnspan=3)

win.mainloop()                                  # Ezzel bele tudunk lépni a fő applikációs ciklusba
