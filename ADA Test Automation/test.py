from openai import OpenAI
import requests

OPENAI_API_KEY = ""
client = OpenAI(api_key=OPENAI_API_KEY)

def give_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional ADA Tester with 10 years of experience. You can write ADA test cases just by looking at the website's HTML code."},
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message)

webPage = requests.get("https://w3schools.com/python/demopage.htm")
html_content = webPage.text

prompt = f"""Generate ADA Test cases for different personas for this website. You have to output the result in this format:

Output:
<To Which Persona are we generating headings>
<Test cases in bullet points>

Website: ### {html_content} ### 

"""

give_response(prompt)
