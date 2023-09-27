
puntos=0
print("¿Qué parece oro y plata no es? Escoge:[a(Plátano)/b(Sandía)/c(Manzana)] ")
respuesta=input();

if respuesta=="a":
    print("Acertaste!!!")
    puntos+=10
else:
    print("Fallaste :(")
    puntos-=5

print("¿Que animal empieza a cuatro patas, luego dos y por ultimo seis? Escoge:[a(Elefante)/b(Humano)/c(Araña)] ")
respuesta=input();

if respuesta=="b":
    print("Acertaste!!!")
    puntos+=10
else:
    print("Fallaste :(")
    puntos-=5

print("¿Qué es aquello que al nombrarlo desaparece? Escoge:[a(Miedo)/b(Viento)/c(Silencio)] ")
respuesta=input();

if respuesta=="c":
    print("Acertaste!!!")
    puntos+=10
else:
    print("Fallaste :(")
    puntos-=5

print("Total de puntos: ",puntos)
