import pandas as pd
from dbnomics import fetch_series


def download_gdp_data():
    data_gdp = fetch_series(
        "Eurostat",
        "nama_10_gdp",
        dimensions={
            "freq": ["A"],
            "unit": ["CLV20_MEUR"],
            "na_item": ["B1GQ"],
            "geo": [
                "AT",  # Austria
                "BE",  # Belgium
                "BG",  # Bulgaria
                "HR",  # Croatia
                "CY",  # Cyprus
                "CZ",  # Czech Republic
                "DK",  # Denmark
                "EE",  # Estonia
                "FI",  # Finland
                "FR",  # France
                "DE",  # Germany
                "GR",  # Greece
                "HU",  # Hungary
                "IE",  # Ireland
                "IT",  # Italy
                "LV",  # Latvia
                "LT",  # Lithuania
                "LU",  # Luxembourg
                "MT",  # Malta
                "NL",  # Netherlands
                "PL",  # Poland
                "PT",  # Portugal
                "RO",  # Romania
                "SK",  # Slovakia
                "SI",  # Slovenia
                "ES",  # Spain
                "SE",  # Sweden
                "EU27_2020",
                "EA20",
            ],
        },
    )

    df_gdp = data_gdp[["original_period", "value", "Geopolitical entity (reporting)"]]
    return df_gdp


def download_indu_data():
    data_indu = fetch_series(
        "Eurostat",
        "namq_10_a10",
        dimensions={
            "freq": ["Q"],
            "unit": ["CLV20_MEUR"],
            "s_adj": ["SCA"],
            "nace_r2": ["B-E"],
            "na_item": ["B1G"],
            "geo": [
                "AT",  # Austria
                "BE",  # Belgium
                "BG",  # Bulgaria
                "HR",  # Croatia
                "CY",  # Cyprus
                "CZ",  # Czech Republic
                "DK",  # Denmark
                "EE",  # Estonia
                "FI",  # Finland
                "FR",  # France
                "DE",  # Germany
                "GR",  # Greece
                "HU",  # Hungary
                "IE",  # Ireland
                "IT",  # Italy
                "LV",  # Latvia
                "LT",  # Lithuania
                "LU",  # Luxembourg
                "MT",  # Malta
                "NL",  # Netherlands
                "PL",  # Poland
                "PT",  # Portugal
                "RO",  # Romania
                "SK",  # Slovakia
                "SI",  # Slovenia
                "ES",  # Spain
                "SE",  # Sweden
            ],
        },
    )

    df_indu = data_indu[
        ["original_period", "value", "Geopolitical entity (reporting)"]
    ].rename(
        columns=(
            {
                "original_period": "Years - Quarters",
                "Geopolitical entity (reporting)": "Countries",
                "value": "Industrial Production",
            }
        )
    )
    df_indu["Years - Quarters"] = pd.PeriodIndex(
        df_indu["Years - Quarters"], freq="Q"
    ).to_timestamp()
    return df_indu


def indu_data_for_2024(df_indu):
    data_2024 = df_indu[df_indu["Years - Quarters"] == "2024-Q2"]

    return data_2024


def indu_data_total_2024(data_2024):
    total_row = pd.DataFrame(
        [
            {
                "Years - Quarters": "Total",
                "Countries": "Total",
                "Industrial Production": data_2024["Industrial Production"].sum(),
            }
        ]
    )

    data_tot = pd.concat([data_2024, total_row])

    return data_tot


def indu_data_for_2000(df_indu):
    data_2000 = df_indu[df_indu["Years - Quarters"] == "2000-Q2"]

    return data_2000
