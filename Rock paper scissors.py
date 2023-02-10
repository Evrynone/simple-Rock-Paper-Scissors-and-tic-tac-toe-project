import random

options = ["1", "2", "3"]
c = 0
h = 0
print("Rock Paper Scissors.\n Options-\n 1- Rock\n 2- Paper\n 3- Scissors.")

while True:
    print(f"score-\n you- {h}\n bot- {c}")
    i1 = random.randint(0,3)
    i = int(i1)
    
    if c == 10:
        print("You lost, try again next time!")
        break
    elif h == 10:
        print("Congrats! You win.")
        break
    j1 = input()

    if j1 not in options:
        print("incorrect input. Exiting the game.")
        break
        
    j = int(j1)
    
    if i == 1:
        if j == 1:
            print("You chose Rock and so did your opponent! It is a draw.")
            continue
        elif j == 2:
            print("You chose Paper and your oppoenent chose Rock. You scored a point!")
            h +=1
            continue
        else:
            print("You chose Scissors and your opponent chose rock. Your opponent scored a point!")
            c +=1
            continue
    if i == 2:
        if j == 1:
            print("You chose Rock and your opponent chose paper! your opponent scores a point!.")
            c += 1
            continue
        elif j == 2:
            print("You chose Paper and so did your oppoenent. It is a draw!")
            continue
        else:
            print("You chose Scissors and your opponent chose Paper. You scored a point!")
            h +=1
            continue
    if i == 3:
        if j == 1:
            print("You chose Rock and your opponent chose Scissors! you scored a point!.")
            h += 1
            continue
        elif j == 2:
            print("You chose Paper and your opponent chose Scissors. Your opponent scores a point!")
            c += 1
            continue
        else:
            print("You chose Scissors and so did your opponent. It is a draw!")
            continue
    

    

