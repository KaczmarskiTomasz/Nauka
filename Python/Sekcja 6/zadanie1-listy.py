#1. Write a Python program to sum all the items in a list.


lista = [1,2,5,6,2,5,3,-2,2.2,-0.56]


lenght = (len(lista))
i = 0
wynik = 0


while i < (lenght - 1):
    wynik += lista[-1]
    wynik = round(wynik, 2)
    num = lista.pop()
    i += 1
    print(f"Dodano {num}")
    print("Aktualny wynik: ", wynik,".")
    
print("Ostateczny wynik: ", wynik, ".")



"""
for num in lista:
    wynik += num
print(wynik)
"""
