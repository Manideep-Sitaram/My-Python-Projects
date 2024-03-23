import google.generativeai as genai
import os
import requests
# from IPython.display import display
# from IPython.display import Markdown
# import textwrap

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name = "gemini-pro")


webPage = requests.get("https://w3schools.com/python/demopage.htm")
html_content = webPage.text

user_input = f"""Generate comprehensive ADA test cases for the following personas, based on the provided website's HTML code:

Persona 1: A user with visual impairment who relies on a screen reader.
Persona 2: A user with auditory impairment who requires captions and transcripts.
Persona 3: A user with motor impairment who uses voice commands and alternative input methods.
Persona 4: A user with cognitive impairment who has difficulty with complex navigation or processing large amounts of information.
Persona 5: A user with neurological impairment, such as seizure disorders, who is sensitive to flashing or rapidly changing content.
For each persona, output the test cases in the following format:

<Persona Heading>

Test Case 1:
- Objective: [Brief description of the test objective]
- Preconditions: [Any prerequisites or setup required]
- Steps: [Numbered steps to perform the test]
- Expected Result: [The expected outcome if the test passes]

Test Case 2:
...

Website HTML:
### {html_content} ###

Please analyze the provided HTML code and generate comprehensive test cases that cover various accessibility scenarios for each of the five personas, ensuring that the website is inclusive and accessible to users with different disabilities and impairments.

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
