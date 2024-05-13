import os
import sys

configuracion = {
    'DIR_INIT': '../Projecte_S-J_L-M/sergio_init',
    'DIR_DST': '../Projecte_S-J_L-M/sergio',
    'MIDA_PETITA': 5120,
    'MIDA_MITJANA': 12288,
    'EXTENSION_FILTRADA': ['pdf', 'exe', 'bin'],
    'DIR_QUARANTENA': '../Projecte_S-J_L-M/quarentena',
    'ZIP_FILE': 'zip_file'
}

def veure_config():
    with open('config.cfg', 'r') as f:
        config_file = f.read()
        print(config_file)

extension_abrir = ["cfg"]

def Carregar_config():
    global extension
    config = input('Introduce el nombre del archivo: ')
    try:
        with (open(config, 'r') as file):
            contenido = file.read()
            if config.split(".")[1] not in extension_abrir:
                print(f'No se puede abrir el archivo {config} (debería ser un archivo de configuración "cfg")')
            elif config.split(".")[1] in extension_abrir:
                print('Contenido del archivo', config, ':')
                print(contenido)

    except FileNotFoundError:
        print('El archivo', archivo, 'no existe.')



def cambiar_parametros():
    global configuracion
    print(configuracion)
    clave = input('Introduce la clave que quieres cambiar: ')
    if clave not in configuracion:
        print("La clave", clave, "no existe en la configuración.")
        return

    if clave == "DIR_INIT" or clave == "DIR_DST" or clave == "DIR_QUARANTENA":
        print('El valor actual:', configuracion[clave])
        nuevo_valor_ruta = input('Introduce el nuevo valor: ../Projecte_S-J_L-M/')
        nuevo_valor = "../Projecte_S-J_L-M/" + nuevo_valor_ruta
        configuracion[clave] = nuevo_valor
    if clave == "MIDA_PETITA" or clave == "MIDA_MITJANA" or clave == "ZIP_FILE":
        print('El valor actual:', configuracion[clave])
        nuevo_valor = input('Introduce el nuevo valor:')
        configuracion[clave] = nuevo_valor
    if clave == "EXTENSION_FILTRADA":
        print('El valor actual:', configuracion[clave])
        nuevo_valor = input('Introduce el nuevo valor (ejemplo: ["XXX","xxx","..."]):')
        configuracion[clave] = nuevo_valor
    print("La configuración se ha actualizado correctamente.")
    print(configuracion)



def guardar_config():
    global configuracion
    print(f"Confirma la configuración {configuracion}")
    nombre_archivo = input("Introduce el nombre del archivo de configuración a crear (o deja en blanco para usar el nombre por defecto 'config.cfg'): ")
    if nombre_archivo == "":
        nombre_archivo = 'config.cfg'

    # Comprobar si el archivo ya existe
    if os.path.exists(nombre_archivo):
        respuesta = input(f"El archivo {nombre_archivo} ya existe. ¿Quieres sobreescribirlo? (s/n): ").strip()
        if respuesta != 's':
            print("Operación cancelada.")
            return

    # Escribir la configuración en el archivo
    with open(nombre_archivo, 'w') as f:
        f.write(str(configuracion))

    print(f"La configuración se ha guardado correctamente en el archivo '{nombre_archivo}'.")

config = sys.argv[1]
