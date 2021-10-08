import streamlit as st
from PIL import Image
import random
import os


st.title('This OCT does not exist')

path = r"/Users/peterwoodward-court/Documents/thisoctdoesnotexist/images/"
random_image = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
])

st.title(random_image)

image = Image.open('/Users/peterwoodward-court/Documents/thisoctdoesnotexist/images/' + random_image)
st.image(image)

