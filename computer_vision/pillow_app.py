import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

img_file = st.file_uploader("upload image",['jpg','png'])
if img_file:
    im = Image.open(img_file)
    st.write(im.size)
    st.write(im.mode)
    st.write(im.format)
    st.write(im.info)
    st.image(im)
  
w= st.number_input('width of image',value=0)
h= st.number_input('height of image',value=0) 
sv= st.checkbox('save image?') 
if st.button("chamge resolution") and im:
    scaled_im = im.resize((w,h))
    st.image(scaled_im)
    if sv:
        scaled_im.save('output.png',format='png')
deg = st.slider('degrees',min_value==0,max_value=360)
svr = st.checkbox('save rotated image?')
if st.button('rotate image') and im:
    rot_img = img.rotate(deg,fillcolor=colr)
    st.image(rot_img)
    if svr:
        rot_img.save('rotated.png',format='png')
if st.checkbox('show filters'):
    cols = st.beta_column(3) 
    with cols[0]:
        st.image(im.filter(ImageFilter.EMBOSS,use_column_width=True))
    with cols[1]:
        st.image(im.filter(ImageFilter.CONTOUR),use_column_width=True)
    with cols[2]:
        st.image(im.filter(ImageFilter.GaussianBlur(10)),use_column_width=True)


    cols = st.beta_column(3) 
    with cols[0]:
        st.image(im.filter(ImageFilter.MinFilter,use_column_width=True))
    with cols[1]:
        st.image(im.filter(ImageFilter.MaxFilter),use_column_width=True)
    with cols[2]:
        st.image(im.filter(ImageFilter.MedianFilter(7)),use_column_width=True)


 