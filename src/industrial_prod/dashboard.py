import importlib.resources
import os
import sys

import numpy as np
import streamlit as st
from download import download_indu_data, indu_data_for_2000, indu_data_for_2024
from plots import (
    plot_indu_prod,
    plot_indu_prod_2000,
    plot_indu_prod_2024,
    plot_indu_prod_per_country,
)
from streamlit_option_menu import option_menu


def main() -> None:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    package_dir = importlib.resources.files("industrial_prod")

    st.set_page_config(
        page_title="Industrial Production",
        page_icon=str(package_dir / "images /favicon.png"),
    )
    st.image(str(package_dir / "images /dbnomics.svg"), width=300)
    st.title(":blue[Industrial Production]")

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
            background-color: #0e1117;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    data_indu = download_indu_data()
    data_indu_2024 = indu_data_for_2024(data_indu)
    data_indu_2000 = indu_data_for_2000(data_indu)

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Explanations", "Industrial Production", "Sources"],
            icons=["book", "bar-chart", "bar-chart", "search"],
            menu_icon=":",
            default_index=0,
        )
    if selected == "Explanations":
        st.write(
            "This dashboard presents the evolution of industrial production in Europe between 2000 and 2024. This geographic focus highlights the contrasting dynamics between major industrial economies, such as Germany and Italy, and emerging countries in Eastern Europe.")
        st.write(
            "The analyzed period is marked by significant economic events: the technological boom of the 2000s, the 2008 financial crisis, and the disruptions caused by the COVID-19 pandemic in 2020." 
            "The presented charts illustrate both absolute production variations and the shifts in the respective shares of European countries, thereby revealing the structural transformations in Europe's industrial landscape."
        )
        st.write(
            "The evolution of industrial production in Europe between 2000 and 2024 is not only a reflection of the continent's economic development but also evidence of how it has responded and recovered from major disruptions." 
            "By examining the policies and strategies implemented during this period, we can better understand the role of industrial production as both a driver of economic stability and an indicator of resilience in the face of global challenges."
            "The early 2000s saw stable growth driven by globalization and the 2004 EU enlargement, supported by *cohesion funds* that helped modernize infrastructure and boost industrial capacities in new member states like Hungary."
            "However, the 2008 financial crisis disrupted this momentum, leading to a severe contraction in industrial output across Europe. In response, the *European Economic Recovery Plan* (2008) injected €200 billion to stabilize economies, though recovery remained uneven."
        )
        st.write(
            "The 2010s brought further challenges, such as the sovereign debt crisis, which imposed austerity measures in many countries, slowing recovery for nations like Italy." 
            "Nonetheless, the adoption of the *Europe 2020 Strategy* fostered investment in research, innovation, and sustainable industrial practices, enabling resilient economies like Germany to strengthen their industrial bases." 
            "By the latter half of the decade, the focus shifted to digitalization and green transitions, with initiatives like the *Digital Single Market Strategy* (2015) and the *Green Deal* (2019), which positioned Europe as a global leader in sustainable industrial practices." 
            "Countries like Denmark capitalized on these policies, showcasing remarkable growth through renewable energy and innovative technologies."
        )
        st.write(
            "The COVID-19 pandemic in 2020 caused a decline in industrial production, exposing vulnerabilities in global supply chains." 
            "However, the EU's *Recovery and Resilience Facility (RRF)* provided €750 billion to aid recovery, focusing on green and digital transformations."
            "This led to a rapid rebound in key economies like France and Germany. Most recently, the *REPowerEU Plan* (2022) responded to the energy crisis triggered by the Ukraine war, accelerating Europe's transition to renewable energy and reinforcing industrial resilience, particularly in nations like Denmark."
        )
        st.write(
            "Looking ahead, European industrial production must contend with emerging global competition, particularly from Asia, and the potential impact of trade barriers like U.S. tariffs." 
            "Additionally, the transition toward sustainability and decarbonization will challenge Europe to align environmental ambitions with industrial competitiveness." 
            "Addressing these issues will require continued innovation and strategic policies to ensure resilience and maintain a strong global presence."
        )
        st.write("*By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*")
    

    if selected == "Industrial Production":

        tab1, tab2, tab3 = st.tabs(
            ["Global Evolution", "Evolution for each Country", "Between 2000 & 2024"]
        )

        with tab1:
            fig = plot_indu_prod(data_indu)
            st.plotly_chart(fig)
        with tab2:
            country = np.unique(data_indu["Country"])

            selected_country = st.selectbox(
                "Select a country :",
                country,
                index=0,
            )

            fig_country = plot_indu_prod_per_country(data_indu, selected_country)
            st.plotly_chart(fig_country)
        with tab3:
            st.header("Share (%) per Country")
            col1, col2 = st.columns(2)
            with col2:
                fig_2024 = plot_indu_prod_2024(data_indu_2024)
                st.plotly_chart(fig_2024)

            with col1:
                fig_2000 = plot_indu_prod_2000(data_indu_2000)
                st.plotly_chart(fig_2000)
        st.write("*By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*")
    
    if selected == "Sources":
        st.header("[**DBnomics**](https://db.nomics.world)") 
        st.subheader("[Code source](https://github.com/MBnomics/industry_production)")
        st.write(
            "\n"
            "[GDP Data](https://db.nomics.world/Eurostat/nama_10_gdp?tab=list)\n"
            "\n"
            "[Gross value added and income](https://db.nomics.world/Eurostat/namq_10_a10?tab=list)\n"
        )
        st.write("*By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*")
    
if __name__ == "__main__":
    main()
