import streamlit as st 
import datetime

import json

def clinical():
    #'diagnosis-workfit.v0_20230808104544_000001_1.json': This is a json file containing standard demographic data in the OpenEHR standards form
    full_path_clinical_data = 'diagnosis-workfit.v0_20230808104544_000001_1.json'

    st.markdown("<h1 style='text-align: center;color: #0B5345;'>Enter your clinical data from here </h1>", unsafe_allow_html = True)
    st.write("#")

    col_63,col_a,col_b,col_c,col_73=st.columns([0.1,2,0.1,2,0.1])

    with col_a:
        #Getting National Insurance Number:
        st.subheader("Problem/Diagnosis name:")
        problem_diagnosis_name=st.text_area(":hdd",label_visibility ="hidden")
        if (len(problem_diagnosis_name)==0):
            st.warning(": You entered nothing!" ,icon="⚠️")
        st.write("#")

    with col_c:
        #Getting patient's name:
        st.subheader("Clinical description:")
        clinical_description= st.text_area('Enter text: ',label_visibility ="hidden")
        if (len(clinical_description)==0):
            st.warning(": You entered nothing !" ,icon="⚠️")
        st.write("#")

    col_aab63,col_aaba,col_aabb,col_aabc,col_aab73=st.columns([0.1,2,0.1,2,0.1])
    with col_aaba:
        #Getting Clock Payroll number:
        st.subheader("Last date of work:")
        last_date_of_work= st.date_input(
            "",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            )
        st.info(f' : Your last date of work is on: {last_date_of_work}',icon="🚨")
        st.write("#")
    
    with col_aabc:
        #Getting "Date/time of onset:
        st.subheader("Date of onset:")
        date_of_onset= st.date_input(
            "dzfd",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            label_visibility ="hidden"
            )
        st.info(f' : Your date of onset is on: {date_of_onset}',icon="🚨")
        st.write("#")

    col_a63,col_aa,col_ab,col_ac,col_a73=st.columns([0.1,2,0.1,2,0.1])

    with col_aa:
        #Date/time clinically recognised:
        st.subheader("Date clinically recognised:")
        date_clinically_recognised= st.date_input(
            "efef",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            label_visibility ="hidden"
            )
        st.info(f' : Your last date of work is on: {date_clinically_recognised}',icon="🚨")
        st.write("#")
    
    with col_ac:
        #Sickness related to work:(yes/no)
        st.subheader("Sickness related to work:")
        sickness=st.selectbox(
        "l",
        ('Yes','No'),
        label_visibility="hidden"
        )
        st.info(f' : You selected: {sickness}',icon="🚨")
        st.write("#")

    col_ab63,col_aba,col_abb,col_abc,col_ab73=st.columns([0.1,2,0.1,2,0.1])

    with col_aba:
        #End of shift time:
        st.subheader("End of shift time:")
        end_of_shift_time = st.time_input('Set an alarm for', datetime.time(00, 00,00), label_visibility ="hidden",step=60)
        st.info(f' : You selected {end_of_shift_time} as your end of shift time',icon="🚨")
    
    with col_abc:
        #Date/time of resolution:
        st.subheader("Resolution date:")
        date_of_resolution= st.date_input(
            "efefd",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            label_visibility ="hidden"
            )
        st.info(f' : Date of resolution is: {date_of_resolution}',icon="🚨")
        st.write("#")

    if(len(clinical_description)>0 and len(problem_diagnosis_name)>0):
        #Demographic data file:
        with open(full_path_clinical_data, 'r') as openfile:
            # Reading from json file
            json_object_clinical_data = json.load(openfile)
        
        json_object_clinical_data=add_clinical_data(json_object_clinical_data,clinical_description,problem_diagnosis_name,last_date_of_work,date_clinically_recognised,sickness,end_of_shift_time,date_of_resolution,date_of_onset)

        json_object_clinical_data = json.dumps(json_object_clinical_data, indent=4)

        st.write("#")
        st.write("#")
        st.subheader("You can download the 'Clinical data' related to this patient for here:")
        st.write("#")

        col1, col2, col3 = st.columns([4,2,3])
        with col2:    
            download_clinical = st.download_button('Download clinical data', json_object_clinical_data, file_name="clinical data for SSP.json")
        if (download_clinical):
            st.write("#")
            st.success(": File saved well" ,icon="✅")

    else:
        st.write("#")
        st.error(": One of the values you entered is invalid, Please check them carefully!",icon="⛔")

    return()

def add_clinical_data(json_object_clinical_data,clinical_description,problem_diagnosis_name,last_date_of_work,date_clinically_recognised,sickness,end_of_shift_time,date_of_resolution,date_of_onset):

    json_object_clinical_data["content"][0]["data"]["items"][0]["value"]["value"]=problem_diagnosis_name
    json_object_clinical_data["content"][0]["data"]["items"][1]["value"]["value"]=clinical_description
    json_object_clinical_data["content"][0]["data"]["items"][2]["value"]["value"]=str(date_of_onset)
    json_object_clinical_data["content"][0]["data"]["items"][3]["value"]["value"]=str(date_clinically_recognised)
    json_object_clinical_data["content"][0]["data"]["items"][4]["value"]["value"]=str(last_date_of_work)
    json_object_clinical_data["content"][0]["data"]["items"][5]["value"]["value"]=str(end_of_shift_time)
    if (sickness=="Yes"):
        json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["value"]=1
        json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["symbol"]["value"]=sickness
        json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["symbol"]["defining_code"]["code_string"]="at0083"

    json_object_clinical_data["content"][0]["data"]["items"][7]["value"]["value"]=str(date_of_resolution)

    return(json_object_clinical_data)