import streamlit as st

st.title("Welcome to A Geography Channel Games")
page = st.sidebar.selectbox("Page", ["Home", "Buy?", "Maps", "About"])
st.title("Test Interactive Map")

#INTERACTIVETEST
import streamlit as st
from PIL import Image
import os
from streamlit_image_coordinates import streamlit_image_coordinates

# --- CONFIG ---
IMAGE_FOLDER = "Europe"
MAP_WIDTH = 633  # Resize for display


# --- LOAD COUNTRY IMAGES ---
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
if "map_size" not in st.session_state:
    sample_img = next(iter(country_images.values()))
    aspect = sample_img.height / sample_img.width
    st.session_state.map_size = (MAP_WIDTH, int(MAP_WIDTH * aspect))

# --- COMPOSITE MAP ---
def compose_map(layers):
    base = Image.open("map.png").convert("RGBA")
    for country, color in layers.items():
        original = country_images[country]
        solid = Image.new("RGBA", original.size, color)
        mask = original.split()[-1]
        tinted = Image.composite(solid, Image.new("RGBA", original.size, (0, 0, 0, 0)), mask)
        base = Image.alpha_composite(base, tinted)
    return base
st.markdown("### 🌍 Europe 2025")

color = st.color_picker("🎨 Select a color to apply", value="#ff0000")

composite_map = compose_map(st.session_state.colored_layers)
resized_map = composite_map.resize(st.session_state.map_size)

coords = streamlit_image_coordinates(resized_map, key="map")

if page == "Maps":
    game = st.sidebar.selectbox("Select Game", ["Europe 2025", "The Americas 2025", "Africa 2025", "Asia 2025", "Southeast Asia + Oceania 2025"])

    if game == "Europe 2025":
        st.markdown("### 🌍 Europe 2025")
        color = st.color_picker("🎨 Select a color to apply", value="#ff0000")

        composite_map = compose_map(st.session_state.colored_layers)
        resized_map = composite_map.resize(st.session_state.map_size)

        coords = streamlit_image_coordinates(resized_map, key="map")

        if coords is not None:
            x_ratio = resized_map.width / composite_map.width
            y_ratio = resized_map.height / composite_map.height
            x = int(coords["x"] / x_ratio)
            y = int(coords["y"] / y_ratio)

            selected_country = None
            for name, img in country_images.items():
                if x >= img.width or y >= img.height:
                    continue
                _, _, _, a = img.getpixel((x, y))
                if a > 0:
                    selected_country = name
                    break

            if selected_country:
                st.session_state.colored_layers[selected_country] = color
                st.rerun()

        st.image(resized_map)

    elif game == "The Americas 2025":
        st.image("Main Maps/The Americas map.png")
    elif game == "Africa 2025":
        st.image("Main Maps/Africa map.png")
    elif game == "Asia 2025":
        st.image("Main Maps/Asia map.png")
    elif game == "Southeast Asia + Oceania 2025":
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
