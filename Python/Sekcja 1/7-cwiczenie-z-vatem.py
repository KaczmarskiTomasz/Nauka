
cenaNettoKawa = 15
cenaNettoHerbata = 5

VAT = 21
VATobliczeniowy = (1 + VAT * 0.01)

cenaBruttoKawa = cenaNettoKawa * VATobliczeniowy
cenaBruttoHerbata = cenaNettoHerbata * VATobliczeniowy

print ("cena kawy brutto :")
print(cenaBruttoKawa)

print ("cena herbaty brutto :")
print (cenaBruttoHerbata)
