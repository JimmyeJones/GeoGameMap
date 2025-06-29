import streamlit as st

st.title("Welcome to A Geography Channel Games")
page = st.sidebar.selectbox("Page", ["Home", "Buy?", "Maps", "About"])
st.title("Test Interactive Map")
from PIL import Image, ImageEnhance, ImageOps
import os

# --- CONFIG ---
IMAGE_FOLDER = "Europe"  # Your folder with country .png files
MAP_WIDTH = 633  # Optional resizing

# --- LOAD COUNTRIES ---
@st.cache_data
def load_country_images():
    countries = {}
    for filename in os.listdir(IMAGE_FOLDER):
        if filename.endswith(".png"):
            name = filename[:-4]
            path = os.path.join(IMAGE_FOLDER, filename)
            img = Image.open(path).convert("RGBA")
            countries[name] = img
    return countries

country_images = load_country_images()
country_names = sorted(country_images.keys())

# --- STATE HANDLING ---
if "colored_layers" not in st.session_state:
    st.session_state.colored_layers = {}

# --- SHOW MAP ---
def compose_map(layers):
    base = Image.new("RGBA", next(iter(country_images.values())).size, (0, 0, 0, 1))
    for country, color in layers.items():
        original = country_images[country]
        # Tint the image
        tinted = ImageOps.colorize(original.convert("L"), black="black", white=color)
        tinted.putalpha(original.split()[-1])  # Retain alpha
        base = Image.alpha_composite(base, tinted)
    return base


# --- DISPLAY CURRENT MAP ---
st.subheader("Current Map")
composite_map = compose_map(st.session_state.colored_layers)
st.image(composite_map.resize((MAP_WIDTH, int(MAP_WIDTH * composite_map.height / composite_map.width))))

# --- CONTROLS ---
st.subheader("Update a Country")
with st.form("update_form"):
    country = st.selectbox("Select a country", country_names)
    color = st.color_picker("Choose a color")
    submitted = st.form_submit_button("Apply")

if submitted:
    st.session_state.colored_layers[country] = color
    st.experimental_rerun()
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
