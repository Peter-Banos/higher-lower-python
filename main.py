import random
from game_data import data
from art import logo, vs


def first_two_choices(data_list):
    """Returns a list with two initial unique elements (dictionaries)."""
    random.shuffle(data_list)
    first_two = [data_list.pop(), data_list.pop()]
    return first_two


def generate_new_choice(old_choice_1, old_choice_2):
    """Returns one unique item (dictionary)."""
    old_choices = [old_choice_1, old_choice_2]
    new_choice = random.choice(data)
    while new_choice in old_choices:
        new_choice = random.choice(data)
    return new_choice


def display_info(compare_a, compare_b):
    """Prints information about the two compared items."""
    print(f"Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}.")
    print(vs)
    print(f"Against B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}.")


def ask_guess():
    """Returns a user input 'a' or 'b' depending on user's guess."""
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    valid_answers = ["a", "b"]
    while answer not in valid_answers:
        print(f"Invalid input: {answer}! You have to write either 'A' or 'B'.")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return answer


def compare_followers(choice_a, choice_b):
    """Returns '0' if follower count is the same, 'a' if first item has more, and 'b' if second item has more."""
    if choice_a["follower_count"] == choice_b["follower_count"]:
        return 0
    elif choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"


def is_game_over(user_input, correct_answer):
    """Returns True if user guessed incorrectly."""
    if correct_answer != 0 and correct_answer != user_input:
        return True


def play_game():
    """Starts a game of Higher Lower."""
    print(logo)
    starting_choices = first_two_choices(data)
    element_a = starting_choices[0]
    element_b = starting_choices[1]

    game_over = False
    score = 0
    reps = 0

    while not game_over:
        reps += 1
        if reps > 1:
            element_c = element_b
            element_b = generate_new_choice(element_a, element_b)
            element_a = element_c

        display_info(element_a, element_b)

        correct = compare_followers(element_a, element_b)
        print(correct)
        guess = ask_guess()

        game_over = is_game_over(guess, correct)
        if not game_over:
            score += 1
            print("\n" * 20)
            print(logo)
            print(f"You're right! Current score: {score}")

    print("\n" * 20)
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

play_game()
