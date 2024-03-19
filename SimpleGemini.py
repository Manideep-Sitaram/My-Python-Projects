import google.generativeai as genai
import os
# from IPython.display import display
# from IPython.display import Markdown
# import textwrap

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name = "gemini-pro")

prompt = [
    "What is Mixture of Experts?",
]

response = model.generate_content(prompt)
print(response.text)

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
