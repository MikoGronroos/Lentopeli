import random

def pokerLite(moneyToGamble):
    pList = []
    cList = []

    for i in range(5):
        pList.append(random.randint(1,9))
        cList.append(random.randint(1, 9))

    print(f"Your hand is: {pList}")

    while True:
        reRoll = int(input("What card do you want to re-roll? (select from cards 1-5 one at a time). When you're ready select 6 as input.) "))
        #print("Also mind that every time you decide to re-roll your hand is one digit smaller (e.g. from 1-5 to 1-4) ")
        if reRoll == 6:
            break
        else:
            pList.remove(pList[reRoll-1])
            print(pList)
    while len(pList) < 5:
        pList.append(random.randint(1, 9))


    if sum(pList) > sum(cList):
        print(f"You won! Your total score was {sum(pList)} and the computer's was {sum(cList)}.")
    elif sum(pList) < sum(cList):
        print(f"You lost! Your total score was {sum(pList)} and the computer's was {sum(cList)}.")
    if sum(pList) == sum(cList):
        print(f"You tied with the computer! Your scores were {sum(pList)} .")
