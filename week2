# Week 2: Ask Gemini a question and log the answer.
# Runs in Google Colab. The API key is stored in Colab Secrets (never in this file).
import requests
import textwrap
from google.colab import userdata

api_key = userdata.get("GEMINI_API_KEY")
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
headers = {"x-goog-api-key": api_key, "Content-Type": "application/json"}

question = input("Your question: ")
payload = {"contents": [{"role": "user", "parts": [{"text": question}]}]}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    answer = data["candidates"][0]["content"]["parts"][0]["text"]
    print(textwrap.fill(answer, width=80))

    with open("qa_log.txt", "a") as f:
        f.write("Q: " + question + "\n")
        f.write("A: " + answer + "\n\n")
except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)
