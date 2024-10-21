# Simple Chatbot

## Overview
This is a simple rule-based chatbot implemented in Python that uses regular expressions to respond to user inputs. The chatbot is designed to assist users by answering questions and engaging in casual conversation.

## Features
- Responds to greetings and general inquiries.
- Can tell jokes and share interesting facts.
- Provides information about its capabilities and purpose.
- User-friendly command-line interface.
- Supports basic conversation flow with predefined patterns.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-chatbot.git
   ```
Navigate to the project directory:
```
cd simple-chatbot
```
Run the chatbot:
```
python chatbot.py
```
Usage
Start the chatbot by running the Python script.
Type your messages in the console to interact with the chatbot.
Type "bye", "exit", "quit", or "see you later" to end the conversation.
Code Explanation
Pattern Matching: The chatbot uses regular expressions to match user inputs with predefined patterns and respond accordingly.
Response Logic: The chatbot_response function checks the user's input against the defined patterns and returns the appropriate response.
User Interaction: The main loop allows continuous interaction until the user decides to exit.
