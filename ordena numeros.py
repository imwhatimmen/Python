def ordena_numero():
    n=input("Dime un numero: ")
    n_cifras=0
    while n>0:
        n=n/10
        n_cifras=n_cifras+1
    print n_cifras
ordena_numero()
    
    
