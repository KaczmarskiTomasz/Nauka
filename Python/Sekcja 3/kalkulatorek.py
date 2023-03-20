from math import sqrt

wybor = input("wybierz operacje: - ; + ; * ; / ; ** ; % ; sqrt ; absolute: ")

if(wybor != 'sqrt' and wybor != 'absolute'):
    a = int(input("wybierz pierwsza liczbe: "))
    b = int(input("wybierz druga liczbe: "))

else:
    if(wybor == 'sqrt'):
        a = int(input("wybierz liczbe podpierwiastkowa: "))
        b = int(input("wybierz stopien pierwiastka: "))
    else:
        a = input("wybierz liczbe: ")
if (wybor == '-'):
    print (a - b)    
elif (wybor == '+'):
    print (a + b)
elif (wybor == '*'):
    print (a * b)
elif (wybor == '/'):
    if (b == 0):
        print ("Nie mozna dzielic przez zero")
    else:
        print (a / b)
elif (wybor == '**'):
    print (a ** b)
elif (wybor == '%'):
    print (a % b)
elif (wybor == 'sqrt'):
    if(a < 0 and (b % 2 == 0)):
        print("Nie można pierwiastkowac liczby ujemnej w parzystym stopniu")
    print (a ** (1/b))
elif (wybor == 'absolute'):
    print (abs(int(eval(a))))
