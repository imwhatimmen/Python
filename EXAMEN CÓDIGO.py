def examen():
    salir=1
    x=10
    suma=0
    for cont in range(0,x+1,1):
        while salir==1:
            print cont
            salir=input "deseas salir (1/0): "
    print "se acaba"
examen()
