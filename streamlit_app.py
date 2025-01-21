import streamlit as st

st.title("Welcome to A Geography Channel Games")
page = st.sidebar.selectbox("Page", ["Home", "Buy?", "Maps", "About"])
if page == "Maps":
    game = st.sidebar.selectbox("Select Game", ["Europe 2025", "The Americas 2025", "Africa 2025", "Asia 2025", "Southeast Asia + Oceania 2025"])
    if game == "Europe 2025":
        st.image("Main Maps/europe map.png")
    if game == "The Americas 2025":
        st.image("Main Maps/The Americas map.png")
    if game == "Africa 2025":
        st.image("Main Maps/Africa map.png")
    if game == "Asia 2025":
        st.image("Main Maps/Asia map.png")
    if game == "Southeast Asia + Oceania 2025":
        st.image("Main Maps/seao map.png")
#Homepage
if page == "Home":
    st.subheader("Home")
#Map 1
if page == "About":
    st.subheader("Map 1")
#Map 2
if page == "Map 2":
    st.subheader("Map 2")