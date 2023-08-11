import streamlit as st
from validate_email_address import validate_email
import datetime

import json 

def demographic():
    #'patient.v0_20230713112750_000001_1.json': This is a json file containing standard demographic data in the OpenEHR standards form
    full_path_demographic_data = 'patient.v2_20230808093040_000001_1.json'

    st.markdown("<h1 style='text-align: center;color: #0B5345;'>Enter your demographic data from here </h1>", unsafe_allow_html = True)
    st.write("#")


    col_1,col_2,col_3,col_4,col_5=st.columns([2,0.1,2,0.1,2])
    with col_1:
        #Getting patient's name:
        st.subheader("Name:")
        name=st.text_input("enter your name:",label_visibility ="collapsed")
        if (len(name)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

    with col_3:
        #Getting patient's Surname:
        st.subheader("Surname:")
        surname=st.text_input("",label_visibility ="collapsed")
        if (len(surname)==0):
            st.warning(": You entered nothing !" ,icon="⚠️") 
        st.write("#") 

    with col_5:
        #Getting patient's gender:
        st.subheader("Gender:")
        status = st.radio("", ('Male', 'Female'),label_visibility="collapsed")
        st.write("#")

    
    col_11,col_12,col_13,col_14,col_15=st.columns([2,0.1,2,0.1,2])
    with col_11:
        #Getting patient's Title:
        st.subheader("Title:")
        title=st.text_input("enter your title:",label_visibility ="collapsed")
        if (len(title)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

    with col_13:
        #Getting patient's birth day:
        st.subheader("Birth date:")
        birthday = st.date_input(
            "",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            label_visibility ="collapsed"
            )
        st.write('Your birth date is on:',birthday)

    with col_15:
        #Getting patient's Marital status:
        st.subheader("Marital status:")
        marital_status= st.selectbox(
        "l",
        ('Single', 'Married', 'Widowed', 'Divorced', 'Separated','Registered partnership'),
        label_visibility="collapsed"
        )
        st.write('You selected:', marital_status)


    col_21,col_22,col_23,col_24,col_25=st.columns([2,0.1,2,0.1,2])
    with col_21:
        #Getting patient's email address:
        st.subheader("Email address:")
        email = st.text_input("Enter your email address", label_visibility ="collapsed")
        # Validate Email and Display Result
        if email:
            if validate_email(email)==False:
                st.error(": Invalid email address",icon="❌")
        else:
            st.warning(": You entered nothing !" ,icon="⚠️")
    with col_23:
        #Getting country code:
        st.subheader("Country code:")
        country_code=st.number_input(":dh",min_value=0,step=1,label_visibility ="collapsed")
        if (country_code==0):
            st.warning(": You entered nothing !" ,icon="⚠️")

    with col_25:
        #Getting patient's phone number
        st.subheader("Phone number:") 
        phone_number=st.number_input(":hz",min_value=0,step=1,label_visibility ="collapsed")
        if (phone_number==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")


    col_31,col_32,col_33,col_34,col_35=st.columns([2,0.1,2,0.1,2])
    with col_31:
        #Getting Country :
        st.subheader("Country:")
        country=st.text_input("Current_country Identifier",label_visibility ="hidden")
        if (len(country)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")

    with col_33:
        #Getting Province:
        st.subheader("Province:")
        province=st.text_input("Current State/territory/province:")
        if (len(province)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")
        
    with col_35:
        #Getting Town:
        st.subheader("City:")
        town=st.text_input("Current Suburb/town/locality:")
        if (len(town)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")


    col_41,col_42,col_43,col_44,col_45=st.columns([2,0.1,2,0.1,2])
    with col_41:
        #Getting Street name:
        st.subheader("Street Name:")
        street_name=st.text_input(":sde",label_visibility ="collapsed")
        if (len(street_name)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

    with col_43:
        #Getting Street number:
        st.subheader("Street N°:")
        street_number=st.number_input(":h",min_value=0,step=1,label_visibility ="collapsed")
        if (street_number==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

        
    with col_45:
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
    

    col_63,col_a,col_b,col_c,col_73=st.columns([0.1,2.5,0.1,2,0.1])
    with col_a:
        #Getting National Insurance Number:
        st.subheader("National Insurance N°:")
        national_insurance=st.number_input(":hdd",min_value=0,step=1,label_visibility ="collapsed")
        if (national_insurance==0):
            st.warning(": You entered nothing!" ,icon="⚠️")
        st.write("#")
    with col_c:
        #Getting Clock Payroll number:
        st.subheader("Clock Payroll N°:")
        clock_payroll=st.number_input(":egrh",min_value=0,step=1,label_visibility ="collapsed")
        if (clock_payroll==0):
            st.warning(": You entered nothing!" ,icon="⚠️")
        st.write("#")

    if(len(title)>0 and len(name)>0 and len(surname)>0 and country_code and validate_email(email) and clock_payroll and national_insurance and phone_number and len(street_name)>0 and street_number>0 and correct_postal_code and len(country)>0 and len(province)>0 and len(town)>0):
        #Demographic data file:
        with open(full_path_demographic_data, 'r') as openfile:
            # Reading from json file
            json_object_demographic_data = json.load(openfile)

        #demographic data:
        json_object_demographic_data=add_demographic_data(json_object_demographic_data,marital_status,title,name,surname,country_code,email,clock_payroll,national_insurance,phone_number,status,birthday,street_name,street_number,postal_code,country,province,town)
        
        json_object_demographic_data = json.dumps(json_object_demographic_data, indent=4)

        st.write("#")
        st.write("#")
        st.subheader("You can download the 'Demographic data' related to this patient for here:")
        st.write("#")

        col1, col2, col3 = st.columns([4,2,3])
        with col2:    
            download_demographics = st.download_button('Download demographic data', json_object_demographic_data, file_name="demographic data for SSP.json")
        if (download_demographics):
            st.write("#")
            st.success(": File saved well" ,icon="✅")
    else:
        st.write("#")
        st.error(": One of the values you entered is invalid, Please check them carefully!",icon="⛔")




#This function adds the submitted demographic_data to the demographics json file 
def add_demographic_data(json_object_demographic_data,marital_status,title,name,surname,country_code,email,clock_payroll,national_insurance,phone_number,status,birthday,street_name,street_number,postal_code,country,province,town):
    
    json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][0]["value"]["value"]=street_name
    json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][1]["value"]["value"]=street_number
    json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][2]["value"]["value"]=postal_code
    json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][3]["value"]["value"]=province
    json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][4]["value"]["value"]=town
    json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][5]["value"]["value"]=country
    json_object_demographic_data["contacts"][0]["addresses"][1]["details"]["items"][0]["value"]["value"]=email
    json_object_demographic_data["contacts"][0]["addresses"][2]["details"]["items"][0]["value"]["value"]=phone_number
    json_object_demographic_data["contacts"][0]["addresses"][2]["details"]["items"][1]["value"]["value"]=country_code
    json_object_demographic_data["identities"][0]["details"]["items"][0]["value"]["value"]=name
    json_object_demographic_data["identities"][0]["details"]["items"][1]["value"]["value"]=surname
    json_object_demographic_data["identities"][0]["details"]["items"][2]["value"]["value"]=title
    json_object_demographic_data["identities"][0]["details"]["items"][3]["value"]["value"]=str(birthday)
    json_object_demographic_data["identities"][0]["details"]["items"][4]["value"]["value"]=marital_status
    
    if(status=="Female"):
        json_object_demographic_data["identities"][0]["details"]["items"][5]["value"]["value"]=status
        json_object_demographic_data["identities"][0]["details"]["items"][5]["value"]["defining_code"]["code_string"]="at0027"
    
    json_object_demographic_data["identities"][0]["details"]["items"][6]["value"]["value"]=national_insurance
    json_object_demographic_data["identities"][0]["details"]["items"][7]["value"]["value"]=clock_payroll

    
    return(json_object_demographic_data)