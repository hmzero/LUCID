import google.generativeai as genai
import os
import configparser

# load prameters from config file
config = configparser.ConfigParser()
config.read('config.cfg')
temp = float(config['gemini']['Temperature'])

# initialize Gemini 1.5 Pro
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")

# send a request to the model and return the text response
def generate(input):
    res = model.generate_content(
        input,
        generation_config = genai.GenerationConfig(
            temperature=temp,
        )
    )
    return res.text