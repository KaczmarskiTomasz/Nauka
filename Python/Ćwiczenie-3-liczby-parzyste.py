wynik = 0
i = 0
operacje = int(input( "Podaj liczbe operacji do wykonania: " ))

while (i < operacje):
    x = float(input( "Podaj liczbe do sumowania: " ))
    if (x % 2 == 0): 
        wynik += x
        i += 1
    else:
        print( "Podano liczbe nieparzysta lub zmiennoprzecinkowa, prosze podac liczbe parzysta calkowita." )
        continue

    print ( "Liczba wykonanych operacji", i, ".", "Aktualny wynik", wynik, "." )
print ( "Suma", operacje, "podanych liczb to", wynik, "." )
