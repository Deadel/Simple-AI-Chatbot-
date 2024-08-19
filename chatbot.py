import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
]

def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()
# TESTY 2
pairs.extend([
    [
        r"(.*) your favorite (.*)?",
        ["I don't have favorites, but I like all kinds of things!",]
    ],
    [
        r"(.*) help (.*)?",
        ["I'm here to assist you. What do you need help with?",]
    ],
])
# TESTY 3
pairs.append([
    r"tell me a joke",
    ["Why don't scientists trust atoms? Because they make up everything!", 
     "I would tell you a chemistry joke, but I know I wouldn't get a reaction.", 
     "Why do programmers prefer dark mode? Because the light attracts bugs!"]
])

if __name__ == "__main__":
    chatbot()

