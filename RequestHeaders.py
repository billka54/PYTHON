import requests


def main(): #Definición de la función principal
    url = input("Introduce la URL: ")
    try:
        response = requests.get(url, timeout=5) #Intenta hacer petición a la web solicitada
        headers = response.headers #La respuesta obtenida se guarda en la variable headers
        for key, value in headers.items(): #Este bucle muestra todos los valores de la cabecera HTTP
            print(key, ":", value)
    except requests.exceptions.RequestException as e: # Cuando no se puede realizar una conexión con la URL solicitada
        print("Error al realizar la petición:", e)


if __name__ == "__main__":
    main()
