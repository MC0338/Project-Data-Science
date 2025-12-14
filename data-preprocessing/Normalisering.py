import pandas as pd

def _to_float(x):
    if pd.isna(x):
        return None
    x = str(x).strip().replace(",", ".")
    try:
        return float(x)
    except ValueError:
        return None

def norm_0_50(value):
    v = _to_float(value)
    if v is None:
        return None
    return 1 + ((v * 4.0) / 50.0)

def norm_1_3(value):
    v = _to_float(value)
    if v is None:
        return None
    return 1 + ((v - 1) * 4.0 / 2.0)

def norm_1_4(value):
    v = _to_float(value)
    if v is None:
        return None
    return 1 + ((v - 1) * 4.0 / 3.0)

def norm_0_5(value):
    v = _to_float(value)
    if v is None:
        return None
    return 1 + ((v * 4.0) / 5.0)

def norm_0_10(value):
    v = _to_float(value)
    if v is None:
        return None
    return 1 + ((v * 4.0) / 10.0)




kolom_formules = {

   # Kolommen die de reeks 1-4 gebruiken
    "Depr_1": norm_1_4,
    "Depr_2": norm_1_4,
    "Depr_3": norm_1_4,
    "Depr_4": norm_1_4,
    "Depr_5": norm_1_4,
    "Depr_6": norm_1_4,
    "Depr_7": norm_1_4,
    "Depr_8": norm_1_4,
    # Kolommen die de reeks 0-10 gebruiken
    "Mot_Stress_1": norm_0_10,
    "Mot_Stress_2": norm_0_10,
    "Mot_Stress_4": norm_0_10,
    "Cantrill_1": norm_0_10,
    "Cantrill": norm_0_10,
    "Q297_1": norm_0_10,
    "Cijfer_huidig_1" : norm_0_10,
    # Kolommen die de reeks 0-50 gebruiken
    "Werk_1": norm_0_50,
    # Kolommen die de reeks 1-3 gebruiken
    "Hulp_1" : norm_1_3,
    "Hulp_2" : norm_1_3,
    "Hulp_3": norm_1_3,
    "Bekendgebruik_1" : norm_1_3,
    "Bekendgebruik_2": norm_1_3,
    "Bekendgebruik_3": norm_1_3,
    "Bekendgebruik_4": norm_1_3,
    "Bekendgebruik_5": norm_1_3,
    "Bekendgebruik_6": norm_1_3,
    "Bekendgebruik_7": norm_1_3,
    # Kolommen die de reeks 0-5 gebruiken
    "Vertr" : norm_0_5,
    "Soc_1" : norm_0_5,
    "Soc_2": norm_0_5,
    "Soc_3": norm_0_5,
    "Soc_4": norm_0_5,
    "Soc_5": norm_0_5,
    "Soc_6": norm_0_5,
    "Soc_7": norm_0_5,
    "Soc_8": norm_0_5,
    "Soc_9": norm_0_5,

}

def normaliseer_kolommen(df):

    for kolom, functie in kolom_formules.items():
        if kolom in df.columns:
            df[kolom] = df[kolom].apply(functie)

    return df