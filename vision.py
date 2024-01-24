from dotenv import load_dotenv
load_dotenv() ## loading all the environment var
from PIL import Image

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel('gemini-pro-vision') #gemini-pro-vision for text

def get_gemini_response(input, image):
    if input:
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# initialise our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key = "input")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("GENERATE")

# if submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader('The Response is')
    st.write(response)