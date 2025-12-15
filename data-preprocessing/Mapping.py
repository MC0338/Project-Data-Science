import pandas as pd
pd.set_option('future.no_silent_downcasting', True)
from Normalisering import normaliseer_kolommen
from Kolommen import behoud_kolommen

import sys
from pathlib import Path

ROOT = Path.cwd().parent
sys.path.append(str(ROOT))
from paths import RAW_DATA, OUTPUT_DIR

#input en ouput mogen niet hetzelfde zijn
input_csv = RAW_DATA/"Welzijnsmonitor2025_test.csv"
output_csv = OUTPUT_DIR/"test_swm.csv"

mapping = {
    "Soms": 3,
    "Nee, maar ik verwacht wel vertraging op te gaan lopen": 1,
    "Ja": 5,
    "Nooit": 1,
    "Helemaal geen stress": 1,
    "Nooit of bijna nooit": 1,
    "Geen (extra) hulp / ondersteuning nodig": 1,
    "Geen (extra) hulp/ondersteuning nodig" : 1,
    "Niet bekend mee": 1,
    "Zeer weinig": 1,
    "Zeer oneens": 1,
    "Helemaal niet": 1,
    "Zeer ongezond": 1,
    "1-10 ECTs": 2,
    "Zelden": 2,
    "Weinig stress": 2,
    "Behoefte aan (extra) hulp / ondersteuning en ontvang dit ook": 2,
    "Behoefte aan (extra) hulp/ondersteuning en ontvang dit ook": 2,
    "Bekend mee, maar geen gebruik van gemaakt": 2,
    "Weinig": 2,
    "Oneens": 2,
    "Ongezond": 2,
    "11-20 ECTs": 3,
    "Matige stress": 3,
    "Meestal": 3,
    "Behoefte aan (extra) hulp / ondersteuning en ontvang dit (nog) niet": 3,
    "Behoefte aan (extra) hulp/ondersteuning en ontvang dit (nog) niet" : 3,
    "Bekend mee en gebruik van gemaakt": 3,
    "Neutraal": 3,
    "Niet ongezond / niet gezond": 3,
    "21-30 ECTs": 4,
    "Vaak": 4,
    "Veel stress": 4,
    "De hele tijd of bijna altijd": 4,
    "Eens": 4,
    "Veel": 4,
    "Gezond": 4,
    "Meer dan 30 ECTs": 5,
    "Altijd": 5,
    "(Bijna) altijd": 5,
    "Heel veel stress": 5,
    "Zeer veel": 5,
    "Zeer eens": 5,
    "Zeer gezond": 5,
    "Niet van toepassing": None,
    "Ik weet het nog niet": 3,
    "Nee": 1,
}

# Lees CSV bestand
df = pd.read_csv(input_csv, sep=';', encoding='utf-8-sig',
                 quotechar='"', on_bad_lines='skip')

# Strip whitespace
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

#Verwijder kolommen die niet gebruikt worden
df = behoud_kolommen(df)


#Eerst de depressie kolommen transformeren die het woord soms bevat
depr_cols = [col for col in df.columns if col.startswith("Depr")]

df[depr_cols] = df[depr_cols].replace({"Soms": 2})

# Mapping toepassen
df = df.replace(mapping)

#Ompolen van depr_4 en depr_6 -> negatieve vraag
reverse_mapping = {
    1: 4,
    2: 3,
    3: 2,
    4: 1,
}
for col in ["Depr_4", "Depr_6"]:
    if col in df.columns:
        df[col] = df[col].map(reverse_mapping)

# Normalisatie uitvoeren in het tweede script
df = normaliseer_kolommen(df)

df.to_csv(
    output_csv,
    sep=';',
    decimal=',',
    encoding='utf-8-sig',
    index=False,
    quoting=1 
)

print(f"Bestand is getransformeerd naar CSV! {output_csv}")
