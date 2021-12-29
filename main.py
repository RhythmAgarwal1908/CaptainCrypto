import streamlit as st
import os
from subprocess import call
import time
import zipfile
import shutil


zip_file = st.file_uploader("Upload An Zip",type=['zip'])

if zip_file is not None:
    file_details = {"FileName":zip_file.name,"FileType":zip_file.type}
    st.write(file_details)
    with open(os.path.join(zip_file.name),"wb") as f:
      f.write(zip_file.getbuffer())         
    st.success("Saved File")
    st.info("UnZiping File")
    time.sleep(1)
    with zipfile.ZipFile(f'./{zip_file.name}', 'r') as zip_ref:
        zip_ref.extractall('./')
    st.success("Unziped Success")
    time.sleep(5)
    st.info("Removing Zip File")
    os.remove('./traits.zip')
    st.success("Removed Zip File")
    time.sleep(10)
    st.info("Generating Images")
    class CallPy(object):
        def __init__(self, path="generator.py"):
            self.path = path
        def call_python_file(self):
            call(["Python", "{}".format(self.path)])
    c = CallPy()
    c.call_python_file()
    time.sleep(1)
    st.success("Image Generated")
    time.sleep(3)
    st.info("Removing Trait Folder")
    shutil.rmtree('traits')
    time.sleep(3)
    st.info("Making Zip For Results")
    time.sleep(3)
    shutil.make_archive('results', 'zip', './output')
    st.success("Made Zip For Results")
    time.sleep(5)
    with open('results.zip', 'rb') as f:
        st.download_button('Download Zip', f, file_name='results.zip')
    time.sleep(10)
    shutil.rmtree("output")
    os.mkdir('output')
    os.remove('./results.zip')