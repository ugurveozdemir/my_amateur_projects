#rock-paper-scissors game
import random
import time
print("""
-------------------------------------
Welcome to rock-paper-scissors game
-------------------------------------
""")

def waiting_animation():
    print("Loading",end="")
    time.sleep(1 / 3)
    print(".", end="")
    time.sleep(1/3)
    print(".",end="")
    time.sleep(1 / 3)
    print(".")

def playing_animation():
    print("Playing",end="")
    time.sleep(1 / 4)
    print(".", end="")
    time.sleep(1/4)
    print(".",end="")
    time.sleep(1 / 4)
    print(".")


def the_game():
    global your_hand
    computer_options = [" ","rock","paper","scissors"]

    try:
        your_hand = int(input("""
              CHOOSE AN AVAILABLE OPTION
              [1]ROCK
              [2]PAPER
              [3]SCISSORS
              """))
        # print(type(your_hand))
    except:
        the_game()
    if (your_hand > 3 or your_hand < 1):
        the_game()
    else:
        random_number = random.randint(1,3)
        computer = computer_options[random_number]
        if your_hand == random_number:
            playing_animation()
            print("It's draw! Try Again.","Computer was",computer)
            the_game()
        elif your_hand == 1 and random_number == 2:
            playing_animation()
            print("You lost looser. Paper wraps rock.","Computer was",computer)
        elif your_hand == 1 and random_number == 3:
            playing_animation()
            print("Congratulations king, you beated. Rock breaks scissors.","Computer was",computer)
        elif your_hand == 2 and random_number == 1:
            playing_animation()
            print("Congratulations king, you beated. Paper wraps rock.","Computer was",computer)
        elif your_hand == 2 and random_number == 3:
            playing_animation()
            print("You lost looser. Scissors cuts paper.","Computer was",computer)
        elif your_hand == 3 and random_number == 1:
            playing_animation()
            print("You lost looser. Rock breaks scissors.","Computer was",computer)
        elif your_hand == 3 and random_number == 2:
            playing_animation()
            print("Congratulations king, you beated. Scissors cuts paper.","Computer was",computer)
        # else:
        #     print(random_number)
        #     print(type(random_number))
        #     print("You are doing something wrong.")


start  = input("press 1 and enter to start game -->")
if start == "1":
    waiting_animation()
    the_game()
else:
    print("OK boss... It's quiting")
    time.sleep(3)




