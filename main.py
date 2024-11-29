import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the Gemini Vision Model
model = genai.GenerativeModel('gemini-1.5-flash') #gemini-pro-vision

def get_gemini_response(inout_prompt, image, user_input_prompt):
    response = model.generate_content([input_prompt, image[0], user_input_prompt])
    return response.text

def input_image_bytes(uploaded_file):
    if uploaded_file is not None:
        #convert the uploaded file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded!!!")
    
if __name__ == "__main__":
    main()    