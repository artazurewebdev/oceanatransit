import streamlit as st

st.title("HyperloopOne Portal")


with st.expander("Credits"):
    st.write("This website was made by Max Shuang using Streamlit on Python Code")
    st.write("This website is purely hypothetical, and is not affiliated with Virgin Group")
    st.write("Do not make any purchases, or share sensitive information here.")
    st.write("The redirection to HyperloopOne's transit map was made using Tennessine.uk's Metro Building by the same maker of this website")
    st.write("This is an official website of Team Oceana for the Future City Project of 2025")

link = "https://tennessine.co.uk/metro/70f7f437184cfe3"

st.markdown(f"""
    <a href="{link}" target="_blank" style="text-decoration: none;">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px;">
            HyperloopOne Transit System Map
        </button>
    </a>
""", unsafe_allow_html=True)