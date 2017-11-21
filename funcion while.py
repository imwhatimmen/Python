def sumador_varias_cifras():
    suma=0
    n=input("Dime un numero")
    while n>0:
        suma=suma+n%10
        n=n/10
    print suma+n
sumador_varias_cifras()
   
