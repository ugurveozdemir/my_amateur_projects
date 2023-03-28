import time
import random



def play_loto():
    global choices
    global c_guess
    choice_options = [0,1,2,3,5,6,7,8,9]
    choices = []
    for i in choice_options:
        print(i,end=", ")
    print()
    print("Those are numbers which will be mixed up. Please select three of those numbers")
    select_number()
    choices.append(num1)
    choices.append(num2)
    choices.append(num3)
    print("OK. You selected your numbers.")
    print("""
    ---------LOTO IS STARTING------------
    """)
    waiting_animation()
    c_guess = [random.randint(0,9),random.randint(0,9),random.randint(0,9)]
    value = 1
    print("<<<<<<< COMPUTER CHOICES >>>>>>>>>")
    for i in c_guess:
        print(f"Number {value} is ({i})",end=" #--# ")
        value += 1
    value = 1
    print()
    print("<<<<<<< YOUR CHOICES >>>>>>>>>")
    for i in choices:
        print(f"Number {value} is ({i})",end=" #--# ")
        value+=1
    print()
    calculate_gain()
    play_again()


def select_number():
    global num1
    global num2
    global num3
    while True:
        num1 = input("First --> ")
        try:
            num1 = int(num1)
        except ValueError:
            print("You entered something wrong. Please select again")
            continue
        if num1 > 9 or num1 < 0:
            print("You entered an invalid number. Try again.")
            continue
        break

    while True:
        num2 = input("Second --> ")
        try:
            num2 = int(num2)
        except ValueError:
            print("You entered something wrong. Please select again")
            continue
        if num2 > 9 or num2 < 0:
            print("You entered an invalid number. Try again.")
            continue
        break

    while True:
        num3 = input("Third --> ")
        try:
            num3 = int(num3)
        except ValueError:
            print("You entered something wrong. Please select again")
            continue
        if num3 > 9 or num3 < 0:
            print("You entered an invalid number. Try again.")
            continue
        break



def calculate_gain():
    constant_coefficent = 1.5
    coefficent = 0
    if choices[0]==c_guess[0]:
        print("You guessed first line and number correctly.")
        choices.remove(choices[0])
        coefficent += 2
    elif choices[1]==c_guess[1]:
        print("You guessed second line and number correctly.")
        choices.remove(choices[1])
        coefficent += 2
    elif choices[2]==c_guess[2]:
        print("You guessed third line and number correctly.")
        choices.remove(choices[2])
        coefficent += 2
    correct_guesses = list(set(choices)&set(c_guess))
    if correct_guesses =="":
        print("Bad game. You could not any number")

    else:
        coefficent += len(correct_guesses) * constant_coefficent
        total_gain = coefficent * money
        print(f"Your coefficent is {coefficent}. Your money going to be multiply with that coefficent.")
        print(f"You bet is {money} dollar. Your gain is {total_gain}")





def play_again():
    start_choices = ["YES", "NO"]
    start = input("Do you want to play game again(yes/no) -->")
    start = start.upper()
    if start not in start_choices:
        print("Please write down one of the present options.")
        play_again()
    elif start == "NO":
        print("OK. It's quiting...")
        quit()
    print("It's starting...")
    waiting_animation()
    place_bet()
    play_loto()
def waiting_animation():
    print("Loading",end="")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
def start_game():
    start_choices = ["YES", "NO"]
    start = input("Do you want to play game(yes/no) -->")
    try:
        start = start.upper()
    except:
        print("Please enter something proper!!")

    if start not in start_choices:
        print("Please write down one of the present options.")
        start_game()
    elif start == "NO":
        print("OK. It's quiting")
        quit()
    print("It's starting")
    waiting_animation()
    place_bet()
    play_loto()
def place_bet():
    global money
    money = input("Please place a bet -->")
    try:
        money = int(money)
    except:
        print("Please enter a dollar number")
        place_bet()
print("""
Welcome to loto game.
Here is the best loto to make money. 
You need luck but you have already,
because You're playing //ugurLOTO// now!!!
""")

print("""You are going to get 1.5 times money for each right guess. 
If you also guess the line of number, you are going to get 2 times money. """)

start_game()

