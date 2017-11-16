def letras():
    palabra=raw_input("Dime una palabra: ")
    sumaa=0
    sumae=0
    sumai=0
    sumao=0
    sumau=0
    for cont in range(0,len(palabra),1):
        if palabra[cont]=="a":
            sumaa=sumaa+1
        if palabra[cont]=="e":
            sumae=sumae+1
        if palabra[cont]=="i":
            sumai=sumai+1
        if palabra[cont]=="o":
            sumao=sumao+1
        if palabra[cont]=="u":
            sumau=sumau+1
    print "En la palabra",palabra,"hay",sumaa,"letras a"
    print "En la palabra",palabra,"hay",sumae,"letras e"
    print "En la palabra",palabra,"hay",sumai,"letras i"
    print "En la palabra",palabra,"hay",sumao,"letras o"
    print "En la palabra",palabra,"hay",sumau,"letras u"
letras()
