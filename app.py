import streamlit as st
from PIL import Image

st.title("HOLAA!! MI NOMBRE ES SANTIAGO")
st.header("En este espacio comienzo")
image= Image.open('Charmander.jpg')
st.image(image,caption='charmander')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
