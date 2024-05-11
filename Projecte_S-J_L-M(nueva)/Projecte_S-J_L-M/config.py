import os

configuracion = {
    "DIR_INIT": "../Projecte_S-J_L-M/",
    "DIR_DST": "../Projecte_S-J_L-M/ggm_classificat",
    "MIDA_PETITA": 17,
    "MIDA_MITJANA": 20,
    "EXTENSION_FILTRADA" : ["pdf", "txt", "bin"],
    "DIR_QUARANTENA": "../Projecte_S-J_L-M/quarentena",
    "ZIP_FILE":"zip_file.zip"
}

def veure_config():
    with open('config.cfg', 'r') as f:
        config_file = f.read()
        print(config_file)

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



def cambiar_parametros():
    print('LA INFORMACION DE configuración')
    veure_config()
    clave = input('Introduce la clave que quieres cambiar: ')
    if clave not in configuracion:
        print("La clave", clave, "no existe en la configuración.")
        return

    print('El valor actual:', configuracion[clave])
    nuevo_valor_ruta = input('Introduce el nuevo valor: ../Projecte_S-J_L-M/')
    nuevo_valor = "../Projecte_S-J_L-M/" + nuevo_valor_ruta

    configuracion[clave] = nuevo_valor
    print("La configuración se ha actualizado correctamente.")

    veure_config()

def guardar_config():
    global configuracion
    nombre_archivo = input("Introduce el nombre del archivo de configuración a crear (o deja en blanco para usar el nombre por defecto 'config.cfg'): ")
    if nombre_archivo == "":
        nombre_archivo = 'config.cfg'

    # Comprobar si el archivo ya existe
    if os.path.exists(nombre_archivo):
        respuesta = input(f"El archivo '{nombre_archivo}' ya existe. ¿Quieres sobreescribirlo? (s/n): ").strip()
        if respuesta != 's':
            print("Operación cancelada.")
            return

    # Escribir la configuración en el archivo
    with open(nombre_archivo, 'w') as f:
        f.write(str(configuracion))

    print(f"La configuración se ha guardado correctamente en el archivo '{nombre_archivo}'.")


