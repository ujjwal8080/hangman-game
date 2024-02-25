#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def choose_word():
    words = ["pathaan", "jawan", "don2", "raone", "zero", "dunki", "raees", "dilwale"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 10
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman! \n Guess SRK movie")

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Word: ",current_display)
        guess = input("Enter a letter: ")

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Correct guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts += 1
                guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

        if current_display == word_to_guess:
            print("Congratulations! You guessed the movie:", word_to_guess)
            break
        elif attempts == max_attempts:
            print("Sorry, you've run out of attempts. The movie was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()


# In[ ]:




