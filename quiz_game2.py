import time
class Question:
    total_point = 0.00000000000001
    def __init__(self,question,choices,correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice
    @classmethod
    def check_answer(cls):
        for i in range(0,12):
            if your_guesses[i] == all_questions[i].correct_choice:
                Question.total_point += 100/len(all_questions)
    @classmethod
    def display_result(cls):
        if Question.total_point < 50:
            print(f"You got {Question.total_point}, so you failed from the exam.")
            print("Try again later")
        elif Question.total_point >= 50 and Question.total_point<85:
            print(f"Your point is {Question.total_point} It's enough to pass the exam.")
            print("But you can do better")
        else:
            print("********CONGRATULATIONS********")
            print(f"Your point is {Question.total_point}")
            print("It's is really amazing. You must be a hardworker.")

def waiting_animation():
    print("LOADING",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print()
def game():
    print(f"""
    Eeach questions is {100/len(all_questions)} points.
    The game is starting...
""")
    waiting_animation()
    global your_guesses
    your_guesses = []
    options = ["A","B","C","D"]
    for num in range(0,12):
        while True:
            print("#---------------------------------------------------#")
            print(all_questions[num].question)
            print(all_questions[num].choices)
            choice = input("Please select an answer -->")
            choice = choice.upper()
            if choice not in options:
                print("Please select one of the available ones")
                continue
            your_guesses.append(choice)
            break
    print("Now calculating your points")
    Question.check_answer()
    waiting_animation()
    Question.display_result()




def starting():
    choices = ["YES","NO"]
    start = input("Do you want to start game(yes/no)")
    start = start.upper()
    if start not in choices:
        print("You entered something wrong. Try again.")
        starting()
    elif start == "YES":
        game()
    elif start == "NO":
        print("OK. It's quiting.")
        quit()

q1 = Question("Türkiye'nin ilk başbakanı kidmir?","A)İsmet İnönü B)Mustafa Kemal Atatürk C)Fevzi Çakmak D)Celal Bayar","A")
q2 = Question("Türkiye'nin ilk cumhurbaşkanı kidmir?","A)İsmet İnönü B)Mustafa Kemal Atatürk C)Fevzi Çakmak D)Adnan Menderes","B")
q3 = Question("Osmanlı Devleti'nin iilk padişahı kimdir","A)Ertuğrul Gazi B)Osman Bey C)Orhan Bey D)Şeyh Edebali","B")
q4 = Question("Kösedağ Savaşı ne zaman olmuştur","A)1256 B)1298 C)1243 D)1286","C")
q5 = Question("Mustafa Kemal hangi görevle Samsun'a gönderilmiştir? ","A)10.Ordu Komutanlığı B)9.Kolordu komutanlığı C)9.Ordu Müfettişliği D)Encümen Ağası","C")
q6 = Question("Mustafa Kemal'in Ben inkılap ruhunu ondan aldım diye söz ettiği yazar kimdir?","A)Ziya Gökalp B)Hasan Ali Yücel C)Jean-Jacques Rousseau D)Tevfik Fikret","D")
q7 = Question("Atatürk'ün en çok sevdiği oyun nedir?","A)Zeybek B)Harmandalı C)Orta oyunu D)Karagöz ve Hacivat","B")
q8 = Question("Atatürk'ün En Sevdiği Yemek Nedir?","A)Kuru Fasülye ve pilav B)Ejder meyveli smoothie C)Suşi D)Barbunya","A")
q9 = Question("Atatürk'ün En Sevdiği Türkü Hangisidir?","A)Selanik B)Bülbülüm altın kafeste C)Havada bulut yok D)Cana rakini handan edersin","B")
q10 = Question("Atatürk'ün babası Ali Rıza Bey'in mesleği nedir?","A)Marangoz B)Gazeteci C)Asker D)Memur","D")
q11 = Question("Atatürk 'Ben Size Savaşmayı Değil, Ölmeyi Emrediyorum.' Sözünü Hangi Cephede Söylemiştir?","A)Filistin Cephesi B)Sakarya Meydan Muharebesi C)Çanakkale Cephesi D)Büyük Taarruz","C")
q12 = Question("Mustafa Kemal'in kendisinin kaleme aldığı eserinin konusu ne ile ilgilidir?","A)Savaş sanatları B)Astronomi C)Kimya D)Geometri","D")
all_questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
game()