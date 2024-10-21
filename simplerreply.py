import re

def chatbot_response(user_input):
    # Convert the input to lowercase for better matching
    user_input = user_input.lower()

    # Define patterns and responses
    patterns = {
        r'hello|hi|hey|greetings': "Hello! How can I assist you today?",
        r'what is your name|who are you': "I'm a simple chatbot. You can call me ChatBot!",
        r'how are you|how do you do|how is it going': "I'm just a computer program, but thanks for asking!",
        r'help|support|assist|can you help me': "Sure, I can help you! What do you need assistance with?",
        r'bye|exit|quit|see you later': "Goodbye! Have a great day!",
        r'what can you do|what are your capabilities|what is your function': "I can chat with you, answer questions, and provide information based on predefined rules.",
        r'what is your favorite color|what color do you like': "I don't have feelings, but I've heard blue is a popular choice!",
        r'tell me a joke|make me laugh|do you know any jokes': "Why did the scarecrow win an award? Because he was outstanding in his field!",
        r'who created you|who made you|who developed you': "I was created by someone who loves programming and natural language processing.",
        r'how is the weather|what is the weather like|is it raining|what\'s the forecast': "I don't have real-time data, but you can check a weather website for updates!",
        r'where are you from|what is your origin|where do you live': "I'm just a program running on your device, so I don't have a physical location.",
        r'what time is it|tell me the time|current time': "I'm not sure, but you can check your device's clock for the time.",
        r'can you speak another language|do you know other languages|what languages do you speak': "I can understand and respond in multiple languages, depending on the implementation.",
        r'favorite food|what do you like to eat|do you have a favorite meal': "I don't eat, but I hear pizza is a favorite for many!",
        r'tell me something interesting|do you have any facts|give me a fact': "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!",
        r'what is your purpose|why do you exist|what is the reason for your creation': "My purpose is to assist users like you by providing information and engaging in conversation.",
        r'can you play a game|let\'s play|do you want to play': "I can play simple text-based games! Just let me know what you'd like to play.",
    }

    # Check each pattern for a match
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Example of running the chatbot
if __name__ == "__main__":
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit', 'see you later']:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")
