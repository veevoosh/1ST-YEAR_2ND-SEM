import time
import random

def calculate_words_per_minute(start_time, end_time, typed_text):
    words_typed = len(typed_text.split())
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60.0
    words_per_minute = words_typed / minutes
    return words_per_minute

def typing_tutor():
    print("Welcome to the Typing Tutor Program!")
    print("Type the following text as fast as you can. \n"
          "Press Enter when finished.")
    print()

    text_to_type = ["We're not holding a funeral chat, BECAUSE SHE'S NOT DEAD!",
                 "Taako... Are you here for business, or for pleasure?",
                 "What do you really want, Jay? Just say it so I can fight for it.",
                 "You showed me dreams can be worth fighting for, more than anything.",
                 "But I like kids. I could never have them, since the idea of sex is no idea at all."]

    selected_item = random.choice(text_to_type)

    print("Text to type:")
    print(selected_item)
    input("Press Enter to start...")
    print()

    start_time = time.time()
    typed_text = input("Type the text here: ")
    end_time = time.time()

    words_per_minute = calculate_words_per_minute(start_time, end_time, typed_text)

    print("Words per minute:", round(words_per_minute, 2))

    correct_chars = sum(1 for char1, char2 in zip(selected_item, typed_text) if char1 == char2)
    accuracy = (correct_chars / len(selected_item)) * 100
    print("Accuracy:", round(accuracy, 2), "%")

typing_tutor()
