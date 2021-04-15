import numpy as np
import streamlit as st
from PIL import Image
import cv2
import imutils
from neural_style_transfer import get_model_from_path, style_transfer

import os

# Style Models Data

style_models_file = ['candy.t7', 'composition_vii.t7', 'feathers.t7',
                     'la_muse.t7', 'mosaic.t7', 'starry_night.t7',
                     'the_scream.t7', 'the_wave.t7', 'udnie.t7']

style_models_name = ['Candy', 'Composition_vii', 'Feathers',
                     'La_muse', 'Mosaic', 'Starry_night',
                     'The_scream', 'The_wave', 'Udnie']

model_path = 'models'

style_models_dict = {name: os.path.join(model_path, filee) for name,
                     filee in zip(style_models_name, style_models_file)}

# Style Images Data

content_images_file = ['ancient_city.jpg', 'blue-moon-lake.jpg',
                       'Dawn Sky.jpg', 'Dipping-Sun.jpg', 'golden_gate.jpg',
                       'Japanese-cherry.jpg', 'jurassic_park.jpg',
                       'Kinkaku-ji.jpg', 'messi.jpg',
                       'sagano_bamboo_forest.jpg', 'Sunlit Mountains.jpg',
                       'tubingen.jpg', 'winter-wolf.jpg', 'JQ.jpg',
                       'JS.jpg', 'AB.jpg', 'AC.jpg']

content_images_name = ['Ancient_city', 'Blue-moon-lake', 'Dawn sky',
                       'Dipping-sun', 'Golden_gate', 'Japanese-cherry',
                       'Jurassic_park', 'Kinkaku-ji', 'Messi',
                       'Sagano_bamboo_forest', 'Sunlit mountains', 'Tubingen',
                       'Winter-wolf', 'JQ', 'JS', 'AB', 'AC']

images_path = 'images'

content_images_dict = {name: os.path.join(images_path, filee) for name,
                       filee in zip(content_images_name, content_images_file)}

# ## Exercices ## #

# ## Exercice 1 : Basic Skills ## #

# 1.1. Put a title at the top of your page

st.title("Neural Style Transfer")

# 1.2. Put a title at the top of your sidebar

st.sidebar.title('Navigation')

# 1.3. Put a header at the top of your page

st.sidebar.header('Options')

# 1.4. Run your application for the first time

# ## Exercise 2 : Use basic components ## #

# 2.1. Create a Selectbox in your sidebar with all the style models name and
#      save its value in a variable : style_model_name

style_model_name = st.sidebar.selectbox("Choose the style model: ",
                                        style_models_name)

style_model_path = style_models_dict[style_model_name]

model = get_model_from_path(style_model_path)

# 2.2. Create a checkbox on the side bar
# 2.2.1. If the checkbox is checked, create a file_uploader to let
#        the user Upload its own file. Only accept "png", "jpg", "jpeg"

if st.sidebar.checkbox('Upload'):
    content_file = st.sidebar.file_uploader("Choose a Content Image",
                                            type=["png", "jpg", "jpeg"])

# 2.2.1. If the checkbox is not checked, let the user choose between
#        all the content
#        images name and save its value in a variable : content_name

else:
    content_name = st.sidebar.selectbox("Choose the content images:",
                                        content_images_name)
    content_file = content_images_dict[content_name]

if content_file is not None:
    content = Image.open(content_file)
    content = np.array(content)  # pil to cv
    content = cv2.cvtColor(content, cv2.COLOR_RGB2BGR)
else:
    st.warning("Upload an Image OR Untick the Upload Button)")
    st.stop()

# ## Exercise 3 : Render your final results ## #

# 3.1. Create a slider on your sidebar to select the quality
#      from 150 to 500, step of 50, default value of 200
#      Store this value in a WIDTH variable

WIDTH = st.sidebar.select_slider('QUALITY (May reduce the speed)',
                                 list(range(150, 501, 50)), value=200)

content = imutils.resize(content, width=WIDTH)
generated = style_transfer(content, model)

# 3.2. Show the source image (content) in the sidebar in BGR channel

st.sidebar.image(content, width=300, channels='BGR')

# 3.3 Show the final result (generated) right in your app

st.image(generated, channels='BGR', clamp=True)
