#2. Write a Python program to multiply all the items in a list.


"""
lista = [1,2,5,6,2,5,3,-2,2.2,-0.56]
wynik = 1

for num in lista:
    wynik *= num
    print("Aktualny",wynik)
print(wynik)

print(max(lista))
"""


#5. Write a Python program to count the number of strings from a given list of strings.
#The string length is 2 or more and the first and last characters are the same

lista = ['abc', 'xyz', 'aba', '1221', '0', '-aba-']
sol = 0 
for seq in lista:
    if( len(seq) >= 2 and seq[0] == seq[-1]):
        sol += 1
print(sol)
