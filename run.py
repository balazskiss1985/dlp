# Application Settings

## Application Output
greetings = f"Üdvözlöm! Kérem, adja meg a vizsgálat típusát: \n"

examination_type_description = {
    "k": "koponya",
    "km": "koponya-mellkas",
    "kmhk": "koponya-mellkas-has-kismedence",
    "m": "mellkas",
    "e": "embolia",
    "mh": "mellkas-felhas",
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


def get_examination_type_name(etype):
    return examination_type_description[etype]

def get_dlp_type_name(etype):
    return dlp_type_description[etype]

for e in examination_type_description:
    greetings = greetings + f' - {str(get_examination_type_name(e))}: {str(e)}\n'

def get_dlp_input(examination_type, dlp_type):
 print(f'Kérem, adja meg a {get_examination_type_name(examination_type)} {get_dlp_type_name(dlp_type)} DLP értékét, majd nyomjon Enter-t')


print(greetings)
examination_type_input = input()
print(f"You have selected: {examination_type_input}")

request_for_age = "Kérem, adja meg a beteg életkorát"
print(request_for_age)
age_input = int(input())
print(f"You have selected: {age_input}")


# Topogram Input
get_dlp_input(examination_type_input, 0)
topogram_dlp_value = input()

# Nativ Input
get_dlp_input(examination_type_input, 1)
nativ_dlp_value = input()

# Kontraszt Input
get_dlp_input(examination_type_input, 2)
kontraszt_dlp_value = input()

