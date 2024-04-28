import clipboard
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Set up OpenAI API key

# Get content from clipboard
clipboard_content = clipboard.paste()

# Create a conversation with ChatGPT
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"Create anki flashcards with the following text using a format like question;answer;tags tags next line question;answer;tags tags etc...{clipboard_content}."}
]

response = client.chat.completions.create(model="gpt-4",
                                          messages=messages,
                                          temperature=0.7,
                                          max_tokens=2000)

# Correctly access the generated text
# Use .text instead of ['message']['content']
generated_flashcards = response.choices[0].message.content


# Save flashcards to a file
with open("flashcards.txt", "w") as f:
    f.write(generated_flashcards)

print("Flashcards saved to 'flashcards.txt'")
