from nltk.chat.util import Chat, reflections
from tkinter import *


# Define new pairs with modified variable names and improved implementation
conversation_pairs = [
    [r"hi|hey|hello", ["Hello! How can I assist you today?", "Hey there!", "Hi! How can I help you?"]],
    [r"What can you do?", ["I can help answer your questions, provide information, or just have a chat."
                           " What do you need?"]],
    [r"What's the weather like today?", ["Let me check that for you. Where are you located?"]],
    [r"I'm in karachi.", ["Currently, it's hot day you can check on weathers app."]],
    [r"Tell me a joke!", ["Sure! Why don't scientists trust atoms? Because they make up everything!"]],
    [r"c", ["You're welcome! Feel free to ask if you need anything else."]],
    [r"Goodbye!", ["Goodbye! Have a great day!"]],
    [r"How are you?", ["I'm just a computer program, but I'm here to help you!"]],
    [r"Can you recommend a movie?", ["Sure! What genre are you interested in?"]],
    [r"I like comedy movies.", ["How about watching 'The Hangover'? It's a classic comedy!"]],
    [r"What's your favorite color?", ["I don't have a favorite color, but I like the concept of colors!"]],
    [r"Do you believe in aliens?", ["I don't have beliefs, but the possibility of extraterrestrial life is fascinating!"]],
    [r"What's the capital of France?", ["The capital of France is Paris."]],
    [r"How do I make pancakes?", ["To make pancakes, you'll need flour, eggs, milk, and a hot pan!"]],
    [r"Can you help me with a math problem?", ["Of course! What's the problem?"]],
    [r"What's the square root of 144?", ["The square root of 144 is 12."]],
    [r"Tell me a fun fact!", ["Did you know that honey never spoils? Archaeologists have found pots of honey in "
                              "ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"]],
    [r"How do I say 'hello' in Spanish?", ["You can say 'hello' in Spanish as 'Hola'!"]],
    [r"What's the meaning of life?", ["That's a profound question! The meaning of life is subjective and varies"
                                      " from person to person."]],
    [r"What's the tallest mountain on Earth?", ["Mount Everest is the tallest mountain on Earth,"
                                                " measuring 8,848 meters (29,029 feet) above sea level."]],
    [r"Can you tell me about yourself?", ["I'm just a chatbot programmed to assist you with your inquiries!"]],
    [r"What's the time  right now?", ["you can check on your phone."]],
    [r"I'm feeling lonely.", ["I'm here for you! Feel free to chat with me anytime you want."]],
    [r"What's your favorite book?", ["I don't have preferences, but I can recommend some popular books "
                                     "if you're interested!"]],
    [r"How do I change my password?", ["To change your password, you typically need to go to your account settings"
                                       " and look for the option to change password."]],
]

# Define a  class for the chatbot application
class ChatBotApp:

    def __init__(self, pairs):
        self.chatbot = Chat(pairs, reflections)

        self.window = Tk()
        self.window.title("CHATBOT")
        self.window.geometry("580x660")
        self.window.maxsize(600, 660)
        self.window.minsize(300, 300)
        self.window.config(bg='#2F4F4F')

        self.label_frame = Frame(self.window, bg="#5D478B")
        self.label_frame.pack(fill=X)
        chatbot_png = "\U0001F916"
        self.bot_label = Label(self.label_frame, text=f"CHATTER BOT{chatbot_png}", height=2, relief="raised",borderwidth=8,font=("Comic Sans MS", 30, "bold"), bg="#5D478B", fg="#DCDCDC")
        self.bot_label.pack(fill=X)

        self.display_frame = Frame(self.window)
        self.display_frame.pack(expand=True, fill=BOTH)

        self.chat_history = Text(self.display_frame,relief="raised",borderwidth=8 ,wrap="word", bg="#5D478B", fg="#FFFFFF", font=("roboto", 14, "bold"))
        self.chat_history.pack(expand=True, fill=BOTH)

        # Create a scrollbar and attach it to the chat history text widget
        self.scrollbar = Scrollbar(self.chat_history, orient=VERTICAL, command=self.chat_history.yview ,bg="#5D478B")
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.chat_history.config(yscrollcommand=self.scrollbar.set)
        self.chat_history.config(state=DISABLED)

        self.entry = Entry(self.window, bg="#DCDCDC", fg="black", font=("roboto", 14, "bold"))
        self.entry.pack(side=LEFT, expand=True, fill=X, anchor=SW)
        self.entry.bind("<Return>", self.send)

        self.submit_button = Button(self.window, text="Send", command=self.send ,bg="#5D478B", fg="white",relief="groove")
        self.submit_button.pack(side=RIGHT)

        self.window.mainloop()

    # Method to handle sending messages
    def send(self, event=None):
        user_input = self.entry.get()
        response = self.chatbot.respond(user_input)

        if not response:  # If the bot's response is empty
            response = "I'm in learning stage.keep in touch to see more features on me in future"

        self.chat_history.config(state=NORMAL)
        self.chat_history.insert(END, "You: " + user_input + "\n")
        self.chat_history.insert(END, "Bot: " + response + "\n\n")
        self.chat_history.config(state=DISABLED)

    # Scroll to the end of the chat history
        self.chat_history.see(END)
        self.entry.delete(0, END)


# Create an instance of the ChatBotApp class with the defined conversation pairs

chat_app = ChatBotApp(conversation_pairs)