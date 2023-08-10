import streamlit as st 
from streamlit_option_menu import option_menu

import PIL as pillow
from PIL import Image

import os

from clinical_data import clinical
from demographic_data import demographic
from self_certification import self_certif

page_icon_img=Image.open(os.path.join("images","Sick-employees.jpeg"))


#this function allows to add the page title and icon
st.set_page_config(page_title="Self Certification Form", page_icon=page_icon_img, layout="centered", initial_sidebar_state="expanded")

#this option menu allows user to choose the web page he wants to visit https://www.youtube.com/watch?v=hEPoto5xp3k&t=77s&ab_channel=CodingIsFun
with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Home page","Demographic data","Clinical data","Self Certification","Log out"],
        icons=["house","geo-alt-fill","clipboard2-pulse","filetype-pdf","box-arrow-right"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
                    "container": {"margin": "0px !important","padding": "0!important", "align-items": "stretch", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "20px",
                        "text-align": "center",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                },
    )

#If the user selects "home" from the option menu Streamlit will run this "if" condition
if selected=="Home page":
    st.write('#')
    st.write('#')
    st.markdown(
    "<h1 style='text-align: center; color: #0B5345;'>Welcome to the Home Page !  </h1>", 
    unsafe_allow_html = True
    )

    home_image=Image.open(os.path.join("images","My project.png"))
    st.image(home_image)
    st.write('#')

    text, anim = st.columns((2, 1))

    #The below code is related to demographic data stuff
    with text:
        
        st.write('#')
        st.subheader('1/You can click on "Demographic data" button in "Main menu" to submit your demographic data and receive it in an OpenEHR standards format ".JSON" file')
    demographic_icon=Image.open(os.path.join("images","demographics.png"))
    with anim:
        st.image(demographic_icon, width=250)

    #The below code is related to clinical data stuff
    with text:
        st.write('#')
        st.write('#')
        st.write('#')
        st.write('#')
        st.write('#')
        
        st.subheader('2/You can click on "Clinical data" button in "Main menu" to submit your clinical data and receive it in an OpenEHR standards format ".JSON" file')
    clinical_image=Image.open(os.path.join("images","clinical_report.png"))
    with anim:
        st.write('#')
        st.write('#')
        st.write('#')
        st.image(clinical_image, width=250)


if selected=="Demographic data":
    demographic()

if selected=="Clinical data":
    clinical()

if selected=="Self Certification":
    self_certif()

if selected=="Log out":
    st.write("This stuff is still not ready")