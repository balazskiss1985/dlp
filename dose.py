
# Online Python - IDE, Editor, Compiler, Interpreter

print ("Üdvözlöm! Kérem, adja meg a vizsgálat típusát(koponya:k, koponya-mellkas:km, koponya-mellkas-has:kmh, koponya-mellkas-has-kismedence:kmhk, mellkas:m, embolia: e, mellkas-felhas:mh, mellkas-has-kismedence: mhk, has-kismedence: hkm"); 
vizsgalat=input ()                                                                                                  #BEKÉREM A VIZSGÁLAT TÍPUSÁT
print ("Kérem, adja meg a beteg életkorát")                                                                                #BEKÉREM AZ ÉLETKORT
kor=input()
 

#KOPONYA-MELLKAS
if vizsgalat=="km" :                                                                            #BEKÉREM A VIZSÁLATNAK MEGFELELŐ DLP ÉRTÉKEKET, MAJD EZEKET ÖSSZEADOM
    print("Kérem, adja meg a koponya topogram DLP értékét, majd nyomjon Enter-t")
    kt= input()
    kop_topo_DLP= float (kt) 
    
    print("Kérem, adja meg a koponya nativ sorozat DLP értékét, majd nyomjon Enter-t")
    kn=input()
    kop_nativ_DLP= float(kn)
    
    print("Kérem, adja meg a koponya kontraszt DLP értékét, majd nyomjon Enter-t")
    kk=input()
    kop_kontraszt_DLP= float(kk)
    
    koponya_DLP= kop_topo_DLP + kop_nativ_DLP + kop_kontraszt_DLP    

    print("Kérem, adja meg a mellkas topogram DLP értékét, majd nyomjon Enter-t")
    mt=input()
    mell_topo_DLP= float(mt)
    
    print("Kérem, adja meg a mellkas nativ sorozat DLP értékét, majd nyomjon Enter-t")
    mn= input()
    mell_nativ_DLP= float(mn)
    
    print("Kérem, adja meg a mellkas kontraszt DLP értékét, majd nyomjon Enter-t")
    mk=input()
    mell_kontraszt_DLP= float(mk)
    mell_DLP= mell_topo_DLP + mell_nativ_DLP + mell_kontraszt_DLP 

    eff_dose_kop_mell_newborn= (koponya_DLP * 0.011)+(mell_DLP*0.039)                   # KISZÁMOLTATOM AZ ÖSSZES KOPONYA_MELLKAS DLP-T, MINDEN ESETRE
    eff_dose_kop_mell_baby= (koponya_DLP * 0.0067)+(mell_DLP*0.026) 
    eff_dose_kop_mell_toddler=(koponya_DLP * 0.004)+(mell_DLP*0.018) 
    eff_dose_kop_mell_child= (koponya_DLP * 0.0032)+(mell_DLP*0.013) 
    eff_dose_kop_mell_adult= (koponya_DLP * 0.0021)+(mell_DLP*0.014) 
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="km") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas vizsgálata esetében:", eff_dose_kop_mell_newborn ,"mSv")
    elif (vizsgalat=="km") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas vizsgálata esetében:", eff_dose_kop_mell_baby ,"mSv")
    elif (vizsgalat=="km") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas vizsgálata esetében:", eff_dose_kop_mell_toddler ,"mSv")
    elif (vizsgalat=="km") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas vizsgálata esetében:", eff_dose_kop_mell_child ,"mSv")    
    elif (vizsgalat=="km") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas vizsgálata esetében:", eff_dose_kop_mell_adult ,"mSv")


#KOPONYA-MELLKAS-HAS
elif vizsgalat=="kmh":                                                                                                   #BEKÉREM A VIZSÁLATNAK MEGFELELŐ DLP ÉRTÉKEKET, MAJD EZEKET ÖSSZEADOM
    print("Kérem, adja meg a koponya topogram DLP értékét, majd nyomjon Enter-t")
    kt= input()
    kop_topo_DLP= float(kt)
    
    print("Kérem, adja meg a koponya nativ sorozat DLP értékét, majd nyomjon Enter-t")
    kn=input()
    kop_nativ_DLP= float(kn)
    
    print("Kérem, adja meg a koponya kontrasztos sorozat DLP értékét, majd nyomjon Enter-t")
    kk=input()
    kop_kontraszt_DLP= float(kk)
    koponya_DLP= kop_topo_DLP + kop_nativ_DLP + kop_kontraszt_DLP
    
    print("Kérem, adja meg a mellkas-has topogram DLP értékét, majd nyomjon Enter-t")
    mht=input()
    mell_has_topo_DLP= float(mht)
    
    print("Kérem, adja meg az artériás has sorozat DLP értékét, majd nyomjon Enter-t")
    ha=input()
    has_art_DLP= float(ha)
    
    print("Kérem, adja meg a mellkas-has kontrasztos sorozat DLP értékét, majd nyomjon Enter-t")
    mhk= input()
    mell_has_kontraszt_DLP= float(mhk)
    
    mell_has_DLP= mell_has_topo_DLP + has_art_DLP + mell_has_kontraszt_DLP 
    
    eff_dose_kop_mell_has_newborn= (koponya_DLP * 0.011)+(mell_has_DLP*0.044)                   # KISZÁMOLTATOM AZ ÖSSZES KOPONYA_MELLKAS_HAS DLP-T, MINDEN ESETRE
    eff_dose_kop_mell_has_baby= (koponya_DLP * 0.0067)+(mell_has_DLP*0.028) 
    eff_dose_kop_mell_has_toddler=(koponya_DLP * 0.004)+(mell_has_DLP*0.019) 
    eff_dose_kop_mell_has_child= (koponya_DLP * 0.0032)+(mell_has_DLP*0.014) 
    eff_dose_kop_mell_has_adult= (koponya_DLP * 0.0021)+(mell_has_DLP*0.015) 
    
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="kmh") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has vizsgálata esetében:", eff_dose_kop_mell_has_newborn ,"mSv")
    elif (vizsgalat=="kmh") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has vizsgálata esetében:", eff_dose_kop_mell_has_baby ,"mSv")
    elif (vizsgalat=="kmh") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has vizsgálata esetében:", eff_dose_kop_mell_has_toddler ,"mSv")
    elif (vizsgalat=="kmh") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has vizsgálata esetében:", eff_dose_kop_mell_has_child ,"mSv")    
    elif (vizsgalat=="kmh") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has vizsgálata esetében:", eff_dose_kop_mell_has_adult ,"mSv")

#KOPONYA-MELLKAS-HAS-KISMEDENCE
elif vizsgalat=="kmhk":                                                                                                   #BEKÉREM A VIZSÁLATNAK MEGFELELŐ DLP ÉRTÉKEKET, MAJD EZEKET ÖSSZEADOM
    print("Kérem, adja meg a koponya topogram DLP értékét, majd nyomjon Enter-t")
    kt= input()
    kop_topo_DLP= float(kt)
    print("Kérem, adja meg a koponya nativ sorozat DLP értékét, majd nyomjon Enter-t")
    kn= input()
    kop_nativ_DLP= float(kt)
    
    print("Kérem, adja meg a koponya kontraszt DLP értékét, majd nyomjon Enter-t")
    kk= input()
    kop_kontraszt_DLP= float(kk)
    koponya_DLP= kop_topo_DLP + kop_nativ_DLP + kop_kontraszt_DLP
    
    print("Kérem, adja meg a mellkas-has-kismedece topogram DLP értékét, majd nyomjon Enter-t")
    mhkt=input()
    mell_has_km_topo_DLP= float(mhkt)
    
    print("Kérem, adja meg az artériás has sorozat DLP értékét, majd nyomjon Enter-t")
    ha=input()
    has_art_DLP= float(ha)
    
    print("Kérem, adja meg a mellkas-has-kismedece kontrasztos sorozat DLP értékét, majd nyomjon Enter-t")
    mhkk= input()
    mell_has_km_kontraszt_DLP= float(mhkk)
    
    mell_has_km_DLP= mell_has_km_topo_DLP + has_art_DLP + mell_has_km_kontraszt_DLP
    
    eff_dose_kop_mell_has_km_newborn= (koponya_DLP * 0.011)+(mell_has_DLP*0.044)                   # KISZÁMOLTATOM AZ ÖSSZES KOPONYA_MELLKAS_HAS DLP-T, MINDEN ESETRE
    eff_dose_kop_mell_has_km_baby= (koponya_DLP * 0.0067)+(mell_has_DLP*0.028) 
    eff_dose_kop_mell_has_km_toddler=(koponya_DLP * 0.004)+(mell_has_DLP*0.019) 
    eff_dose_kop_mell_has_km_child= (koponya_DLP * 0.0032)+(mell_has_DLP*0.014) 
    eff_dose_kop_mell_has_km_adult= (koponya_DLP * 0.0021)+(mell_has_DLP*0.015) 
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="kmhk") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has-kismedence vizsgálata esetében:",  eff_dose_kop_mell_has_km_newborn ,"mSv")
    elif (vizsgalat=="kmhk") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has-kismedence vizsgálata esetében:", eff_dose_kop_mell_has_km_baby ,"mSv")
    elif (vizsgalat=="kmhk") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has-kismedence vizsgálata esetében:", eff_dose_kop_mell_has_km_toddler ,"mSv")
    elif (vizsgalat=="kmhk") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has-kismedence vizsgálata esetében:", eff_dose_kop_mell_has_km_child ,"mSv")    
    elif (vizsgalat=="kmhk") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya-mellkas-has-kismedence vizsgálata esetében:", eff_dose_kop_mell_has_km_adult ,"mSv")

#HA NEM KOPONYA+VALAMI, BEKÉREM A SIMA DLP-T
else :                                                                                                                      
    print ("Kérem, adja meg a DLP-t, majd nyomjon Enter-t")
    a= input()
    DLP=float (a)
    
#KOPONYA
    eff_dose_kop_newborn= DLP * 0.011                   # KISZÁMOLTATOM AZ ÖSSZES KOPONYA DLP-T, MINDEN ESETRE
    eff_dose_kop_baby= DLP * 0.0067
    eff_dose_kop_toddler= DLP * 0.004
    eff_dose_kop_child= DLP * 0.0032
    eff_dose_kop_adult= DLP * 0.0021
    
    # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="k") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya vizsgálata esetében:", eff_dose_kop_newborn ,"mSv")
    elif (vizsgalat=="k") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya vizsgálata esetében:", eff_dose_kop_baby ,"mSv")
    elif (vizsgalat=="k") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya vizsgálata esetében:", eff_dose_kop_toddler ,"mSv")
    elif (vizsgalat=="k") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya vizsgálata esetében:", eff_dose_kop_child ,"mSv")    
    elif (vizsgalat=="k") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens koponya vizsgálata esetében:", eff_dose_kop_adult ,"mSv")
    
#MELLKAS
    eff_dose_mell_newborn= DLP * 0.039                   # KISZÁMOLTATOM AZ ÖSSZES MELLKAS DLP-T, MINDEN ESETRE
    eff_dose_mell_baby= DLP * 0.026
    eff_dose_mell_toddler= DLP * 0.018
    eff_dose_mell_child= DLP * 0.013
    eff_dose_mell_adult= DLP * 0.014
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="m") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas vizsgálata esetében:", eff_dose_mell_newborn ,"mSv")
    elif (vizsgalat=="m") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas vizsgálata esetében:", eff_dose_mell_baby ,"mSv")
    elif (vizsgalat=="m") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas vizsgálata esetében:", eff_dose_mell_toddler ,"mSv")
    elif (vizsgalat=="m") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas vizsgálata esetében:", eff_dose_mell_child ,"mSv")    
    elif (vizsgalat=="m") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas vizsgálata esetében:", eff_dose_mell_adult ,"mSv")
        
#MELLKAS-HAS-KISMEDENCE
    eff_dose_mell_has_km_newborn= DLP * 0.044                   # KISZÁMOLTATOM AZ ÖSSZES MELLKAS-HAS-KISMEDENCE DLP-T, MINDEN ESETRE
    eff_dose_mell_has_km_baby= DLP * 0.028
    eff_dose_mell_has_km_toddler= DLP * 0.019
    eff_dose_mell_has_km_child= DLP * 0.014
    eff_dose_mell_has_km_adult= DLP * 0.015
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="mhk") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas-has-kismedece vizsgálata esetében:", eff_dose_mell_has_km_newborn ,"mSv")
    elif (vizsgalat=="mhk") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas-has-kismedece vizsgálata esetében:", eff_dose_mell_has_km_baby ,"mSv")
    elif (vizsgalat=="mhk") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas-has-kismedece vizsgálata esetében:", eff_dose_mell_has_km_toddler ,"mSv")
    elif (vizsgalat=="mhk") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas-has-kismedece vizsgálata esetében:", eff_dose_mell_has_km_child ,"mSv")    
    elif (vizsgalat=="mhk") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkas-has-kismedece vizsgálata esetében:", eff_dose_mell_has_km_adult ,"mSv")
        
#HAS-KISMEDENCE
    eff_dose_has_km_newborn= DLP * 0.049                   # KISZÁMOLTATOM AZ ÖSSZES HAS-KISMEDENCE DLP-T, MINDEN ESETRE
    eff_dose_has_km_baby= DLP * 0.03
    eff_dose_has_km_toddler= DLP * 0.02
    eff_dose_has_km_child= DLP * 0.015
    eff_dose_has_km_adult= DLP * 0.015
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="hkm") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens has-kismedence vizsgálata esetében:", eff_dose_has_km_newborn ,"mSv")
    elif (vizsgalat=="hkm") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens has-kismedence vizsgálata esetében:", eff_dose_has_km_baby ,"mSv")
    elif (vizsgalat=="hkm") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens has-kismedence vizsgálata esetében:", eff_dose_has_km_toddler ,"mSv")
    elif (vizsgalat=="hkm") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens has-kismedence vizsgálata esetében:", eff_dose_has_km_child ,"mSv")    
    elif (vizsgalat=="hkm") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens has-kismedence vizsgálata esetében:", eff_dose_has_km_adult ,"mSv")

#EMBOLIA
    eff_dose_emb_newborn= DLP * 0.039                   # KISZÁMOLTATOM AZ ÖSSZES MELLKAS DLP-T, MINDEN ESETRE
    eff_dose_emb_baby= DLP * 0.026
    eff_dose_emb_toddler= DLP * 0.018
    eff_dose_emb_child= DLP * 0.013
    eff_dose_emb_adult= DLP * 0.014
    
     # MEGADOM IF-EKKEL A FELTÉTELEKET (ÉLETKOR, RÉGIÓ, STB) ÉS BEÍROM A SZORZÁSOKAT
    if (vizsgalat=="e") & (kor== "0"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkasi angio (embolia) vizsgálata esetében:", eff_dose_emb_newborn ,"mSv")
    elif (vizsgalat=="e") & (kor<="1"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkasi angio (embolia) vizsgálata esetében:", eff_dose_emb_baby ,"mSv")
    elif (vizsgalat=="e") & (kor<="5"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkasi angio (embolia) vizsgálata esetében:", eff_dose_emb_toddler ,"mSv")
    elif (vizsgalat=="e") & (kor<="10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkasi angio (embolia) vizsgálata esetében:", eff_dose_emb_child ,"mSv")    
    elif (vizsgalat=="e") & (kor>"10"):
        print ("A kalkulált effektív dózis", kor, "éves páciens mellkasi angio (embolia) vizsgálata esetében:", eff_dose_emb_adult ,"mSv")
   
print ("A kalkulátor által számolt értékek megközelítőlegesek. A számításhoz szükséges k (mSvmGy-1cm-1) konverziós faktor a The Measurement, Reporting, and Management of Radiation Dose in CT- Report of AAPM Task Group 23: CT Dosimetry-Diagnostic Imaging Council CT Committee alapján lett beállítva")    
    
input("A befejezéshez és kilépéshez nyomja meg az ENTER-t")