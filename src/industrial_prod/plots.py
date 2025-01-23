import plotly.express as px
import plotly.graph_objects as go
import numpy as np 


def plot_indu_prod(df_indu):
    fig = go.Figure()
    fig = px.line(
        df_indu[df_indu["Years - Quarters"] >= "2000-Q1"],
        x="Years - Quarters",
        y="Industrial Production",
        color="Country",
        title="Industrial Production",
    )
    fig.update_layout(
        title=dict(text="Industrial Production per Country",font=dict(size=20, color="white"),x=0.5,xanchor="center"),
        xaxis_title="Year",
        yaxis_title="Industrial Production"
        )

    return fig

def plot_indu_prod_per_country(df_indu, country): 

        df_indu_filtred = df_indu[df_indu["Country"] == country]
        fig = go.Figure()
        fig = px.line(
            df_indu_filtred,
            x="Years - Quarters",
            y="Industrial Production",
            color= "Country"
        )
        fig.update_layout(
        title=dict(text=f"Industrial Production for {country}",font=dict(size=20, color="white"),x=0.5,xanchor="center"),
        xaxis_title="Year",
        yaxis_title="Industrial Production"
        )
        return fig 

def plot_indu_prod_2024(data_2024):
    fig = px.pie(
        data_2024,
        values="Industrial Production",
        names= "Country",
        title="2024",
    )
    fig.update_layout(
        title=dict(text="2024",font=dict(size=20, color="white"),x=0.35,xanchor="center"),
        legend=dict(title ="Country"))
    return fig

def plot_indu_prod_2000(data_2000):
    fig = px.pie(
        data_2000,
        values="Industrial Production",
        names= "Country",
        title="2000",
    )
    fig.update_layout(
        title=dict(text="2020",font=dict(size=20, color="white"),x=0.35,xanchor="center"),
        legend=dict(title ="Country")
        )
    return fig
