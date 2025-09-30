import random

print("Welcome to Roulette! Choose a number between 1-12.")
print("If you bet on an even number, you will win even if the winning number is another even number")
print("What are you betting on?")

def roulette():
    odd = [1, 3, 5, 7, 9, 11]
    even = [2, 4, 6, 8, 10, 12]

    while True:
        result = random.randint(1, 12)
        print(result)
        answer = int(input("What are you betting on? (1-12): "))

        if answer == result:
            print("jee arvasit numeron oikein")
        else:
            if answer in odd and result in odd:
                print("Jee arvasit ryhmän oikein (odd)")
            elif answer in even and result in even:
                print("Jee arvasit ryhmän oikein (even)")
            else:
                print("Hävisit betin")

        jatkaa = input("Haluatko jatkaa? (y/n) ")

        if jatkaa == "n":
            break
