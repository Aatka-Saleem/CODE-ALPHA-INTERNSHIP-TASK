import tkinter as tk
import random

def print_hangman(wrong):
    # ASCII art for Hangman stages
    hangman_art = [
        "+--------+\n         |\n         |\n         |\n     ========",
        "+--------+\nO        |\n         |\n         |\n     ========",
        "+--------+\nO        |\n|        |\n         |\n     ========",
        "+--------+\n O       |\n/|       |\n         |\n     ========",
        "+--------+\n O       |\n/|\      |\n         |\n     ========",
        "+--------+\n O       |\n/|\      |\n/        |\n     ========",
        "+--------+\n O       |\n/|\      |\n/ \      |\n     ========"
    ]
    # Ensure wrong stays within the valid index range of hangman_art
    if wrong < len(hangman_art):
        # Display the Hangman stage on the canvas
        canvas.delete("hangman")
        canvas.create_text(150, 100, text=hangman_art[wrong], tags="hangman", font=("Courier", 20,"bold"))
    else:
        # If wrong exceeds the range, display the last Hangman stage
        canvas.delete("hangman")
        canvas.create_text(160, 100, text=hangman_art[-1], tags="hangman", font=("Courier", 20, "bold"))

def print_word(guessed_letters, word):
    display_word = ""
    for char in word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    # Display the word on the canvas
    canvas.delete("word")
    canvas.create_text(160, 250, text=display_word, tags="word", font=("Courier", 20, "bold"))
    return display_word  # Return the display word

def guess_letter(word, guessed_letters, letter_entry, wrong_guesses_label, guess_button, result_label, start_button):
    global wrong_guesses
    guessed_letter = letter_entry.get().lower()  # Get the guessed letter
    letter_entry.delete(0, tk.END)  # Clear the entry field
    if guessed_letter and guessed_letter.isalpha() and wrong_guesses < 6:  # Check if a valid letter is guessed and maximum wrong guesses not reached
        if guessed_letter not in guessed_letters:  # Check if the letter has not been guessed before
            guessed_letters.add(guessed_letter)  # Add the guessed letter to the set
            if guessed_letter not in word:  # Check if the guessed letter is not in the word
                wrong_guesses += 1  # Increment wrong guesses count
                print_hangman(wrong_guesses)  # Print updated Hangman stage
                wrong_guesses_label.config(text=f"Wrong Guesses: {wrong_guesses}")  # Update wrong guesses label
            print_word(guessed_letters, word)  # Print updated word with guessed letters

            if "_" not in print_word(guessed_letters, word):  # Check if word has been fully guessed
                guess_button.config(state="disabled")  # Disable guess button
                letter_entry.config(state="disabled")  # Disable guess entry field
                win_emoji = "\U0001F389"
                result_label.config(text=f"Congratulations! You won the game!{win_emoji}")  # Display winning message
            elif wrong_guesses == 6:  # Check if maximum wrong guesses reached
                guess_button.config(state="disabled")  # Disable guess button
                letter_entry.config(state="disabled")  # Disable guess entry field
                lose_emoji = "\U0001F61E"
                result_label.config(text=f"You lose! The word was: {word}{lose_emoji}")  # Display losing message
        else:
            result_label.config(text="You already guessed that letter! ")  # Display message for repeated guess

        if wrong_guesses == 6 and "_" in print_word(guessed_letters, word):  # Check if maximum wrong guesses reached and word not fully guessed
            guess_button.config(state="disabled")  # Disable guess button
            letter_entry.config(state="disabled")  # Disable guess entry field
            lose_emoji = "\U0001F61E"
            result_label.config(text=f"You lose! The word was: {word}{lose_emoji}")  # Display losing message

def start_game(guess_button, letter_entry, wrong_guesses_label, result_label, start_button):
    global word, wrong_guesses, guessed_letters
    word = random.choice(wordDictionary)  # Choose a random word from the word dictionary
    wrong_guesses = 0  # Reset wrong guesses count
    guessed_letters = set()  # Clear the guessed letters set
    print_word(guessed_letters, word)  # Print the word with blanks
    print_hangman(wrong_guesses)  # Print initial Hangman stage
    wrong_guesses_label.config(text=f"Wrong Guesses: {wrong_guesses}")  # Reset wrong guesses label

    # Configure guess_button command directly
    guess_button.config(
        command=lambda: guess_letter(word, guessed_letters, letter_entry, wrong_guesses_label, guess_button,
                                     result_label, start_button)
    )

    guess_button.config(state="normal")  # Enable guess button
    letter_entry.config(state="normal")  # Enable guess entry field
    result_label.config(text="")  # Reset result label
    start_button.config(text="Start New Game", command=lambda: start_game(guess_button, letter_entry, wrong_guesses_label, result_label, start_button))

root = tk.Tk()
root.title("Hangman")
root.geometry("700x680")
root.maxsize(700, 680)
root.minsize(700, 680)
root.config(bg="#4B0082")

frame1 = tk.Frame(root, bg="#4B0082")
frame1.pack(pady=5)

frame2 = tk.Frame(root, bg="#4B0082")
frame2.pack(pady=9)

frame3 = tk.Frame(root, bg="#4B0082")
frame3.pack(pady=10)

frame4 = tk.Frame(root, bg="#4B0082")
frame4.pack(pady=5)

frame5 = tk.Frame(root, bg="#4B0082")
frame5.pack(pady=10)

hangman_label = tk.Label(frame1, text="HANGMAN GAME ",font=("Comic Sans MS", 30, "bold"), bg="#4B0082", fg="white" )
hangman_label.pack(pady=(0, 9))

canvas = tk.Canvas(frame2, width=300, height=300, bg="#4B0082" , borderwidth=10, relief="groove")
canvas.pack(side="top", padx=(0, 20), pady=(10, 0))

wrong_guesses_label = tk.Label(frame2, text="Incorrect Guesses: 0",font=("HoboStd" ,15 , "bold") , relief="flat",borderwidth=10, bg="#4B0082", fg="white")
wrong_guesses_label.pack(side="top", padx=(0,20), pady=(5, 0))

def clear_default_text(event):
    if letter_entry.get() == "Enter guess here":
        letter_entry.delete(0, tk.END)

letter_entry = tk.Entry(frame3, font=("HoboStd", 10, "bold"), relief="raised", borderwidth=6, bg="#4B0082", fg="white")
letter_entry.insert(0, "Enter guess here")  # Set default text
letter_entry.bind("<FocusIn>", clear_default_text)  # Bind function to clear default text
letter_entry.pack(side="left", padx=(0, 10), pady=(0, 8))

guess_button = tk.Button(frame3, text="Submit Guess" ,font=("HoboStd" ,10 , "bold") , relief="raised" ,borderwidth=6, bg="#4B0082", fg="white" )
guess_button.pack(side="right",pady=(0, 8))

start_button =tk.Button(frame5, text="Start Game",font=("HoboStd" ,15 , "bold") , relief="sunken", borderwidth=10, bg="#4B0082", fg="white",
                         command=lambda: start_game(guess_button, letter_entry, wrong_guesses_label, result_label, start_button))
start_button.pack(side="bottom", padx=10, pady=5)

result_label = tk.Label(frame4, text="Game Result:\U0001F600 ",font=("Segue UI Emoji", 24),bg="#4B0082", fg="white")
result_label.pack(side="left", padx=(0, 10), pady=(3, 0))

wordDictionary = ["sunflower", "house", "diamond", "memes", "yeet", "hello", "howdy", "like", "subscribe", "pizza",
                  "kite", "meat", "honey", "housefly", "shark", "happy", "smile", "spring", "sunshine", "unstoppable"]
word = ""
wrong_guesses = 0
guessed_letters = set()

root.mainloop()