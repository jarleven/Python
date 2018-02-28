brett = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]

while True:
    
    for player in['X', 'O']:
 
        print("   ")
        print(brett)
        print("")
        print("")
    

        print("Spelar %s " % player)
    
        while True:
            position = input("    Velg rute : ")
            position = int(position)
            
            if (position < 9) and (brett[position] == ' '):
                brett[position] = player
                break
            
