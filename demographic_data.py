import streamlit as st

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
        st.subheader("First name:")
        first_name=st.text_input("enter your name:",label_visibility ="collapsed")
        if (len(first_name)==0):
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
        #Getting patient's Title:
        st.subheader("Title:")
        title=st.selectbox(
        "ld",
        ('MR', 'MRS', 'MISS', 'MS', 'Other title'),
        label_visibility="collapsed"
        )
        if (title != "Other title"):
            st.info(f' You selected: {title}',icon="🚨")
        else:
            title=st.text_input("Enter the other title:")
            if (len(title)==0):
                st.warning(": You entered nothing !" ,icon="⚠️")

        st.write("#")
    

    col_11,col_12,col_13,col_14,col_15=st.columns([2,0.1,2,0.1,2])
    with col_11:
        #Getting patient's birth day:
        st.subheader("Birth date:")
        birthday = st.date_input(
            "",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            label_visibility ="collapsed"
            )
        st.info(f' Your birth date is on: {birthday}',icon="🚨")

    with col_13:
        #Getting country code:
        st.subheader("Country code:")
        country_code=st.number_input(":dh",min_value=0,step=1,label_visibility ="collapsed")
        if (country_code==0):
            st.warning(": You entered nothing !" ,icon="⚠️")

    with col_15:
        #Getting patient's phone number
        st.subheader("Phone number:") 
        phone_number=st.number_input(":hz",min_value=0,step=1,label_visibility ="collapsed")
        if (phone_number==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")


    col_63,col_a,col_b,col_c,col_73=st.columns([0.1,2,0.1,2,0.1])
    with col_a:
        #Getting National Insurance Number:
        st.subheader("National Insurance N°:")
        national_insurance=st.number_input(":hdd",min_value=0,max_value=999999999,step=1,label_visibility ="collapsed")
        if (national_insurance==0):
            st.warning(": You entered nothing!" ,icon="⚠️")
        st.write("#")
    with col_c:
        #Getting Clock Payroll number:
        st.subheader("Payroll N°:")
        clock_payroll=st.number_input(":egrh",min_value=0,max_value=99999999999999,step=1,label_visibility ="collapsed")
        if (clock_payroll==0):
            st.warning(": You entered nothing!" ,icon="⚠️")
        st.write("#")

    if(len(title)>0 and len(first_name)>0 and len(surname)>0 and country_code and clock_payroll and national_insurance and phone_number):
        #Demographic data file:
        with open(full_path_demographic_data, 'r') as openfile:
            # Reading from json file
            json_object_demographic_data = json.load(openfile)

        #demographic data:
        json_object_demographic_data=add_demographic_data(json_object_demographic_data,title,first_name,surname,country_code,clock_payroll,national_insurance,phone_number,birthday)
        
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
def add_demographic_data(json_object_demographic_data,title,first_name,surname,country_code,clock_payroll,national_insurance,phone_number,birthday):
    

    json_object_demographic_data["contacts"][0]["addresses"][2]["details"]["items"][0]["value"]["value"]=phone_number
    json_object_demographic_data["contacts"][0]["addresses"][2]["details"]["items"][1]["value"]["value"]=country_code
    json_object_demographic_data["identities"][0]["details"]["items"][0]["value"]["value"]=first_name
    json_object_demographic_data["identities"][0]["details"]["items"][1]["value"]["value"]=surname
    json_object_demographic_data["identities"][0]["details"]["items"][2]["value"]["value"]=title
    json_object_demographic_data["identities"][0]["details"]["items"][3]["value"]["value"]=str(birthday)

    json_object_demographic_data["identities"][0]["details"]["items"][6]["value"]["value"]=national_insurance
    json_object_demographic_data["identities"][0]["details"]["items"][7]["value"]["value"]=clock_payroll

    
    return(json_object_demographic_data)