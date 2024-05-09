import os
import shutil
import config
import sys
import pwd

propietarios = []

def crear_dir_dst():

    with open('config.txt') as f:
        config_file = eval(f.read())

    directorio = config_file['DIR_DST']
    os.mkdir(directorio)
    for i in range(1, 4):
        propietario = os.path.basename(directorio) + str(i)
        propietarios.append(propietario)

    directorio_user = propietarios
    midas = ['gran', 'mitja', 'petita']

    for propietario in directorio_user:
        dir_path = os.path.join(directorio, propietario)
        os.mkdir(dir_path)
        print(f'Directorio "{dir_path}" creado.')

        for subdirectorio in midas:
            dir_path2 = os.path.join(dir_path, subdirectorio)
            os.mkdir(dir_path2)
            print(f'Directorio "{dir_path2}" creado.')


def classificar_arxius():
    with open('config.txt') as f:
        configuracio = eval(f.read())

    DIR_INIT = configuracio["DIR_INIT"]
    DIR_DST = configuracio["DIR_DST"]
    MIDA_PETITA = configuracio["MIDA_PETITA"]
    MIDA_MITJANA = configuracio["MIDA_MITJANA"]

    # Obtener una lista de propietarios únicos en el directorio de destino
    propietarios = os.listdir(DIR_DST)

    for root, dirs, files in os.walk(DIR_INIT):
        for file in files:
            file_path = os.path.join(root, file)
            propietario_uid = os.stat(file_path).st_uid
            propietario_nombre = pwd.getpwuid(propietario_uid).pw_name
            size = os.path.getsize(file_path)
            print("Archivo:", file, 'con la ruta', root, 'con tamaño de', size, 'con propietario', propietario_nombre)

            # Convertir tamaño de bytes a kilobytes
            size_kb = size / 1024

            if size_kb < MIDA_PETITA:
                destino = "petita"
            elif MIDA_PETITA <= size_kb < MIDA_MITJANA:
                destino = "mitja"
            else:
                destino = "gran"

            # Crear directorio de destino si no existe
            destination_directory = os.path.join(DIR_DST, propietario_nombre, destino)

            destination_path = os.path.join(destination_directory, file)  # Ruta del archivo de destino
            shutil.copy(file_path, destination_path)
            print('Moviendo', file, 'a', destination_path)

def filtrar_archivos():

    with open('config.txt') as f:
        configuracio = eval(f.read())

    DIR_INIT = configuracio["DIR_INIT"]
    FILTRADA = configuracio["EXTENSION_FILTRADA"]

    for root, dirs, files in os.walk(DIR_INIT):
        for file in files:
            file_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1]



            print("Archivo:", file, 'con la ruta', root)
            print(extension)

        #if file_path in


def comprovar_classificacio():
    with open('config.txt') as f:
        configuracio = eval(f.read())
    DIR_DST = configuracio["DIR_DST"]
    if DIR_DST:
        os.system(f"tree -h {DIR_DST}")
    else:
        print('no')

def menu_configuración():
    while True:
        print('\n\tMENU configuración')
        print('1. veure_config')
        print('2. Carregar config')
        print('3. Canviar paràmetres')
        print('4. Desar config')
        print('5. Salir')
        opcion = -1
        while opcion not in [0, 1, 2, 3, 4, 5, 6]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            config.veure_config()
        elif opcion == 2:
            config.Carregar_config()
        elif opcion == 3:
            config.cambiar_parametros()
        elif opcion == 4:
            config.guardar_config()
        elif opcion == 5:
            break
        else:
            print('Opción no válida. Por favor, elige una opción válida.')


def menu():
    while True:
        print('\n\tMENU PRINCIPAL: \n')
        print('1. Configuración')
        print('2. creacio de directoris')
        print('3. classificacio arxius')
        print('4. filtratge')
        print('5. canvis de propietari i de permisos')
        print('6. comprovació')
        print('7. compressió')
        print('8. creació d’informe')
        print('0. Salir')
        opcion = -1
        while opcion not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            menu_configuración()
        elif opcion == 2:
            crear_dir_dst()
        elif opcion == 3:
            classificar_arxius()
        elif opcion == 4:
            filtrar_archivos()
        elif opcion == 5:
            pass
        elif opcion == 6:
            comprovar_classificacio()
        else:
            break


if len(sys.argv) < 2:
    print("Por favor, proporcione el nombre del archivo de configuración como argumento.")
    sys.exit(1)

config.txt = sys.argv[1]



menu()

