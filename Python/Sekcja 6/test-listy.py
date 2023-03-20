
imiona = ["Arkadiusz", "Wiola","Antek"]
imie = "X"

while imie not in imiona:
    imie = input("Podaj swoje imie: ")
    if (imie in imiona):
        print("Masz dostęp.")
    else:
        print("Nie masz dostepu.")
