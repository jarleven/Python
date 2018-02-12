# Ei liste med spelardata, denne held X og O som spelarane legg inn/veljer
#  
#           0   1    2    3    4    5    6    7    8    9
spelarar = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]

#
# Funksjon for utskrift av brettet over, vi sender inn ei liste med data for rutene
def brett(board):
    print(' ')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print(' ')
    

#
# Ein funksjon som sjekkaer om det er tre symbol på rad
# Vi sender inn lista med spelardata og kva for eit symbol 'O' eller 'X' vi skal sjekke med
def trepaarad(liste):

    print("------------- Sjekk om vi har ein vinnar ---------------")   
    print("")
    
    """
     Ei liste med to dimmensjonar. Vi legg inn kombinasjonane
     med tre på rad som gjer ein vinnar. Totalt 8 muligheitar.
    """
    kombinasjonar = [
                     [1,2,3],  # Horisontalt
                     [4,5,6],
                     [7,8,9],
                     [1,4,7],  # Vertikalt
                     [2,5,8],
                     [3,6,9],
                     [1,5,9],  # Diagonalt
                     [3,5,7]
                    ]
    
    
    # Vi testar om tre ruter på rad er lik test variabelen
    
    
    for symbol in['X', 'O']:

        # Vi går gjennom alle 8 tre på rad kombinasjonane
        for loop in range(0,8):
        
            # Vi hentar ut eit sett med tre ruter på rad
            a = kombinasjonar[loop][0]      # [Element nedover][Element bortover]
            b = kombinasjonar[loop][1]
            c = kombinasjonar[loop][2]
        
            
            print("  Sjekkar om rutene [ %d %d %d ] er like med %c" % (a,b,c, symbol))
        
            # Vi hentar ut kva som ligg på dei tre rutene
            A = liste[a]
            B = liste[b]
            C = liste[c]
           
            print("  ----------------- [ %c %c %c ]" % (A,B,C))
            
        
        
            # Vi samanliknar og sjekkar om alle tre rutene på rad er lik test variabelen vår
            #    Det som står under er:
            #     Hvis 'A' og 'B' og 'C' er lik 'symbol' så har vi ein vinnar.
            #
            if (symbol == A and symbol == B and symbol == C ):
                print("  ----------------- 3 på rad") 

                
            # Legg inn litt luft mellom kvar runde, litt lettare å lese kva vi har då.
            print("")
            


# Vi kan teste at funksjonen vår fungerar med koden under.


# Vi kan sjekke om det er tre på rad med denne funksjonen.
trepaarad(spelarar)


# Du kan legg inn 'O' og 'X' slik
spelarar[1] = "O"
spelarar[2] = "O"
spelarar[3] = "O"

# Så sjekkar vi eing gong til etter at vi har lagt inn data i rutene
trepaarad(spelarar)
