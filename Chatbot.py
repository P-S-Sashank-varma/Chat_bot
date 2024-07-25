import openai
import time

openai.api_key = "your-api-key"

def open_ai(human_input):
    try:
        response = openai.chat.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": human_input}
            ]
        )
        return response.choices[0].message["content"]
    except openai.error.RateLimitError as e:
        print("Rate limit exceeded. Retrying in 60 seconds...")
        time.sleep(60)
        return open_ai(human_input)  # Retry the request

if __name__ == "__main__":
    human_input = "Hello, how are you?"
    ai_response = open_ai(human_input)
    print(ai_response)
