# Simple AI Chatbot (NLP-Based)

A beginner-friendly, NLP-powered chatbot built with Python using the `nltk` library. This chatbot uses keyword recognition to simulate basic conversations and is a great starting point for understanding Natural Language Processing and AI.

## Features

- Uses NLP to understand user input
- Responds to basic questions
- Keyword-based response system
- Gracefully exits when user types 'exit'
- Easy to expand with more responses

## Demo

```
You: What is your name?
Bot: My name is SimpleBot.

You: How are you?
Bot: I'm functioning properly, thank you!

You: Can you help me?
Bot: I can answer simple questions. Try asking me!

You: Exit
Bot: Goodbye! Have a great day!
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/simple-ai-chatbot.git
cd simple-ai-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download necessary NLTK data (run once):
```python
import nltk
nltk.download('punkt')
```

## Running the Chatbot

```bash
python chatbot_nlp.py
```

## Folder Structure

```
simple-ai-chatbot/
├── chatbot_nlp.py       # Main chatbot script
├── README.md            # Project documentation
└── requirements.txt     # Dependency file
```

## Future Ideas

- Add a GUI using Tkinter or a web version with Flask
- Replace keyword matching with a trained model (like from Hugging Face)
- Store conversation history in a text file

## License

This project is open-source and free to use for learning purposes.