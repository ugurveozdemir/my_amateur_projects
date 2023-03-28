questions = {0:"Who founded the Republic of Turkey",
                 1:"When founded the Republic of Turkey",
                 2:"Who is the first prime minister of Turkey",
                 3:"Who is the last king of Ottoman Empire"}
answer_options = [["A)ATATURK", "B)FEVZI CAKMAK", "C)DAMAT FERIT", "D)II.ABDULHAMID"],
                      ["A)1919" ,"B)1921" ,"C)1922","D)1923"],
                      ["A)ATATURK", "B)ISMET INONU" ,"C)CELAL BAYAR", "D)KAZIM KARABEKIR"],
                      ["A)II.ABDULHAMID" ,"B)V.MEHMET REŞAT", "C)VAHDETTIN", "D)ATATURK"]
                      ]
correct_answers = ["A","D","B","C"]
your_answers = []
options = ["A","B","C","D"]
def the_game():

    for q in range(0,len(questions.keys())):
        print("#-------------------------------")
        print(questions[q])
        for choices in answer_options[q]:
            print(choices)
        collectAnswers()
    display_score()
    play_again()

def collectAnswers():
    answer = input("Please select an answer -->")
    answer = answer.upper()
    if answer not in options:
        print("Please enter one of the choices.")
        collectAnswers()
    else:
        your_answers.append(answer)

def display_score():
    global score
    score = 0
    for i in range(0,len(correct_answers)):
        if correct_answers[i] == your_answers[i]:
            print("Mr.{}, question {} is correct".format(name,i+1))
            score += 25
        else:
            print("Question {} is not correct".format(i+1))
    print("Your score is {}.".format(score))
    if score <50:
        print("Mr.{}, I have bad news. Your score is under 50, so you failed.".format(name))
    else:
        print("Congratulations {}, you passed.".format(name))
def play_again():
    yesNo= ["YES","NO"]
    again = input("Do you want yo play again(yes/no)-->").upper()
    if again not in yesNo:
        print("Please enter one of the proper choices.")
        play_again()
    else:
        if again == yesNo[0]:
            the_game()
        elif again == yesNo[1]:
            print("Quiting...")
            quit()


def firstStart():
    global name
    name = input("Enter your name to start the game -->")
    if len(name) < 3:
        print("Your name can not be less than 3 characters.")
        firstStart()
    else:
        the_game()
firstStart()

the_game()

