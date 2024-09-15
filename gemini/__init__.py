import google.generativeai as genai
import os

# initialize Gemini 1.5 Pro
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

# send a request to the model and return the text response
def generate(input):
    res = model.generate_content(input)
    return res.text