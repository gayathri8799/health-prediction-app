# health-prediction-app
Health Prediction Application using Python, Streamlit, SQLite and Gemini AI API
# Health Prediction Application

## Project Overview

This application was developed as part of the Junior AI/ML Developer technical assessment.

The system allows users to manage patient blood test records and generate AI-powered health predictions based on blood test values.

## Features

### CRUD Operations

* Create patient records
* View patient records
* Update patient records
* Delete patient records

### Data Validation

* Valid email validation
* Date of birth validation
* Numeric validation for blood test values

### AI Health Prediction

The application integrates with the Google Gemini AI API to generate health risk assessments using:

* Glucose
* Haemoglobin
* Cholesterol

The generated prediction is automatically stored in the Remarks field.

### Persistent Storage

SQLite database is used for storing patient records.

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### AI Integration

* Google Gemini API

## Database Fields

* Full Name
* Date of Birth
* Email Address
* Glucose
* Haemoglobin
* Cholesterol
* Remarks

## Installation

Clone the repository:

git clone https://github.com/yourusername/health-prediction-app.git

Navigate to the project:

cd health-prediction-app

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## Project Structure

health-prediction-app/
├── app.py
├── database.py
├── ai_service.py
├── requirements.txt
├── README.md
├── screenshots/
└── data/

## Future Improvements

* User authentication
* Advanced ML prediction models
* Cloud deployment
* Dashboard analytics

## Author

Gandhimathi Annamalai
Junior AI/ML Developer Assessment Submission
