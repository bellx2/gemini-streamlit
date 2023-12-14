import streamlit as st
import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


def main():
    my_api_key = os.getenv('GOOGLE_API_KEY')
    st.title('Gemini Pro / Vision')
    if my_api_key is None:
        my_api_key = st.text_input('Google API Key')
    # APIキーの設定
    genai.configure(api_key=my_api_key)
    model_type = st.selectbox('Model', ['Text', 'Text & Image'])
    text = st.text_input('Talk to Gemini Pro')
    if model_type != 'Text':
        image_file = st.file_uploader('Upload Image')
    if st.button('Send'):
        if my_api_key == "":
            st.error('Google API Key Required')
            return
        if model_type == 'Text':
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content([text])
        else:
            model = genai.GenerativeModel('gemini-pro-vision')
            image = PIL.Image.open(image_file)
            if text == '':
                text = 'この画像について説明してください'
            response = model.generate_content([text, image])
        st.markdown(response.text)


if __name__ == "__main__":
    main()
