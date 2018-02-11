# Test of Modulo division

for tal in range(1,11):
    
    test = 3
    heile = tal/test    # Divisjon
    rest = tal%test     # Modulo divisjon
    print("%2d delt på %d  er -- %d rest er %d  --  vi kan skrive det slik %2d = (%d * %d) + %d " % (tal, test, heile, rest,   tal, test, heile, rest))
