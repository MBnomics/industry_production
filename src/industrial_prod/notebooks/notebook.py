# %%
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dbnomics import fetch_series
import pandas as pd 
#%%
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
# %%
countries = np.unique(df_indu["Countries"])
dfs = {}
# %%
for country in countries:
    dfs[f"df_indu_{country}"] = df_indu[df_indu["Countries"] == country]
    fig = go.Figure()
    fig = px.line(
        dfs[f"df_indu_{country}"],
        x="Years - Quarters",
        y="Industrial Production",
        color= "Countries",
        title="Industrial Production",
    )
    fig.show()

# %%
