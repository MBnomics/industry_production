import plotly.express as px
import plotly.graph_objects as go


def plot_indu_prod(df_indu):
    fig = go.Figure()
    fig = px.line(
        df_indu[df_indu["Years - Quarters"] >= "2000-Q1"],
        x="Years - Quarters",
        y="Industrial Production",
        color="Countries",
        title="Industrial Production",
    )

    return fig


def plot_indu_prod_2024(data_2024):
    fig = px.pie(
        data_2024,
        values="Industrial Production",
        names= "Countries",
        title="2024 - Industrial Production of European Continent",
    )
    return fig

def plot_indu_prod_2000(data_2000):
    fig = px.pie(
        data_2000,
        values="Industrial Production",
        names= "Countries",
        title="2000 - Industrial Production of European Continent",
    )
    return fig
