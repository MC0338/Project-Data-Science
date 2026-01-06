import pandas as pd
pd.set_option('future.no_silent_downcasting', True)
from Normalisering import normaliseer_kolommen
from Kolommen import behoud_kolommen

import sys
from pathlib import Path

"""
Resolve project root and ensure local package imports work.
•⁠  ⁠⁠ ROOT ⁠ points two levels up from this script file.
•⁠  ⁠The resolved root is inserted into ⁠ sys.path ⁠ so that modules like ⁠ paths ⁠
  can be imported without relative import issues.
"""
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from paths import RAW_DATA, PROCESSED_DATA

#input en ouput mogen niet hetzelfde zijn
"""
Define input and output locations (must be different).
•⁠  ⁠⁠ input_excel ⁠: the prepared Excel source in RAW_DATA.
•⁠  ⁠⁠ output_csv ⁠: the processed CSV destination in PROCESSED_DATA.
"""
input_excel = RAW_DATA/"Welzijnsmonitor2025_prep.xlsx"
output_csv = PROCESSED_DATA/"Welzijnsmonitor2025_processed.csv"

"""
Categorical-to-ordinal mapping for Dutch survey responses.
This dictionary converts textual labels (frequencies, stress levels, agreement,
ECT ranges, health assessments, support needs) into integer scores. 
It also handles non-applicable or unknown responses (mapped to None) and a binary 'Nee' (0).
Note:
•⁠  ⁠'Soms' appears here as 3, while depression columns are pre-handled separately
•⁠  ⁠to set 'Soms' to 2 before global mapping (see the 'Depr' section below).
"""
mapping = {
    "Soms": 3,
    "Nee, maar ik verwacht wel vertraging op te gaan lopen": 1,
    "Ja": 1,
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
    "Ik weet het nog niet": None,
    "Nee": 0,
}

# Lees CSV bestand
"""
Load the prepared Excel file into a DataFrame.
Uses the openpyxl engine to ensure compatibility with .xlsx files.
"""
df = pd.read_excel(input_excel, engine="openpyxl")

# Strip whitespace
"""
Strip leading/trailing whitespace from all string cells.
This helps prevent mismatches during mapping due to stray spaces.
Non-string cells are left unchanged.
"""
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

#Verwijder kolommen die niet gebruikt worden
"""
Retain only relevant columns for analysis.
Uses Kolommen.behoud_kolommen to keep only the necessary columns, based on predefined rules for removing irrelevant ones.
"""
df = behoud_kolommen(df)


#Eerst de depressie kolommen transformeren die het woord soms bevat
"""
Pre-transform depression-related columns ('Depr*') for the label 'Soms'.
To align scale interpretation, 'Soms' in these columns is first mapped to 2 before applying the global mapping. 
This ensures consistent scoring for
depression items.
"""
depr_cols = [col for col in df.columns if col.startswith("Depr")]

df[depr_cols] = df[depr_cols].replace({"Soms": 2})

# Mapping toepassen
"""
Apply the global categorical-to-ordinal mapping.
Replaces textual responses across the dataset with the numeric values defined in ⁠ mapping ⁠. 
Special cases include None for 'Niet van toepassing' and 'Ik weet het nog niet', and 0 for 'Nee'.
"""
df = df.replace(mapping)

#Ompolen van depr_4 en depr_6 -> negatieve vraag
"""
Reverse-score negatively phrased depression items.
For 'Depr_4' and 'Depr_6', apply the 1↔️4 and 2↔️3 mapping:
    1 -> 4
    2 -> 3
    3 -> 2
    4 -> 1
Only applied if the columns exist in the DataFrame.
"""
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
"""
(Optional) Normalize columns.

If enabled, ⁠ Normalisering.normaliseer_kolommen(df) ⁠ performs additional
normalization suitable for downstream analysis. Disabled here by default.
"""
df = normaliseer_kolommen(df)

"""
Export the processed DataFrame to CSV with European formatting.
•⁠  ⁠Semicolon (';') as the field separator.
•⁠  ⁠Comma (',') as the decimal separator.
•⁠  ⁠UTF-8 with BOM for broad Excel compatibility.
•⁠  ⁠⁠ quoting=1 ⁠ (csv.QUOTE_ALL) to quote all fields.
"""
df.to_csv(
    output_csv,
    sep=';',
    decimal=',',
    encoding='utf-8-sig',
    index=False,
    quoting=1 
)

print(f"Bestand is getransformeerd naar CSV! {output_csv}")
