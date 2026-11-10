
import random
import string
from collections import Counter

best_score = 0


# NUMBER GUESSING GAME
def play_game():
    global best_score

    secret_number = random.randint(1, 100)

    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100.")

    attempts = 0
    max_attempts = 7
    score = 100
    guessed_correctly = False

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue

        attempts += 1

        if guess == secret_number:
            print("Correct! You guessed the number!")
            guessed_correctly = True
            break

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("Too low! Try again.")

        score -= 10

    if not guessed_correctly:
        print("Game over! The number was:", secret_number)

    print("Attempts used:", attempts)
    print("Final score:", score)

    if guessed_correctly and score > best_score:
        best_score = score

    print("Best score:", best_score)


# WORD COUNTER
def count_words(path):
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read().lower()

    except FileNotFoundError:
        print("File not found:", path)
        return None

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text.split()

    return Counter(words)


def show_word_count(path):
    counts = count_words(path)

    if counts is None:
        return

    if not counts:
        print("The file is empty.")
        return

    print("\n===== WORD COUNT RESULTS =====")
    print("Total words:", sum(counts.values()))
    print("Unique words:", len(counts))

    print("\nTop 10 most common words:")

    for word, count in counts.most_common(10):
        print(word, ":", count)


# MAIN MENU
while True:
    print("\n===== PYTHON PROJECT MENU =====")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        play_game()

    elif choice == "2":
        show_word_count("sample.txt")

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Select 1, 2, or 3.")
