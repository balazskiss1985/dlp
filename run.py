import tkinter as tk

# DESKTOP APP
window = tk.Tk()
window.title("Effektív dózis kalkulátor ver. 1.0")  # Elnevezzük
window.geometry("1000x550")  # Megadjuk a méretét
window.configure(bg="#f5edec")

# Application Settings

## Application Output
greetings = f"Üdvözlöm! Kérem, adja meg a vizsgálat típusát: \n"

examination_type_description = {
    "k": "koponya",
    "km": "koponya-mellkas",
    "kmh": "koponya-mellkas-has",
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
    2: "toddler",
    # Age equal to 10 year or less
    3: "child",
    # Age equal to 11 year or less
    4: "adult",
}
koponya_constant_by_age = {
    0: 0.011,
    1: 0.0067,
    2: 0.004,
    3: 0.0032,
    4: 0.0021,
}
mellkas_constant_by_age = {
    0: 0.039,
    1: 0.026,
    2: 0.018,
    3: 0.013,
    4: 0.014,
}
mellkas_has_by_age = {
    0: 0.044,
    1: 0.028,
    2: 0.019,
    3: 0.014,
    4: 0.015,
}
has_kismedence_by_age = {
    0: 0.049,
    1: 0.03,
    2: 0.02,
    3: 0.015,
    4: 0.015,
}

dlp_value = 0.0
topogram_dlp_value = 0.0
nativ_dlp_value = 0.0
kontraszt_dlp_value = 0.0


def get_type_description(etype):
    return examination_type_description[etype]


def get_dlp_type_name(etype):
    return dlp_type_description[etype]


def get_examination_type_name(etype):
    return examination_type_description[etype]


def dlp_input_message(examination_type, dlp_type):
    print(
        f"Kérem, adja meg a {get_examination_type_name(examination_type)} {get_dlp_type_name(dlp_type)} DLP értékét, majd nyomjon Enter-t"
    )


def get_examination_type():
    print(greetings)
    return str(input())


def get_age_value():
    print("Kérem, adja meg a beteg életkorát")
    return int(input())


def get_dlp_value():
    print("Kérem, adja meg a DLP-t, majd nyomjon Enter-t")
    return float(input())


def get_dlp_type_value(examination_type_value, dlp_type_value):
    print(
        f"Kérem, adja meg a {get_examination_type_name(examination_type_value)} {get_dlp_type_name(dlp_type_value)} DLP értékét, majd nyomjon Enter-t"
    )
    return float(input())


def add_values(*args):
    return sum(args)


def add_constant_value_by_age_and_dlp_type(age, dlp_type):
    if age == 0:
        if dlp_type == "k":
            return koponya_constant_by_age[0]
        if dlp_type == "m":
            return mellkas_constant_by_age[0]
        if dlp_type == "mh":
            return mellkas_has_by_age[0]
        if dlp_type == "hkm":
            return has_kismedence_by_age[0]
    if age <= 1:
        if dlp_type == "k":
            return koponya_constant_by_age[1]
        if dlp_type == "m":
            return mellkas_constant_by_age[1]
        if dlp_type == "mh":
            return mellkas_has_by_age[1]
        if dlp_type == "hkm":
            return has_kismedence_by_age[1]
    if age <= 5:
        if dlp_type == "k":
            return koponya_constant_by_age[2]
        if dlp_type == "m":
            return mellkas_constant_by_age[2]
        if dlp_type == "mh":
            return mellkas_has_by_age[2]
        if dlp_type == "hkm":
            return has_kismedence_by_age[2]
    if age <= 10:
        if dlp_type == "k":
            return koponya_constant_by_age[3]
        if dlp_type == "m":
            return mellkas_constant_by_age[3]
        if dlp_type == "mh":
            return mellkas_has_by_age[3]
        if dlp_type == "hkm":
            return has_kismedence_by_age[3]
    if age > 10:
        if dlp_type == "k":
            return koponya_constant_by_age[4]
        if dlp_type == "m":
            return mellkas_constant_by_age[4]
        if dlp_type == "mh":
            return mellkas_has_by_age[4]
        if dlp_type == "hkm":
            return has_kismedence_by_age[4]


for e in examination_type_description:
    greetings = greetings + f" - {str(get_examination_type_name(e))}: {str(e)}\n"

examination_type_value = get_examination_type()
age_value = get_age_value()

value = 0
add_value = 0

if examination_type_value in ["km", "kmh", "kmhk"]:
    koponya_value = get_dlp_type_value("k", 0)
    koponya_nativ_value = get_dlp_type_value("k", 1)
    koponya_kontraszt_value = get_dlp_type_value("k", 2)
    koponya = add_values(
        koponya_value,
        koponya_nativ_value,
        koponya_kontraszt_value,
    ) * add_constant_value_by_age_and_dlp_type(age_value, "k")
    if examination_type_value == "km":
        mell_topogram_value = get_dlp_type_value("m", 0)
        mell_nativ_value = get_dlp_type_value("m", 1)
        mell_kontraszt_value = get_dlp_type_value("m", 2)
        mell = add_values(
            mell_topogram_value,
            mell_nativ_value,
            mell_kontraszt_value,
        ) * add_constant_value_by_age_and_dlp_type(age_value, "m")
        add_value = mell
    else:
        mellkas_has_topogram_value = get_dlp_type_value("mh", 0)
        mellkas_has_nativ_value = get_dlp_type_value("mh", 1)
        mellkas_has_kontraszt_value = get_dlp_type_value("mh", 2)
        mellkas_has = add_values(
            mellkas_has_topogram_value,
            mellkas_has_nativ_value,
            mellkas_has_kontraszt_value,
        ) * add_constant_value_by_age_and_dlp_type(age_value, "mh")
        add_value = mellkas_has
    value = koponya + add_value
elif examination_type_value in ["k", "m", "mhk", "hkm", "e"]:
    glp_value = get_dlp_value()
    if examination_type_value == "k":
        value = glp_value * add_constant_value_by_age_and_dlp_type(age_value, "k")
    if examination_type_value == "m":
        value = glp_value * add_constant_value_by_age_and_dlp_type(age_value, "m")
    if examination_type_value == "hkm":
        value = glp_value * add_constant_value_by_age_and_dlp_type(age_value, "hkm")
    if examination_type_value == "mhk":
        value = glp_value * add_constant_value_by_age_and_dlp_type(age_value, "mhk")
    if examination_type_value == "e":
        value = glp_value * add_constant_value_by_age_and_dlp_type(age_value, "m")
else:
    print("Incorrect Value, try again.")

print(
    "A kalkulált effektív dózis",
    age_value,
    "éves páciens koponya-mellkas vizsgálata esetében:",
    value,
    "mSv.",
)

print(
    "A kalkulátor által számolt értékek megközelítőlegesek. \n \
A számításhoz szükséges k (mSvmGy-1cm-1) konverziós faktor a \n \
The Measurement, Reporting, and Management of Radiation Dose in \n \
CT- Report of AAPM Task Group 23: CT Dosimetry-Diagnostic \n \
Imaging Council CT Committee alapján lett beállítva."
)
