import random

puntos=0

lista=["¿Qué parece oro y plata no es? Escoge:[a(Plátano)/b(Sandía)/c(Manzana)] ",
    "¿Que animal empieza a cuatro patas, luego dos y por ultimo seis? Escoge:[a(Humano)/b(Elefante)/c(Araña)] ",
    "¿Qué es aquello que al nombrarlo desaparece? Escoge:[a(Silencio)/b(Viento)/c(Miedo)] "]
    
adv1, adv2 = (random.sample(lista, 2)) 
print(adv1)
respuesta=input()
if respuesta=="a":
     print("Correcto!")
     puntos=int (puntos+10)
else:
        print("Fallaste!")
        puntos=int (puntos-5)

print(adv2)
respuesta=input()
if respuesta=="a":
        print("Correcto!")
        puntos=int (puntos+10)
else:
        print("Fallaste!")
        puntos=int (puntos-5)

print("Total de puntos: ",puntos)
