def vocales_a():
    palabra=raw_input("Dime algo plis: ")
    suma=0
    for cont in range(0,len(palabra),1):
        if palabra[cont]=="a":
            suma=suma+1
    print "En la palabra",palabra,"hay",suma,"letras a"
vocales_a()
    
