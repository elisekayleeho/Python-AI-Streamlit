import streamlit as st
from fastai.vision.all import *
import pathlib
import platform

# streamlit is a web application to easily do a rapid prototyping


if platform.system() == "Windows":
    pathlib.PosixPath = pathlib.WindowsPath
else:
    pathlib.WindowsPath = pathlib.PosixPath

# labeling mechanism / function
def cat_or_dog(file_name):
    if file_name[0].isupper():
        return f"CAT-{confidence_level}"
    else:
        return f"DOG-{confidence_level}"

cat_vs_dog_model = load_learner("cat_vs_dog_model2_17_9.pkl")

st.markdown("<h1 style='color: pink;'>Cat or Dog Classifier</h1>", unsafe_allow_html=True)
#st.title("Cat or Dog")
st.text("Created by Gamas Chang")

uploaded_file = st.file_uploader("Choose as image...", type=["jpg", "png", "jpeg"])
if uploaded_file:
    real_img = PILImage.create(uploaded_file)
    resized_img = real_img.resize((224, 224), Image.NEAREST)
    prediction = cat_vs_dog_model.predict(resized_img)
    print(prediction)
    index = int(prediction[1])
    confidence_level = prediction[2]
    confidence_level = confidence_level[index]
    confidence_level = prediction[2][index] * 100
    st.text(f"{prediction[0]} - {confidence_level}")


    if confidence_level > 90:
        label = f"I am {confidence_level:.2f} % sure that it is a {prediction[0]}"
    else:
        label = f"WARNING. It am {confidence_level:.2f} % sure that it is a {prediction[0]}"
    st.text(label)
    st.image(uploaded_file)
    st.text(f"prediction[0]")
    st.image(uploaded_file)

    #***streamlit run cat_vs_dog_classification.py***