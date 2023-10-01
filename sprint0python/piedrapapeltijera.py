numJug=0
victorias=0
derrotas=0
import random
manos=['piedra', 'papel', 'tijeras']
while numJug<5:
    print("Escoge [piedra/papel/tijeras] (Escribe la palbra entera tal como esta)")
    usuario=input()
    rival=random.choice(manos)
    if usuario=="piedra" and rival=="tijeras":
        print("Ganaste, "+usuario+" gana a "+rival)
        numJug= int((numJug+1))
        victorias= int (victorias+1)

    elif usuario=="piedra" and rival=="papel":
        print("Perdiste, "+rival+" gana a "+usuario) 
        numJug= int(numJug+1)
        derrotas= int (derrotas+1)

    elif usuario=="piedra" and rival=="piedra":
        print("Empate, la jugada no cuenta")


    elif usuario=="papel" and rival=="tijeras":
        print("Perdiste, "+rival+" gana a "+usuario)
        numJug= int(numJug+1)
        derrotas= int (derrotas+1)

    elif usuario=="papel" and rival=="papel":
        print("Empate, la jugada no cuenta")


    elif usuario=="papel" and rival=="piedra":
        print("Ganaste, "+usuario+" gana a "+rival)
        numJug= int(numJug+1)
        victorias= int (victorias+1)
    elif usuario=="tijeras" and rival=="tijeras":
        print("Empate, la jugada no cuenta")


    elif usuario=="tijeras" and rival=="papel":
        print("Ganaste, "+usuario+" gana a "+rival)
        numJug= int(numJug+1)
        victorias= int (victorias+1)
    elif usuario=="tijeras" and rival=="piedra":
        print("Perdiste, "+rival+" gana a "+usuario)
        numJug= int(numJug+1)
        derrotas= int (derrotas+1)
if victorias>derrotas:
    print("Felicidades!, has ganado tu resultado es de ",victorias," victorias y ",derrotas," derrotas")
else:
    print("Perdiste..., tu resultado es de ",victorias," victorias y ",derrotas," derrotas")






 



