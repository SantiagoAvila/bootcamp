## archivo de aprender usar request
import requests
from pprint import pprint
def datos_peli(Nombre_peli):
    API_KEY= ""
    URL= "http://www.omdbapi.com/?apikey="
    titulo=Nombre_peli
    busqueda= URL + API_KEY + "&t=" + titulo
    respuesta= requests.get(busqueda)
    dic_peli= respuesta.json()
    pprint(dic_peli)
    pprint(dic_peli["Actors"])
 
datos_peli("Blade Runner")



