import streamlit as st
import pandas as pd
import re

from datetime import date

from database import *
from ai_service import *

create_table()

st.set_page_config(
    page_title="Health Prediction App",
    layout="wide"
)

st.title("🏥 Health Prediction Application")

menu = [
    "Create",
    "View",
    "Update",
    "Delete"
]

choice = st.sidebar.selectbox(
    "Menu",
    menu
)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# ---------------- CREATE ----------------

if choice == "Create":

    st.subheader("Add Patient")

    full_name = st.text_input("Full Name")

    dob = st.date_input(
        "Date of Birth",
        min_value=date(1950,1,1),
        max_value=date.today()
    )

    email = st.text_input(
        "Email Address"
    )

    glucose = st.text_input("Glucose")

    haemoglobin = st.text_input(
        "Haemoglobin"
    )

    cholesterol = st.text_input(
        "Cholesterol"
    )

    if st.button("Generate Prediction & Save"):

        try:

            if not re.match(
                EMAIL_REGEX,
                email
            ):
                st.error(
                    "Invalid email format"
                )

            elif dob > date.today():
                st.error(
                    "DOB cannot be future date"
                )

            else:

                glucose = float(glucose)
                haemoglobin = float(
                    haemoglobin
                )
                cholesterol = float(
                    cholesterol
                )

                remarks = (
                    generate_health_prediction(
                        glucose,
                        haemoglobin,
                        cholesterol
                    )
                )

                add_patient(
                    full_name,
                    str(dob),
                    email,
                    glucose,
                    haemoglobin,
                    cholesterol,
                    remarks
                )

                st.success(
                    "Patient Saved Successfully"
                )

                st.text_area(
                    "AI Remarks",
                    remarks,
                    height=150
                )

        except Exception as e:
            st.error(
                f"Error: {e}"
            )

# ---------------- VIEW ----------------

elif choice == "View":

    st.subheader("Patient Records")

    data = get_patients()

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Full Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ---------------- UPDATE ----------------

elif choice == "Update":

    st.subheader("Update Patient")

    data = get_patients()

    ids = [row[0] for row in data]

    if ids:

        selected_id = st.selectbox(
            "Select Patient ID",
            ids
        )

        patient = None

        for row in data:
            if row[0] == selected_id:
                patient = row
                break

        full_name = st.text_input(
            "Full Name",
            patient[1]
        )

        dob = st.text_input(
            "DOB",
            patient[2]
        )

        email = st.text_input(
            "Email",
            patient[3]
        )

        glucose = st.number_input(
            "Glucose",
            value=float(patient[4])
        )

        haemoglobin = st.number_input(
            "Haemoglobin",
            value=float(patient[5])
        )

        cholesterol = st.number_input(
            "Cholesterol",
            value=float(patient[6])
        )

        if st.button(
            "Update Record"
        ):

            remarks = (
                generate_health_prediction(
                    glucose,
                    haemoglobin,
                    cholesterol
                )
            )

            update_patient(
                selected_id,
                full_name,
                dob,
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success(
                "Updated Successfully"
            )

    else:
        st.info("No Records")

# ---------------- DELETE ----------------

elif choice == "Delete":

    st.subheader(
        "Delete Patient"
    )

    data = get_patients()

    ids = [row[0] for row in data]

    if ids:

        selected_id = st.selectbox(
            "Select Patient ID",
            ids
        )

        if st.button(
            "Delete Record"
        ):

            delete_patient(
                selected_id
            )

            st.success(
                "Deleted Successfully"
            )

    else:
        st.info(
            "No Records Found"
        )
