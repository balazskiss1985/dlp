# Application Settings

## Application Output
greetings = f"Üdvözlöm! Kérem, adja meg a vizsgálat típusát: \n"

examination_type_description = {
    "k": "koponya",
    "km": "koponya-mellkas",
    "kmhk": "koponya-mellkas-has-kismedence",
    "m": "mellkas",
    "e": "embolia",
    "mh": "mellkas-has",
    "mhk": "mellkas-has-kismedence",
    "hkm": "has-kismedence",
}
dlp_type_description = {
        0: "topogram",
        1: "nativ",
        2: "kontraszt",
}

patient_by_age = {
        # Age equal to 0 years
        0: "newborn",
        # Age equal to 1 year or less
        1: "baby",
        # Age equal to 5 year or less
        5: "toddler",
        # Age equal to 10 year or less
        10: "child",
        # Age equal to 11 year or less
        11: "adult",
}


def get_type_description(etype):
    return examination_type_description[etype]

def get_dlp_type_name(etype):
    return dlp_type_description[etype]

for e in examination_type_description:
    greetings = greetings + f' - {str(e)}: {str(e)}\n'

def dlp_input_message(examination_type, dlp_type):
    print(f'Kérem, adja meg a {get_examination_type_name(examination_type)} {get_dlp_type_name(dlp_type)} DLP értékét, majd nyomjon Enter-t')

def get_examination_type():
    print(greetings)
    return str(input())

dlp_value = 0.0
topogram_dlp_value = 0.0
nativ_dlp_value = 0.0
kontraszt_dlp_value = 0.0

def get_age_value():
    print ("Kérem, adja meg a beteg életkorát")                                                                                #BEKÉREM AZ ÉLETKORT
    return int(input())

def get_dlp_value():
    print("Kérem, adja meg a DLP-t, majd nyomjon Enter-t")
    return float(input())

def get_dlp_type_value(examination_type_value, dlp_type_value):
    print(f'Kérem, adja meg a {get_examination_type_name(examination_type_value)} {get_dlp_type_name(dlp_type_value)} DLP értékét, majd nyomjon Enter-t')
    return float(input())

examination_type_value = get_examination_type()
age_input = get_age_value()

if examination_type_value in ["k", "m", "mhk", "hkm", "e" ]:
    dlp_value = get_dlp_value()
elif examination_type_value in ["km","kmh", "kmhk" ]:
    if examination_type_value == "km":
        koponya_topogram_dlp_value = get_dlp_type_value("k", 0)
        koponya_nativ_dlp_value = get_dlp_type_value("k", 1)
        koponya_kontraszt_dlp_value = get_dlp_type_value("k", 2)
        mell_topogram_dlp_value = get_dlp_type_value("m", 0)
        mell_nativ_dlp_value = get_dlp_type_value("m", 1)
        mell_kontraszt_dlp_value = get_dlp_type_value("m", 2)
    elif examination_type_value == "kmh":
        koponya_topogram_dlp_value = get_dlp_type_value("k", 0)
        koponya_nativ_dlp_value = get_dlp_type_value("k", 1)
        koponya_kontraszt_dlp_value = get_dlp_type_value("k", 2)
        mellkas_has_topogram_dlp_value = get_dlp_type_value("mh", 0)
        mellkas_has_nativ_dlp_value = get_dlp_type_value("mh", 1)
        mellkas_has_kontraszt_dlp_value = get_dlp_type_value("mh", 2)
        pass
    elif examination_type_value == "kmhk":
        pass
else:
    print("Incorrect Value, try again.")


print(f"DLP value: {dlp_value}")
print(f"Topogram value: {topogram_dlp_value}")
print(f"Nativ value: {nativ_dlp_value}")
print(f"Kontraszt value: {kontraszt_dlp_value}")
print(f"Age value: {age_input}")
