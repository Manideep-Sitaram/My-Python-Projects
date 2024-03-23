import google.generativeai as genai
import os
import requests
# from IPython.display import display
# from IPython.display import Markdown
# import textwrap

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name = "gemini-pro")


webPage = requests.get("https://www.ada.gov/resources/web-guidance/")
html_content = webPage.text

user_input = f"""Analyze the provided website's HTML code and identify the personas for which ADA test cases are required based on the website's content and structure. Generate comprehensive test cases only for the relevant personas.

For each applicable persona, output the test cases in the following format:

<Applicable Persona Heading>  

Test Case 1:
- Objective: [Brief description of the test objective]
- Preconditions: [Any prerequisites or setup required]  
- Steps: [Numbered steps to perform the test]
- Expected Result: [The expected outcome if the test passes]

Test Case 2:
...

Website HTML:
### {html_content} ###

Please ensure that the generated test cases cover all relevant accessibility scenarios for the identified personas based on the website's HTML structure and content. If a particular persona is not applicable or relevant based on the analysis, do not include test cases for that persona.
"""

prompt = [
    "You are a professional ADA (Americans with Disabilities Act) tester with 10 years of experience in accessibility testing for visual, auditory, motor, cognitive, and neurological impairments. You can write comprehensive ADA test cases by analyzing a website's HTML code and considering different personas with disabilities.",
    user_input
]

response = model.generate_content(prompt)
print(response.text)

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
