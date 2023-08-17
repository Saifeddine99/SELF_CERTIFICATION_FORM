import streamlit as st 
import datetime

import json

def clinical():
    #'diagnosis-workfit.v0_20230808104544_000001_1.json': This is a json file containing standard demographic data in the OpenEHR standards form
    full_path_clinical_data = 'diagnosis-workfit.v0_20230808104544_000001_1.json'

    st.markdown("<h1 style='text-align: center;color: #0B5345;'>Enter your clinical data from here </h1>", unsafe_allow_html = True)
    st.write("#")

    col_a,col_b,col_c,col_73,col_d=st.columns([2,0.1,2,0.1,2])

    with col_a:
        #Getting National Insurance Number:
        st.subheader("Problem/ Diagnosis name:")
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
    
    with col_d:
        #Sickness related to work:(yes/no)
        st.subheader("Sickness related to work:")
        sickness=st.selectbox(
        "l",
        ('Yes','No'),
        label_visibility="hidden"
        )
        st.info(f' : You selected: {sickness}',icon="🚨")
        st.write("#")

    col_aab63,col_aaba,col_aabb,col_aabc,col_aab73=st.columns([0.1,2,0.1,2,0.1])
    with col_aaba:
        #Getting Clock Payroll number:
        st.subheader("Last date of work before sickness began:")
        last_date_of_work= st.date_input(
            "",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            )
        st.info(f' : Your last date of work is on: {last_date_of_work}',icon="🚨")
        st.write("#")
    
    with col_aabc:
        #End of shift time:
        st.subheader("What time did you finish work on that date?")
        time_of_finishing_work = st.time_input('Set an alarm for', datetime.time(00, 00,00), label_visibility ="hidden",step=60)
        st.info(f' : You selected {time_of_finishing_work} as your end of shift time',icon="🚨")
        

    col_ab63,col_aba,col_abb,col_abc,col_ab73=st.columns([0.1,2,0.1,2,0.1])

    with col_aba:
        #Getting "Date/time of onset:
        st.subheader("What date did your sickness begin?")
        date_of_sickness_beginning= st.date_input(
            "dzfd",
            min_value=datetime.date(1923,1,1),
            max_value=datetime.date.today(),
            label_visibility ="hidden"
            )
        st.info(f' : Your date of onset is on: {date_of_sickness_beginning}',icon="🚨")
        st.write("#")

    
    with col_abc:
        #Date/time of resolution:
        st.subheader("Resolution date:")
        knowing_sickness_end=st.selectbox(
        "Do you know what date did your sickness end ?",
        ('Yes','No'),  
        )

        if (knowing_sickness_end=="Yes"):
            date_of_resolution= st.date_input(
                "Enter this date:",
                min_value=datetime.date(1923,1,1),
                max_value=datetime.date.today(),
                )
            st.info(f' : Date of resolution is: {date_of_resolution}',icon="🚨")
        else:
            date_of_resolution=datetime.date(1923,1,1) 
        st.write("#")


    if(len(clinical_description)>0 and len(problem_diagnosis_name)>0):
        #Demographic data file:
        with open(full_path_clinical_data, 'r') as openfile:
            # Reading from json file
            json_object_clinical_data = json.load(openfile)
        
        json_object_clinical_data=add_clinical_data(json_object_clinical_data,clinical_description,problem_diagnosis_name,last_date_of_work,sickness,time_of_finishing_work,date_of_resolution,date_of_sickness_beginning)

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

def add_clinical_data(json_object_clinical_data,clinical_description,problem_diagnosis_name,last_date_of_work,sickness,time_of_finishing_work,date_of_resolution,date_of_sickness_beginning):

    json_object_clinical_data["content"][0]["data"]["items"][0]["value"]["value"]=problem_diagnosis_name
    json_object_clinical_data["content"][0]["data"]["items"][1]["value"]["value"]=clinical_description
    json_object_clinical_data["content"][0]["data"]["items"][2]["value"]["value"]=str(date_of_sickness_beginning)
    json_object_clinical_data["content"][0]["data"]["items"][4]["value"]["value"]=str(last_date_of_work)
    json_object_clinical_data["content"][0]["data"]["items"][5]["value"]["value"]=str(time_of_finishing_work)
    if (sickness=="Yes"):
        json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["value"]=1
        json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["symbol"]["value"]=sickness
        json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["symbol"]["defining_code"]["code_string"]="at0083"

    json_object_clinical_data["content"][0]["data"]["items"][7]["value"]["value"]=str(date_of_resolution)

    return(json_object_clinical_data)