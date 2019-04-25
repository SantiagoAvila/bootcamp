###### crear un diccionario persona con claves nomre, edad, estatura e imprimir cada uno de los valores de las claves en un print diferente
###Luego cambiar el valor edad con un input e imprimir de nuevo
##LUEGO AGREGRA UN CLAVE HOBBIE PERO QUE SU VALOR SEA UNA LISTA
##primera parte
dic_individuo={
                "nombre":"juan",
                "edad":18,
                "estatura":1.85}

print(dic_individuo.get("nombre"))
print(dic_individuo.get("edad"))
print(dic_individuo.get("estatura"))

##segunda parte 
nuevo_valor=input("cual es la edad correcta?")
dic_individuo["edad"]=nuevo_valor
print("la edad correcta es",dic_individuo.get("edad"))

##tercera parte
pasatiempo=["jugar futbol","jugar basket","leer","andar en bici"]
dic_individuo["hobbies"]=pasatiempo
print(dic_individuo)