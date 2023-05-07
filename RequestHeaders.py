import requests


def main(): #Definición de la función principal
    url = input("Introduce la URL: ")
    try:
        response = requests.get(url, timeout=5) #Intenta hacer petición a la web solicitada
        headers = response.headers #La respuesta obtenida se guarda en la variable headers

        csp_correcto = False
        xfo_correcta = False
        xss_correcta = False
        cache_correcta = False

        for key, value in headers.items(): #Este bucle muestra todos los valores de la cabecera HTTP
            print(key, ":", value)
            if key == "Content-Security-Policy" or key == "content-security-policy":
                csp_correcto = True
            elif key == "X-Frame-Options" or key == "x-frame-options":
                xfo_correcta = True
            elif key == "X-XSS-Protection" or key == "x-xss-protection":
                xss_correcta = True
            elif key == "Cache-Control" or key =="cache-control":
                cache_correcta = True

        
        if csp_correcto:
            print("La cabecera CSP esta implementada correctamente")
        else:
            print("La cabecera CSP NO esta implementada")
        if xfo_correcta:
            print("La cabecera X-Frame-Options esta implementada correctamente")
        else:
            print("La cabecera X-Frame-Options NO esta implementada")
        if xss_correcta:
            print("La cabecera X-XSS-Protection esta implementada correctamente")
        else:
            print("La cabecera X-XSS-Protection NO esta implementada")
        if cache_correcta:
            print("La cabecera Cache-Control esta implementada correctamente")
        else:
            print("La cabecera Cache-Control NO esta implementada")

        
    except requests.exceptions.RequestException as e: # Cuando no se puede realizar una conexión con la URL solicitada
        print("Error al realizar la petición:", e)


if __name__ == "__main__":
    main()
    
