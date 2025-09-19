import streamlit as web
from PIL import Image

img  = Image.open("favi.png")

web.write("# Rayyan Made This")

web.set_page_config(page_title="Rayyan :)" , page_icon=img)

if web.button("Click to Celebrate !!!") :

    web.balloons

