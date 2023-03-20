
dictionary = {'1': 'Tomasz','2': 'Jan','3': 'Maciej'}
status = 1
while status == 1: 

    operation = input("To add new key type: add, to find a key type: search, to delete a key type: delete." "\n"\
                      "Operation: ")

    if(operation == 'add'):
        key = input("key: ")
        value = input("value: ")
        dictionary[key] = value
        
    elif(operation == 'search'):
        wantedKey = input("key: ")
        print(dictionary[wantedKey],":", wantedKey)

    elif(operation == 'delete'):
        dictionary.pop(input("key: "))
    else:
        print("You typed bad operation name. Try again.")
        continue
    status = int(input("If u want to make another operation press: 1, if u want to end press: 0." "\n"\
                   "Operation: "))

 
