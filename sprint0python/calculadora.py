from operaciones import *

cont="s"
while cont=="s":

    print("Introduce un número")
    n1=int((input()))

    print("Introduce otro número")
    n2=int((input()))

    print("Que operacion desea realizar:[1-Suma/2-Resta/3-Multiplicacion/4-Division]")
    op= int (input())


    if op==1:
            print(suma(n1,n2))
    else:
        if op==2:
            print(resta(n1,n2))
        else:
            if op==3:
                    print(multiplicacion(n1,n2))
            else:     
                if n1!=0 and n2!=0:
                    print(division(n1,n2))
                else:
                    print("No se admite división entre 0")

    print("¿Desea continuar? [s/n]")
    cont=input()
