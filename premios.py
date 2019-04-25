from random import randint
parti = ["pepito","juan","pablo","marcela","santiago"]
sorteo=1
while sorteo<4:
    x=len(parti)-1
    y=randint(0,x)
    z= parti[y]
    print("el ganador numero",sorteo,"es",z)
    parti.pop(y)
    sorteo=sorteo+1
