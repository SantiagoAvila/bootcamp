from random import randint
parti = ["pepito","juan","pablo","marcela","santiago"]
def sorteos(cantidad_premios,lista):
    if cantidad_premios <= len(lista):
        sorteo=1
        while sorteo<cantidad_premios+1:
            x=len(lista)-1
            y=randint(0,x)
            z= lista[y]
            print("el ganador numero",sorteo,"es",z)
            lista.pop(y)
            sorteo=sorteo+1
    else:
        print("tu numero de premios supera al de participantes... dejate de joder")

sorteos(2,parti)