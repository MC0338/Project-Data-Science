import pandas as pd

# ---------------------------------------------
# Kolommen die in de dataset moeten zitten
# Kolommen staan in het format gebaseerd op de dataset van 2025, dus niet alfabetisch
# Beschrijvende kolommen staan onderaan
# ---------------------------------------------
Kolommen_Blijven = [
    "StudentID",
    "Jaar",
    "Bevl_1",
    "Bevl_2",
    "Bevl_3",
    "Burn1_1",
    "Burn1_2",
    "Burn1_3",
    "Burn1_4",
    "Mot_Stress_1",
    "Mot_Stress_2",
    "Mot_Stress_4",
    "Onnodige_stress_1",
    "Onnodige_stress_2",
    "Onnodige_stress_3",
    "Onnodige_stress_4",
    "Onnodige_stress_5",
    "Onnodige_stress_6",
    "Onnodige_stress_7",
    "Onnodige_stress_8",
    "Onnodige_stress_9",
    "Onnodige_stress_10",
    "Leefst",
    "Cantrill_1",
    "Cantrill",
    "Q297_1",
    "Depr_1",
    "Depr_2",
    "Depr_3",
    "Depr_4",
    "Depr_5",
    "Depr_6",
    "Depr_7",
    "Depr_8",
    "Cijfer_huidig_1",
    "Vertr",
    "StopInt",
    "Hulp_1",
    "Hulp_2",
    "Hulp_3",
    "Bekendgebruik_1",
    "Bekendgebruik_2",
    "Bekendgebruik_3",
    "Bekendgebruik_4",
    "Bekendgebruik_5",
    "Bekendgebruik_6",
    "Bekendgebruik_7",
    "Cogn_Eng1_1",
    "Cogn_Eng1_2",
    "Cogn_Eng1_3",
    "Cogn_Eng1_4",
    "Cogn_Eng1_5",
    "Cogn_Eng1_6",
    "Cogn_Eng2_1",
    "Cogn_Eng2_2",
    "Cogn_Eng2_3",
    "Cogn_Eng2_4",
    "Cogn_Eng2_5",
    "Cogn_Eng2_6",
    "Cogn_Eng2_7",
    "Cogn_Eng2_8",
    "Partici1_1",
    "Partici1_2",
    "Partici1_3",
    "Partici1_4",
    "Stopint2",
    "Betrok_Ouders",
    "Werk_1",
    "Zorg_1",
    "Zorg_2",
    "Zorg_3",
    "Zorg_4",
    "Zorg_5",
    "Zorg_6",
    "Pres_1",
    "Pres_2",
    "Pres_12",
    "Pres_4",
    "Veer_1",
    "Veer_2",
    "Veer_3",
    "Veer_4",
    "Veer_5",
    "Veer_6",
    "Cogregiedocent_1",
    "Cogregiedocent_2",
    "Cogregiedocent_3",
    "Cogregiedocent_4",
    "Cogregiedocent_5",
    "Cogregiedocent_6",
    "Extr_eng2_1",
    "Extr_eng2_2",
    "Extr_eng2_3",
    "Cogregiedocent_7",
    "Cogregiedocent_8",
    "Cogregiedocent_9",
    "Cogregiedocent_10",
    "Soc_veilig",
    "Soc_veilig_stelling_1",
    "Soc_veilig_stelling_2",
    "Soc_veilig_stelling_3",
    "Soc_veilig_stelling_4",
    "Soc_veilig_stelling_5",
    "Soc_1",
    "Soc_2",
    "Soc_3",
    "Soc_4",
    "Soc_5",
    "Soc_6",
    "Soc_7",
    "Soc_8",
    "Soc_9",
    "Pres_3",
    "Burn1_5",
    "Burn1_6",
    "Burn1_7",
    "Burn1_8",
    "Burn2_1",
    "Burn2_2",
    "Burn2_3",
    "Burn2_4",
    "Burn2_5",
    "Burn2_6",
    "Partici1_5",
    "Bevl_ext_1",
    "Bevl_ext_2",
    "Bevl_ext_3",
    "Bevl_ext_4",
    "Bevl_ext_5",
    "Bevl_ext_6",
    "Bevl_ext_7",
    "Domein",
    "Geslacht",
    "Leeftijd",
    "Locatie",
    "Studiejaar",
    "Uitwissel",
    "Vooropleid",
    "Woonsit"

]



def behoud_kolommen(df: pd.DataFrame) -> pd.DataFrame:
    """
    Behoudt alleen de kolommen in Kolommen_Blijven.
    Alle andere kolommen worden verwijderd.
    """

    # Kolommen die ontbreken
    ontbrekend = [k for k in Kolommen_Blijven if k not in df.columns]
    if ontbrekend:
        print("De volgende kolommen bestaan niet in de dataset:")
        for kol in ontbrekend:
            print(f"   - {kol}")

    # Kolommen die wél aanwezig zijn
    bestaande_kolommen = [k for k in Kolommen_Blijven if k in df.columns]

    # Kolommen die verwijderd worden
    te_verwijderen = [k for k in df.columns if k not in bestaande_kolommen]
    if te_verwijderen:
        print("\n De volgende kolommen worden verwijderd:")
        for kol in te_verwijderen:
            print(f"   - {kol}")

    return df[bestaande_kolommen]
