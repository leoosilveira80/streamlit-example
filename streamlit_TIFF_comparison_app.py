#!/usr/bin/env python
# coding: utf-8

# In[1]:

# In[ ]:


import streamlit as st
import cv2
import numpy as np

def compare_images(img1, img2):
    # Load the images
    img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

    # Calculate the absolute difference between the images
    diff = cv2.absdiff(img1, img2)

    # Threshold the difference image to highlight the differences
    _, diff = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the difference image
    cv2.imwrite("difference.tif", diff)

st.title("TIFF Image Comparison")

img1 = st.file_uploader("Upload File 1 (TIFF)", type=["tif"])
img2 = st.file_uploader("Upload File 2 (TIFF)", type=["tif"])

if img1 is not None and img2 is not None:
    compare_images(img1, img2)
    st.image("difference.tif", caption="Difference Image", use_column_width=True)
