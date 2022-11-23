# import dependencies
import random
import art
from game_data import data
import os


def get_data_points(list1):
    """ Picks a random number from a list """

    num_choice = random.choice(list1)

    return num_choice


def get_data(a, dbase):
    """ returns the data from a list corresponding to index 'a' """
    return dbase[a]


def compare(a, b):
    """ Compares data from two option and returns the stringing corresponding to the
    choice with the higher follower count. """
    print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
    print(art.vs)
    print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}')
    if a["follower_count"] > b["follower_count"]:
        return "a"
    elif b["follower_count"] > a["follower_count"]:
        return "b"


def is_correct(winning_option):
    """Prompts the user to pick the option they think has the higher follower count and
    returns 'True' if the same as the correct answer """
  
    user_choice = input("Who has more followers? Type 'A' or 'B':").lower()
    if user_choice == winning_option:
        return True


# initialize variables
data_full = [i for i in range(0, 50)]

score = 0
add_up = True
num_1 = get_data_points(data_full)

print(art.logo)

# Run until false
while add_up:  
    num_2 = get_data_points(data_full)
    while num_2 == num_1:
        num_2 = get_data_points(data_full)
    option_a = get_data(num_1, data)
    option_b = get_data(num_2, data)
  
    highest = compare(option_a, option_b)
    result = is_correct(highest)
    if result:
        score += 1
        num_1 = num_2
        os.system('cls')
        print(art.logo)
        print(f"You're right! Current score: {score}")
    else:
        os.system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        add_up = False
