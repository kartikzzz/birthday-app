import streamlit as st
import random

# Set the background image
def set_background(image_file):
    with open(image_file, "rb") as image:
        data = image.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{data.encode("base64")});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to add a post-it note
def add_note():
    note = st.text_area("Enter your note:")
    if st.button("Add Note"):
        notes.append(note)

# Initialize notes list
if 'notes' not in st.session_state:
    st.session_state.notes = []

notes = st.session_state.notes

# Set background
set_background("image.jpg")

# Title
st.title("Happy Birthday!")

# Add Note button and section
if st.button("Add Note"):
    add_note()

# Display notes
for note in notes:
    st.markdown(f"<div style='background-color:yellow;padding:10px;margin:10px;border-radius:10px;'>{note}</div>", unsafe_allow_html=True)

# CSS for button positioning
st.markdown(
    """
    <style>
    .stButton > button {
        position: fixed;
        top: 10px;
        right: 10px;
        background-color: yellow;
        color: black;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
