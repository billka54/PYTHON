import re, sys, subprocess
# Biblioteca re --> para hacer uso de expresiones regulares
# Biblioteca sys --> Nos ayuda a obtener informacion del sistema
# Biblioteca subprocess --> Para ejecutar proecesos externos en el SO

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 " + sys.argv[0] + " <direccion-ip>\n")
    sys.exit(1)

def get_ttl (ip):
    proceso = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proceso.communicate()

    out = out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0] #Esta expresion regular nos ayuda a encontrar digitos entre 1 y tres carácteres y el [0] para que saque el primer elemento de la lista

    return ttl_value


def os (ttl):
    ttl = int(ttl)

    if ttl >=0 and ttl <=64:
        print ("El sistema operativo detectado es Linux")
    elif ttl >= 65 and ttl <= 128:
        print ("El sistema operativo detectado es Windows")
    elif ttl >= 129 and ttl <= 256:
        print ("El sistema operativo identificado es Solaris")
    else:
        print ("Error, sistema operativo no encontrado")

if __name__ == "__main__":

    ip = sys.argv[1]
    ttl = get_ttl(ip)
    nombreSO= os(ttl)

    print("La dirección IP introducida es: {}".format(ip))
    print ("El S.O es: {}".format(nombreSO))

