#pip install -r requirements.txt

import streamlit as st
import pytesseract
from PIL import Image

def ocr(image):
    # Convert image to grayscale
    gray_image = image.convert("L")

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(gray_image, lang='eng')
    return text

def main():
    # Set Streamlit app title and description
    st.title("OCR for English Handwritten Text")
    st.write("Upload an image with English handwritten text for OCR.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read image file
        image = Image.open(uploaded_file)

        # Display uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Perform OCR on the image
        if st.button('Perform OCR'):
            text = ocr(image)
            st.write("OCR Result:")
            st.write(text)

if __name__ == "__main__":
    main()
