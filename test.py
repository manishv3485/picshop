# install first:
# pip install openai streamlit pillow

import streamlit as st
import openai
from PIL import Image
import io

openai.api_key = "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"

st.title("picshop")

mode = st.radio("Choose Mode:", ["Generate Image", "Edit Image"])

if mode == "Generate Image":
    prompt = st.text_input("Enter your prompt:", "A beautiful sunset over the ocean")
    if st.button("Generate"):
        with st.spinner("Creating magic..."):
            result = openai.images.generate(
                model="gpt-image-1",  # DALL·E 3
                prompt=prompt,
                size="512x512"
            )
            image_url = result.data[0].url
            st.image(image_url, caption="Generated Image")

elif mode == "Edit Image":
    uploaded = st.file_uploader("Upload an image to edit", type=["png", "jpg", "jpeg"])
    prompt = st.text_input("Describe what to edit:", "Make it look like a painting")
    if uploaded and st.button("Edit"):
        with st.spinner("Editing image..."):
            result = openai.images.edit(
                model="gpt-image-1",
                image=uploaded,
                prompt=prompt,
                size="512x512"
            )
            edited_url = result.data[0].url
            st.image(edited_url, caption="Edited Image")
