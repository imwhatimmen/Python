def numeros():
    numero=input("Dime un numero ")
    for cont in range(numero-3,numero,1):
            print "Los anteriores son ",cont
    for cont in range(numero+1,numero+4,1):
            print "Los siguientes son ",cont
numeros()
