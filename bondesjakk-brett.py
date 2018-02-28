"""
 Bondesjakk Tic Tac Toe.
 Inspirert av denne https://inventwithpython.com/chapter10.html
"""

# Du kan lage ASCII ART Tekst på denne sida: 
#   http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
#
#  (ASCII er bokstavkodane, https://no.wikipedia.org/wiki/ASCII)

#
# Ein funksjon som skriv it logoen vår
def bondesjakkLogo():
    print("                                                                            ")
    print("                                                                            ")
    print("  __________                   .___                 __        __    __      ")
    print("  \______   \ ____   ____    __| _/____   ______   |__|____  |  | _|  | __  ")
    print("   |    |  _//  _ \ /    \  / __ |/ __ \ /  ___/   |  \__  \ |  |/ /  |/ /  ")
    print("   |    |   (  <_> )   |  \/ /_/ \  ___/ \___ \    |  |/ __ \|    <|    <   ")
    print("   |______  /\____/|___|  /\____ |\___  >____  >\__|  (____  /__|_ \__|_ \  ")
    print("          \/            \/      \/    \/     \/\______|    \/     \/    \/  ")
    print("                                                                            ")
    print("                                                                            ")



# Ei liste med spelardata, denne held X og O som spelarane legg inn/veljer
#  
#           0   1    2    3    4    5    6    7    8    9
spelarar = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]

ruter =    [0, "1", "2", "3", "4", "5", "6", "7", "8", "9"]


"""
    Rutene i brettet er definert som følgande

     |   |
   7 | 8 | 9
     |   |
  -----------
     |   |
   4 | 5 | 6
     |   |
  -----------
     |   |
   1 | 2 | 3
     |   |

"""

#
# Funksjon for utskrift av brettet over, vi sender inn ei liste med data for rutene
def brett(board):
    print(' ')
    print('   |   |')
    print(' %s | %s | %s' % (board[7],board[8],board[9]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' %s | %s | %s' % (board[4],board[5],board[6]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' %s | %s | %s' % (board[1],board[2],board[3]))
    print('   |   |')
    print(' ')
    

# Skriv ut logoen med ASCII art text
bondesjakkLogo()

# Skriv ut brettet med rutenummerte frå lista 'ruter'
brett(ruter)

# Skriv ut brettet med spelardata. Lista med spelardata er tom no !
brett(spelarar)

# Legg inn ein 'X' på den midterste ruta. Det er rute nr 5
spelarar[5] = 'X'
# Skriv ut brettet ein gong til
brett(spelarar)

# Lag litt luft med to blanke linjer

print("")
print("")

# Sjå kva som ligg i spelardata lista no
print(spelarar)

# Lag litt luft, vi skriv ut to blanke linjer
print("")
print("")
