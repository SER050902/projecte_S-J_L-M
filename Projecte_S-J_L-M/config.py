import os

configuracion = {
    "DIR_INIT": '../Projecte_S-J_L-M/',
    "DIR_DST": '../Projecte_S-J_L-M/ggm_classificat',
    "MIDA_PETITA": 17,
    "MIDA_MITJANA": 20,
    "EXTENSION_FILTRADA" : ['pdf', 'txt', 'bin']
}

def obtener_configuracion():
    return configuracion


def veure_config():
    print(configuracion)

def Carregar_config():
    global configuracion,extension
    archivo = input('Introduce el nombre del archivo: ')
    try:
        with (open(archivo, 'r') as file):
            contenido = file.read()
            if archivo != extension:
                print('el pdf es extension filtrado')
                if archivo.endswith('.txt'):
                    print('Contenido del archivo', archivo, ':')
            else:
                print('No se puede abrir el archivo',archivo)
            print(contenido)
    except FileNotFoundError:
        print('El archivo', archivo, 'no existe.')






def guardar_config():
    global configuracion
    with open('config.txt', 'w') as f:
        f.write(str(configuracion))


def cambiar_parametros():
    print('LA INFORMACION DE configuración')
    veure_config()
    clave = input('Introduce la clave que quieres cambiar: ')
    if clave not in configuracion:
        print("La clave", clave, "no existe en la configuración.")
        return

    while True:
        print('El valor actual:', configuracion[clave])
        nuevo_valor = input('Introduce nuevo valor:')

    guardar_config()
    veure_config()


def mostrar_configuraciones():
    global configuracion
    print("Valors actuals de la configuració:")
    for clave, valor in configuracion.items():
        print(clave, "=", valor)




