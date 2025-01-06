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
            🔒 HyperloopOne Transit System Map
        </button>
    </a>
""", unsafe_allow_html=True)

st.header("Our Trains")

st.subheader("Loop 1")

st.write("Local Supersonic Hyperloop")
st.write(" - 718kts")
st.write(" - Triple-section Seating (Economy, Business, First)")
st.write(" - Maglev Train")
st.write(" - Tubed Vacuum Train")
st.write(" - Seats 140 (3-section seating)")

st.subheader("Loop 2")

st.write("Regional Supersonic Hyperloop")
st.write(" - 1200kts")
st.write(" - Four-section Seating (Economy, Business, First, Suite)")
st.write(" - Maglev Train")
st.write(" - Tubed Vacuum Train")
st.write(" - Seats 280 (4-section seating)")

st.subheader("Loop 2-M2124")

st.write("Cross-country Supersonic Hyperloop")
st.write(" - 1450kts")
st.write(" - Five-section Seating (Economy, Business, First, Suite, Cabin Crew Quarters on FL2)")
st.write(" - Maglev Train")
st.write(" - Tubed Vacuum Train")
st.write(" - Seats 300 (5-section seating)")

st.subheader("SecureTransit - SubLoop A")

st.write("Local Subsonic Metrolink")
st.write(" - 350kts")
st.write(" - Single-section Seating (Coach)")
st.write(" - Maglev Train")
st.write(" - Underground Transit Train")
st.write(" - Seats 65")

st.subheader("Loop 3 | Overture")

st.write("Overseas Supersonic Hyperloop")
st.write(" - 1600kts")
st.write(" - Five-section Seating (Economy, Business, First, Suite, Cabin Crew Quarters on FL2)")
st.write(" - Maglev Train")
st.write(" - Tubed Vacuum Train")
st.write(" - Seats 345 (3-section seating)")
st.write(" - Seats 300 (5-section seating)")