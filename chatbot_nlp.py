import nltk
from nltk.tokenize import word_tokenize

# Download required resources once
nltk.download('punkt')

# Predefined responses based on keywords
responses = {
    "name": "My name is SimpleBot.",
    "how": "I'm functioning properly, thank you!",
    "you": "I was created by a beginner Python developer.",
    "can": "I can answer simple questions. Try asking me!",
    "exit": "Goodbye! Have a great day!"
}

def get_response(user_input):
    tokens = word_tokenize(user_input.lower())
    for word in tokens:
        if word in responses:
            return responses[word]
    return "I'm still learning. I didn't understand that."

def chatbot():
    print("Hello! I'm SimpleBot (NLP version). Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if 'exit' in user_input.lower():
            print("Bot:", responses["exit"])
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()