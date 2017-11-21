def contador():
    n=input("Dime un numero")
    m=input("Dime otro numero")
    if ((n%2 >0) and (m%2 >0)):
        print "Los dos son impares"
    if ((n%2==0) and (m%2==0)):
        print "Los dos son pares"
    if ((n%2==0) and (m%2 >0)):
        print "Uno es par y otro impar"
    if ((n%2 >0) and (m%2==0)):
        print "Uno es impar y otro es par"
contador()
