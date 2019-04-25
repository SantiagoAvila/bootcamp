from random import randint
###realizamos un juego de adivinanza

#num = randint(1, 99)             #numeros aleatorios entre 1 y 99
num = randint(1, 500)
adivino = False
intentos = 7                            #Declaro cunatos intentos
while adivino == False and intentos > 0:    #Dos condicione
    apostala = int(input("Cual es tu apuesta?: "))
    if apostala == num:
        adivino = True
        print("Sos un Crack!")
    elif apostala < num:
        print("Es más!")
    elif apostala > num > 500: #para que no entre si pone mas de 500
        print("Es menos!")
    if apostala>500:            #siempre analiza esto
        print("Solo hasta 500")
        #adivino = True          #para que salga del ciclo
    intentos -= 1
    print("Tienes ", intentos, " intento(s): ")

                
print("Termino el juego")

