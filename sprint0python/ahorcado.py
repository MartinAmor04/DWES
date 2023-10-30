import random

seguir="s"

fallos=6
numE=0
partida = True
i=0
letrasFalladas=['Letras falladas: ']
letrasAdivinadas=['Letras adivinadas: ']

while seguir!="n":
    partida = True
    fallos=6
    facil = ["casa", "agua", "azul"]
    normal = ["garaje", "cabeza", "guardia"]
    dificil = ["curiosidad", "paracaidas", "coagulacion"]
    listaPalabraMost = []
    listaPalabraAdiv=[]
    palabraAdivinar=""
    print("Escoge dificultad f/n/d")
    dif=input()
    print("ESTADO DEL JUEGO")
    
    print(letrasFalladas)
    print(letrasAdivinadas)
    print("Fallos totales",numE)

    if dif=="f":
        palabraAdivinar=random.choice(facil)
        listaPalabraAdiv = list(palabraAdivinar)
    
        for item in listaPalabraAdiv:
            listaPalabraMost.append('_')
        while partida:
            print(' '.join(listaPalabraMost))
            print("Introduce letra")
            letra=input()
            if letra not in palabraAdivinar:
                print("Esta letra no se encuentra en la palabra")
                fallos=int (fallos-1)
                if letra not in letrasFalladas:
                    letrasFalladas.append(letra)
                print(letrasFalladas)
                print("Te quedan ",fallos," intentos")
                numE=int(numE+1)
            else:
                for i, letraAdv in enumerate(listaPalabraAdiv):
                    if letraAdv==letra:
                        listaPalabraMost[i]=letra
                        if letra not in letrasAdivinadas:
                            letrasAdivinadas.append(letra)
            
            if fallos <= 0:
                partida = False
                print("Has perdido, la palabra era ",palabraAdivinar)
            elif listaPalabraAdiv == listaPalabraMost:
                partida = False
                print("Has ganado, la palabra era ",palabraAdivinar)

    if dif=="n":
        palabraAdivinar=random.choice(normal)
        listaPalabraAdiv = list(palabraAdivinar)
    
        for item in listaPalabraAdiv:
            listaPalabraMost.append('_')
        while partida:
            print(' '.join(listaPalabraMost))
            print("Introduce letra")
            letra=input()
            if letra not in palabraAdivinar:
                print("Esta letra no se encuentra en la palabra")
                fallos=int (fallos-1)
                if letra not in letrasFalladas:
                    letrasFalladas.append(letra)
                print(letrasFalladas)
                print("Te quedan ",fallos," intentos")
                numE=int(numE+1)
            else:
                for i, letraAdv in enumerate(listaPalabraAdiv):
                    if letraAdv==letra:
                        listaPalabraMost[i]=letra
                        if letra not in letrasAdivinadas:
                            letrasAdivinadas.append(letra)
            
            if fallos <= 0:
                partida = False
                print("Has perdido, la palabra era ",palabraAdivinar)
            elif listaPalabraAdiv == listaPalabraMost:
                partida = False
                print("Has ganado, la palabra era ",palabraAdivinar)

                
    if dif=="d":
        palabraAdivinar=random.choice(dificil)
        listaPalabraAdiv = list(palabraAdivinar)
    
        for item in listaPalabraAdiv:
            listaPalabraMost.append('_')
        while partida:
            print(' '.join(listaPalabraMost))
            print("Introduce letra")
            letra=input()
            if letra not in palabraAdivinar:
                print("Esta letra no se encuentra en la palabra")
                fallos=int (fallos-1)
                if letra not in letrasFalladas:
                    letrasFalladas.append(letra)
                print(letrasFalladas)
                print("Te quedan ",fallos," intentos")
                numE=int(numE+1)
            else:
                for i, letraAdv in enumerate(listaPalabraAdiv):
                    if letraAdv==letra:
                        listaPalabraMost[i]=letra
                        if letra not in letrasAdivinadas:
                            letrasAdivinadas.append(letra)
            
            if fallos <= 0:
                partida = False
                print("Has perdido, la palabra era ",palabraAdivinar)
            elif listaPalabraAdiv == listaPalabraMost:
                partida = False
                print("Has ganado, la palabra era ",palabraAdivinar)

    
    print("Seguir jugando? s/n")
    seguir=input()
    if seguir=="n":
        exit
    
        
        

      
               
        
         


