import os
import shutil
import configuracion
import sys
import pwd


def crear_dir_dst():

    with open(config) as f:
        configuracio = eval(f.read())

    propietarios = []
    directorio = configuracio['DIR_DST']
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
    with open(config) as f:
        configuracio = eval(f.read())

    DIR_INIT = configuracio["DIR_INIT"]
    DIR_DST = configuracio["DIR_DST"]
    MIDA_PETITA = configuracio["MIDA_PETITA"]
    MIDA_MITJANA = configuracio["MIDA_MITJANA"]

    for ruta, cuerpo, ficheros in os.walk(DIR_INIT):
        for fichero in ficheros:
            file_path = os.path.join(ruta, fichero)
            propietario_uid = os.stat(file_path).st_uid
            propietario_nombre = pwd.getpwuid(propietario_uid).pw_name
            size = os.path.getsize(file_path)
            print("Archivo:", fichero, 'con la ruta', ruta, 'con tamaño de', size, 'con propietario', propietario_nombre)

            # Convertir tamaño de bytes a kilobytes
            size_kb = size / 1024

            if size_kb < MIDA_PETITA:
                destino = "petita"
            elif MIDA_PETITA <= size_kb < MIDA_MITJANA:
                destino = "mitja"
            else:
                destino = "gran"

            destino_directorio = os.path.join(DIR_DST, propietario_nombre, destino,fichero)


            shutil.copy(file_path, destino_directorio)
            print('Moviendo', fichero, 'a', destino_directorio)
    

def filtrar_archivos():
    with open(config) as f:
        configuracio = eval(f.read())

    DIR_INIT = configuracio["DIR_INIT"]
    DIR_DST = configuracio["DIR_DST"]
    DIR_QUARANTENA = configuracio["DIR_QUARANTENA"]
    EXTENSION_FILTRADA = configuracio["EXTENSION_FILTRADA"]

    for ruta,cuerpo,ficheros in os.walk(DIR_INIT):
        for fichero in ficheros:
            file_path = os.path.join(ruta,fichero)
            filtrar = os.path.basename(file_path)

            if filtrar.split('.')[1] in EXTENSION_FILTRADA:
                os.makedirs(DIR_QUARANTENA,exist_ok=True)
                if DIR_QUARANTENA:
                    shutil.copy(file_path,DIR_QUARANTENA)
                    print('copiado')
                else:
                    print('encontrado')



def cambiar_per_pro():
    with open(config) as f:
        configuracio = eval(f.read())

    DIR_DST = configuracio["DIR_DST"]

    user = input('Introduce el USUARIO:')
    os.system(f'sudo useradd -m {user}')

    grupo = input('Introduce el GRUPO:')
    os.system(f'sudo groupadd {grupo}')

    os.system(f'sudo chown {user}:{grupo} {DIR_DST}')

    os.system(f'sudo chmod 775 {DIR_DST}')

    for ruta, cuerpo, ficheros in os.walk(DIR_DST):
        for fichero in ficheros:
            file_path = os.path.join(ruta, fichero)
            os.system(f'sudo chmod 664 {file_path}')

def comprir():
    with open(config) as f:
        configuracio = eval(f.read())

    ZIP_FILE = configuracio['ZIP_FILE']
    DIR_DST = configuracio['DIR_DST']


    shutil.make_archive(ZIP_FILE,'zip',base_dir=DIR_DST)
    print('comprirdo')


def comprovar_classificacio():
    with open(config) as f:
        configuracio = eval(f.read())
    DIR_DST = configuracio["DIR_DST"]
    if DIR_DST:
        os.system(f"tree -h {DIR_DST}")
    else:
        print('no')


def menu_configuración():
    while True:
        print('\n\tMENU configuración por defecto')
        print('1. veure_config')
        print('2. Carregar config')
        print('3. Canviar paràmetres')
        print('4. Desar config')
        print('5. Salir')
        opcion = -1
        while opcion not in [0, 1, 2, 3, 4, 5, 6]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            configuracion.veure_config()
        elif opcion == 2:
            configuracion.Carregar_config()
        elif opcion == 3:
            configuracion.cambiar_parametros()
        elif opcion == 4:
            configuracion.guardar_config()
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
            cambiar_per_pro()
        elif opcion == 6:
            comprovar_classificacio()
        elif opcion == 7:
            comprir()
        elif opcion == 8:
            pass
        else:
            break


if len(sys.argv) < 2:
    print("Por favor, proporcione el nombre del archivo de configuración como argumento.")
    sys.exit(1)

config = sys.argv[1]

menu()


