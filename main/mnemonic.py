from openai import OpenAI
from private import keykey
def getMn(prompt):


    YOUR_API_KEY = keykey

    messages = [
        {
            "role": "system",
            "content": (
                "You are a mnemonic machine and you need to "
                "create mnemonic devices to help memorize terms and their definition"
                "they will be given in the form: [term] [definition]"
            ),
        },
        {
            "role": "user",
            "content": (
                "the prompt is " + prompt + "give me an output in this format [mnemonic:, explanation: ]"
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