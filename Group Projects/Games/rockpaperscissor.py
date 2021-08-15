def rock():
    import random


    def rockpaperscissor(c, u):
        if c == u:
            print("TIE!!!")
        elif (c == 'Rock' and u == 'Paper') or (c == 'Paper' and u == 'Scissor') or (c == 'Scissor' and u == 'Rock'):
            print("User Wins!!!")
        else:
            print("Computer Wins!!!")

        print("Computer:", c ,"User:", u)


    rps_list = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(rps_list)
    print("PRESS\n1.Rock\n2.Paper\n3.Scissor\n")
    user_input = int(input())
    user_choice = rps_list[user_input - 1]
    rockpaperscissor(computer_choice, user_choice)