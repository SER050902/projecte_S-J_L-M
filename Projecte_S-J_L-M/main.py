import os
import shutil
import config
import sys

def crear_dir_dst():

    with open('config.txt') as f:
        config_file = eval(f.read())

    directorio = config_file['DIR_DST']
    os.mkdir(directorio)
    users = []
    for i in range(1, 4):
        user = os.path.basename(directorio) + str(i)
        users.append(user)

    for user in users:
        cmd = f'useradd {user}'
        os.system(cmd)
        print('ejecutado:', cmd)

    directorio_user = users
    midas = ['gran', 'mitja', 'petita']

    for user in directorio_user:
        dir_path = os.path.join(directorio, user)
        os.mkdir(dir_path)
        print(f'Directorio "{dir_path}" creado.')
        shutil.chown(dir_path, user, user)
        print('Permisos cambiados para:', dir_path)

        for subdirectorio in midas:
            dir_path2 = os.path.join(dir_path, subdirectorio)
            os.mkdir(dir_path2)
            print(f'Directorio "{dir_path2}" creado.')


def classificar_arxius():
    return os.listdir('dani_init')

def menu_configuración():
    while True:
        print('\n\tMENU configuración')
        print('1. veure_config')
        print('2. Carregar config')
        print('3. Canviar paràmetres')
        print('4. Desar config')
        print('5. Salir')
        opcion = -1
        while opcion not in [0, 1, 2, 3, 4, 5]:
            opcion = int(input('Opción: '))
        if opcion == 1:
            config.veure_config()
        elif opcion == 2:
            config.Carregar_config()
        elif opcion == 3:
            config.cambiar_parametros()
        elif opcion == 4:
            config.guardar_config()
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
        if opcion == 2:
            crear_dir_dst()
        else:
            break


if len(sys.argv) < 2:
    print("Por favor, proporcione el nombre del archivo de configuración como argumento.")
    sys.exit(1)

config.txt = sys.argv[1]


menu()

