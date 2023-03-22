from enum import IntEnum

Days_OfWeek = IntEnum('Days_OfWeek ', 'mon tue wen thu fri sat sun')

choice = int(input("""Enter the day of the week
1 Monday
2 Tuesday
3 Wednesday
4 Thrusday
5 Friday
6 Saturday
7 Sunday
Choice: 
"""))



if (choice == Days_OfWeek.mon):
    print('Mondej srondej')

elif (choice == Days_OfWeek.tue):
    print('Tuesday srusdej')

elif (choice == Days_OfWeek.wen):
    print('Wednesday densdej')

elif (choice == Days_OfWeek.thu):
    print('Thursday tjisdej')

elif (choice == Days_OfWeek.fri):
    print('Friday frajej')

elif (choice == Days_OfWeek.sat):
    print('Saturday srondej')

elif (choice == Days_OfWeek.sun):
    print('Sunday srondej')
