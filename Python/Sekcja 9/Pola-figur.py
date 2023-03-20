from math import pi

def poleProstokata(a, b):
    return a * b

def poleKwadratu(a):
    return a ** 2

def poleTrojkata(a, h):
    return   (a * h) / 2

def poleTrapezu(a, b, h):
    return ((a + b) * h) / 2

def poleKola(r):
    return pi * r ** 2

wybor = 'Init'

while(wybor != 'end'):

    print('''Aby policzyć pole prostokąta wpisz: 1
Aby policzyć pole kwadratu wpisz: 2
Aby policzyć pole trójkąta wpisz: 3
Aby policzyć pole trapezu wpisz: 4
Aby policzyć pole koła wpisz: 5
Aby zakończyć liczenie wpisz: end''')

    wybor = input("Podaj operacje: ")

    if wybor == '1':
        bokA = int(input("Podaj długość 1. boku: "))
        bokB = int(input("Podaj długość 2. boku: "))
        print("Pole prostokąta wynosi", poleProstokata(bokA, bokB))

    if wybor == '2':
        bokA = int(input("Podaj długość boku: "))
        print("Pole kwadratu wynosi", poleKwadratu(bokA))
        
    if wybor == '3':
        podstawa = int(input("Podaj długość podstawy trójkąta: "))
        wysokosc = int(input("Podaj wysokość trójkąta: "))
        print("Pole trojkata wynosi", poleTrojkata(podstawa, wysokosc))
        
    if wybor == '4':
        podstawa1 = int(input("Podaj długość pierwszej podstawy trapezu: "))
        podstawa2 = int(input("Podaj długość drugiej podstawy trapezu: "))
        wysokosc = int(input("Podaj wysokość trapezu: "))
        print("Pole trapezu wynosi", poleTrapezu(podstawa1, podstawa2, wysokosc))
        
    if wybor == '5':
        promien = int(input("Podaj promień koła: "))
        print("Pole koła wynosi: ", poleKola(promien))
        
    if wybor == 'end':
        break
