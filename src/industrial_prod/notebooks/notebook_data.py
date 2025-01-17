# %%
import pandas as pd 
from dbnomics import fetch_series
import plotly.express as px

# %%
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
# %% 
data_indu = data_indu[["original_period", "value", "Geopolitical entity (reporting)"]].rename(
columns=({"original_period":"Years - Quarters","Geopolitical entity (reporting)":"Countries","value" : "Industrial Production"})
)
#%%
data_indu["Years - Quarters"] = pd.PeriodIndex(data_indu["Years - Quarters"], freq='Q').to_timestamp()
# %%
fig = px.line(
  data_indu, x="Years - Quarters", y="Industrial Production", color="Countries"
)
fig
# %%
#Data for 2024
data_2024 = data_indu[data_indu["Years - Quarters"] == "2024-01-01 00:00:00"]
# %%
total_row = pd.DataFrame([{
    "Years - Quarters": "Total",
    "Countries": "Total",
    "Industrial Production": data_2024["Industrial Production"].sum()
}])

#%%
data_2024 = pd.concat([data_2024, total_row])

# %%
fig = px.pie(data_2024, values= "Industrial Production", names="Countries", title = "Industrial Production of European Continent for 2024")
fig.show()

# %%
path = r"/home/juliette/projets/industrial_prod/src/industrial_prod"
path
