def vocales_u():
    texto=raw_input("Dime un texto: ")
    lista1=list(texto)
    for cont in range (0,len(texto),1):
        if lista1[cont]=="a"or"e"or"i"or"o":
            lista1[cont]="u"
    final="".join(lista1)
vocales_u()
    
