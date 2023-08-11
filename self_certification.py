import streamlit as st

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from io import BytesIO

import json

# This function turns the "done_button" state_session to True (Take a look on st.state_session if you are not familiar with it)
def callback():
    #Button was clicked!
    st.session_state.done_button= True

def generate_pdf(data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    # Add a rectangle for header
    c.setFillColor(colors.blue)
    c.rect(0, 750, letter[0], 50, fill=True)

    # Set font and size for header text
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.white)
    c.drawString(100, 760, "Generated PDF with Design")

    # Set font and size for content
    c.setFont("Helvetica", 12)

    # Add submitted data
    c.drawString(100, 700, "Submitted Data:")
    c.drawString(100, 680, f"Name: {data['name']}")
    c.drawString(100, 660, f"Email: {data['email']}")

    # Add more data fields as needed

    # Add a styled paragraph
    style = getSampleStyleSheet()["Normal"]
    p = Paragraph("This is a sample paragraph with <b>bold</b> and <font color='red'>colored</font> text.", style)
    p.wrapOn(c, 400, 100)
    p.drawOn(c, 100, 620)

    c.save()
    buffer.seek(0)
    return buffer

def self_certif():

    # take a look on st.session_state to understand the utility of this line of code 
    if "done_button" not in st.session_state:
        st.session_state.done_button=False

    st.markdown("<h1 style='text-align: center; color: #0d325c;'>SELF CERTIFICATION FORM (SSP)</h1>", unsafe_allow_html = True)
    st.write('#')
    st.write('#')

    col_0a,col_a,col_0b,col_c,col_0c=st.columns([0.1,2,0.1,2,0.1])

    with col_a:
        #Getting clinical json file:
        st.subheader("Enter your clinical data file:")
        #This function allows user to submit his clinical data 
        clinical_json_file=st.file_uploader("jg",accept_multiple_files=False,type="json",label_visibility="hidden")

    with col_c:
        #Getting demographic json file:
        st.subheader("Enter your demographic data file:")
        #This function allows user to submit his clinical data 
        demographic_json_file=st.file_uploader("",accept_multiple_files=False,type="json")

    st.write('#')
    st.write('#')

    if((clinical_json_file is not None) and (demographic_json_file is not None)):
        error_demographics=0
        error_clinical=0
        #Getting clinical data:
        clinical_data = json.load(clinical_json_file)
        try:
            problem_diagnosis_name,clinical_description,date_of_onset,date_clinically_recognised,last_date_of_work,end_of_shift_time,sickness,date_of_resolution=clinical_data_extractor(clinical_data)
        except:
            error_clinical=1
            st.error(": This is not the requested clinical data file",icon="❌")

        #Geting demographic data:
        demographic_data = json.load(demographic_json_file)
        try:
            street_name,street_number,postal_code,province,town,country,email,phone_number,country_code,name,surname,title,birthday,marital_status,status,national_insurance,clock_payroll=demographical_data_extractor(demographic_data)
        except:
            error_demographics=1
            st.error(": This is not the requested demographic data file",icon="❌")


        if(error_clinical==0 and error_demographics==0):
            st.write("here comes the big stuff")
            submitted_data = {
                "name": name,
                "email": email,
                # Add more fields here
            }
            if st.button("Generate PDF"):
                pdf_buffer = generate_pdf(submitted_data)
                st.download_button("Download PDF", pdf_buffer.getvalue(), "generated_pdf.pdf")
            

    elif ((clinical_json_file is not None) and (demographic_json_file is None)):
        st.warning(": Waiting for the demographic data",icon="⚠️")

    elif ((clinical_json_file is None) and (demographic_json_file is not None)):
        st.warning(": Waiting for the clinical data",icon="⚠️")

    else:
        st.warning(": Waiting for both: demographic & clinical data",icon="⚠️")


    return()


def clinical_data_extractor(json_object_clinical_data):

    problem_diagnosis_name=json_object_clinical_data["content"][0]["data"]["items"][0]["value"]["value"]
    clinical_description=json_object_clinical_data["content"][0]["data"]["items"][1]["value"]["value"]
    date_of_onset=json_object_clinical_data["content"][0]["data"]["items"][2]["value"]["value"]
    date_clinically_recognised=json_object_clinical_data["content"][0]["data"]["items"][3]["value"]["value"]
    last_date_of_work=json_object_clinical_data["content"][0]["data"]["items"][4]["value"]["value"]
    end_of_shift_time=json_object_clinical_data["content"][0]["data"]["items"][5]["value"]["value"]
    sickness=json_object_clinical_data["content"][0]["data"]["items"][6]["value"]["symbol"]["value"]
    date_of_resolution=json_object_clinical_data["content"][0]["data"]["items"][7]["value"]["value"]

    return(problem_diagnosis_name,clinical_description,date_of_onset,date_clinically_recognised,last_date_of_work,end_of_shift_time,sickness,date_of_resolution)


def demographical_data_extractor(json_object_demographic_data):

    street_name=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][0]["value"]["value"]
    street_number=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][1]["value"]["value"]
    postal_code=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][2]["value"]["value"]
    province=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][3]["value"]["value"]
    town=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][4]["value"]["value"]
    country=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][5]["value"]["value"]
    email=json_object_demographic_data["contacts"][0]["addresses"][1]["details"]["items"][0]["value"]["value"]
    phone_number=json_object_demographic_data["contacts"][0]["addresses"][2]["details"]["items"][0]["value"]["value"]
    country_code=json_object_demographic_data["contacts"][0]["addresses"][2]["details"]["items"][1]["value"]["value"]
    name=json_object_demographic_data["identities"][0]["details"]["items"][0]["value"]["value"]
    surname=json_object_demographic_data["identities"][0]["details"]["items"][1]["value"]["value"]
    title=json_object_demographic_data["identities"][0]["details"]["items"][2]["value"]["value"]
    birthday=json_object_demographic_data["identities"][0]["details"]["items"][3]["value"]["value"]
    marital_status=json_object_demographic_data["identities"][0]["details"]["items"][4]["value"]["value"]
    status=json_object_demographic_data["identities"][0]["details"]["items"][5]["value"]["value"]
    national_insurance=json_object_demographic_data["identities"][0]["details"]["items"][6]["value"]["value"]
    clock_payroll=json_object_demographic_data["identities"][0]["details"]["items"][7]["value"]["value"]

    country=json_object_demographic_data["contacts"][0]["addresses"][0]["details"]["items"][5]["value"]["value"]
    return(street_name,street_number,postal_code,province,town,country,email,phone_number,country_code,name,surname,title,birthday,marital_status,status,national_insurance,clock_payroll)