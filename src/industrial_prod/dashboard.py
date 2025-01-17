import importlib.resources
import sys
import os 
import streamlit as st
from download import download_indu_data, indu_data_for_2024, indu_data_for_2000
from plots import plot_indu_prod, plot_indu_prod_2024, plot_indu_prod_2000
from streamlit_option_menu import option_menu


def main() -> None:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    package_dir = importlib.resources.files("industrial_prod")

    st.set_page_config(
        page_title="Industrial Production",
        page_icon=str(package_dir / "images /favicon.png"),
    )
    st.image(str(package_dir / "images /dbnomics.svg"), width=300)
    st.title(":blue[Industrial Production for European Countries]")

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(str(package_dir / "assets/styles.css"))
    st.markdown(
        """
        <style>
        hr {
            height: 1px;
            border: none;
            color: #333;
            background-color: #333;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Explanations", "Industrial Production", "Sources"],
            icons=["book", "bar-chart", "bar-chart", "search"],
            menu_icon=":",
            default_index=0,
        )
    if selected == "Industrial Production":

        data_indu = download_indu_data()
        data_indu_2024 = indu_data_for_2024(data_indu)
        data_indu_2000 = indu_data_for_2000(data_indu)


        fig = plot_indu_prod(data_indu)
        st.plotly_chart(fig)

        col1, col2 = st.columns(2)
        with col1:
            
            fig_2024 = plot_indu_prod_2024(data_indu_2024)
            st.plotly_chart(fig_2024)

        with col2:
            fig_2000 = plot_indu_prod_2000(data_indu_2000)
            st.plotly_chart(fig_2000)


if __name__ == "__main__":
    main()
