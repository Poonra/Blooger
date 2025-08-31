from openai import OpenAI
import os
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No API key found. Set OPENAI_API_KEY AND PAY THE BILL.")

client = OpenAI(api_key=api_key)

def generate_blog(topic):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful writing assistant."},
            {"role": "user", "content": f"Write a big-brain-simple detailed article about this: {topic}"}
        ],
        max_tokens=300,
        temperature=0.7,
    )

    retrieve_blog = response.choices[0].message.content

    return retrieve_blog


print(generate_blog('give me the best hero in combination to play rank in dota2'))
