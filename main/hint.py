from openai import OpenAI
from private import keykey
def getHint(prompt):


    YOUR_API_KEY = keykey

    messages = [
        {
            "role": "system",
            "content": (
                "You are a hint machine and you need to "
                "create hints for someone who has a term and needs to find the definition"
                
                "you must limit your response to a maximum of 200 characters"
                "they will be given in the form: [term] [definition]"
                "you cannot put the term or definition in your response"
            ),
        },
        {
            "role": "user",
            "content": (
                "the prompt is " + prompt + "give me a single output in this format [hint: ]."
            ),
        },
    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    # chat completion without streaming
    response = client.chat.completions.create(
        model="mistral-7b-instruct",
        messages=messages,
    )

    # Extract and print the output from the chatbot
    for choice in response.choices:
        if choice.message.role == 'assistant':
            return(choice.message.content)
        
if __name__ == "__main__":
    print(getHint("[woodland mansion] [hosuse in dark oak forrest biome]"))