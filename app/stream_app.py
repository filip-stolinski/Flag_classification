import tensorflow as tf
import streamlit as st
import os
from PIL import Image
import numpy as np
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


with open('class_names.txt') as temp_file:
    class_list = [line.rstrip('\n') for line in temp_file]


def load_image():
    uploaded_file = st.file_uploader(
        label='Pick a flag image to make prediction')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        img = Image.open(uploaded_file).convert('RGB')
        image_array = tf.keras.utils.img_to_array(img)

        return image_array


def load_model():
    model = tf.keras.models.load_model("my_h5_model_8_5.h5")
    return model


def predict(model, image_data):
    img_array = tf.image.resize(image_data, (180, 240))
    img_array = tf.expand_dims(img_array, 0)

    prediction = model.predict(img_array)
    class_pred = class_list[np.argmax(prediction)]

    st.subheader(f'This is the flag of {class_pred}.')


def main():
    st.title('Classify your flag')
    model = load_model()
    image = load_image()
    result = st.button('Run CNN on image')
    if result:
        st.write('Calculating results...')
        predict(model, image)


if __name__ == '__main__':
    main()
