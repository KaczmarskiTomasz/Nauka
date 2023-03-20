from random import randint
wantedNumber = randint(0,100)
givenNumber = float('inf')

while wantedNumber != givenNumber :

    givenNumber = int(input("Podaj liczbe: "))

    if (givenNumber < wantedNumber):
        print("Podana liczba jest mniejsza od szukanej.")
    elif (givenNumber > wantedNumber):
        print("Podana liczba jest większa od szukanej.")

print("Zgadłeś")

