def suma(num1,num2):
    respuesta=num1+num2
    return respuesta
def resta(num1,num2):
    respuesta=num1-num2
    return respuesta
def multiplicacion(num1,num2):
    respuesta=num1*num2
    return respuesta
def division(num1,num2):
    respuesta=num1/num2
    return respuesta
       
def menu_operacion():
    seguir="si"
    num1=input("Dime un numero ")
    num2=input("Dime otro numero ")
    while (seguir=="si"):
        print "�Que deseas hacer con los numeros?"
        print "1.Sumarlos"
        print "2.Restarlos"
        print "3.Multiplicarlos"
        print "4.Dividirlos"
        respuesta=input()
        if(respuesta==1):
            print num1,"+",num2,"=",suma(num1,num2)
        if(respuesta==2):
            print num1,"-",num2,"=",resta(num1,num2)
        if(respuesta==3):
            print num1,"*",num2,"=",multiplicacion(num1,num2)
        if(respuesta==4):
            print num1,"/",num2,"=",division(num1,num2)
                    
menu_operacion()
