import streamlit as st
import tensorflow as tf


@st.cache_resource
def load_model():
    model=tf.keras.models.load_model('my_model.hdf5')
    return model
model = load_model()
    
# File Processing Pkgs
from PIL import Image, ImageOps
import cv2
import numpy as np

def import_and_predict(image_data,model):
    
    img = Image.open(imageFile)
    img = img.resize((64,64))
    image_array = np.array(img)
    image = Image.fromarray(image_array, 'RGB')
    image = np.array(image)
    new_img= np.expand_dims(image, axis=0)


    prediction = model.predict(new_img)

    return prediction


#load images
@st.cache_data
def load_image(imageFile):
    img = Image.open(imageFile)
    return img


st.title("Malaria Cell Detector")
imageFile = st.file_uploader("Upload Images", type="png")

col1, col2 = st.columns(2, gap="small")

if col1.button('Detect'):

    result = import_and_predict(imageFile,model)
    class_names=['Parisitized','Uninfected']
    string=class_names[np.argmax(result)]
    st.header(string)
    
if col2.button('Show Image'):
    if imageFile is not None:
        st.image(load_image(imageFile), width=200)
        

