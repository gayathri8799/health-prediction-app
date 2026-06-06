import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_health_prediction(
        glucose,
        haemoglobin,
        cholesterol):

    prompt = f"""
You are a healthcare assistant.

Patient Values:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Provide:

1. Possible health risk
2. Short explanation

Limit response to 2 sentences.
"""

    response = model.generate_content(prompt)

    return response.text
