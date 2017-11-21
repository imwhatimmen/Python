def funcion():
    a=input("Dame la a")
    b=input("Dame la b")
    c=input("Dame la c")
    formula1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
    formula2=(-b-(b**2-4*a*c)**(1/2))/(2*a)

    if (b**2-4*a*c)==0:
        print"Tiene dos soluciones", formula1,"y", formuula2
    if (b**2-4*a*c)>0:
        print"Tiene una solución", formula1,"y", formula2
    else:
        print"No tiene soluciones"
        
funcion()
