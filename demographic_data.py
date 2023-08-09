import streamlit as st
def demographic():

    st.markdown("<h1 style='text-align: center;color: #0B5345;'>Enter your demographic data from here </h1>", unsafe_allow_html = True)
    st.write("#")

    col_1,col_2,col_3,col_4,col_5=st.columns([2,0.1,2,0.1,2])
    with col_1:
        #Getting Street name:
        st.subheader("Street name:")
        street_name=st.text_input(":sde",label_visibility ="collapsed")
        if (len(street_name)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

        #Getting Country :
        st.subheader("Country:")
        country=st.text_input("Current_country Identifier",label_visibility ="hidden")
        if (len(country)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")

    with col_3:
        #Getting Street number:
        st.subheader("Street N°:")
        street_number=st.number_input(":h",min_value=0,step=1,label_visibility ="collapsed")
        if (street_number==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

        #Getting Province:
        st.subheader("Province:")
        province=st.text_input("Current State/territory/province:")
        if (len(province)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

    with col_5:
        #Getting patient's postal_code:
        st.subheader("Postal Code:")
        postal_code=st.text_input("enter your postal code:",label_visibility ="collapsed")
        correct_postal_code=True
        if (len(postal_code)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
            correct_postal_code=False
        elif (postal_code.isnumeric() is False or len(postal_code)!=5):
            st.error("Postal code must be composed of 5 numbers" ,icon="❌")
            correct_postal_code=False
        st.write("#")

        #Getting Town:
        st.subheader("Town:")
        town=st.text_input("Current Suburb/town/locality:")
        if (len(town)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")
    return()