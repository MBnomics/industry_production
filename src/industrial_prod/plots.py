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
        title="Industrial Production of European Continent for 2024",
    )
    return fig
