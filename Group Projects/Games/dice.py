def dice():
    import random

    chance = 0
    print("Dice Rolling Game")
    print("Start Game")
    print("How many chances do you wish to play")
    n = int(input())
    while chance < n:
        input("\nRolling dice(press any keyword):")
        chance = chance + 1

        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(d1, d2)
        if d1 == d2:
            print("You win\n")
            break
        else:
            print("You lose")
        print("Number of chances left: ", n - chance)
    if n - chance == 0:
        print("--------------Game over---------------")
