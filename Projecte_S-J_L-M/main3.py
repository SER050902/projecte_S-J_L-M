import os
import shutil
import config
import sys


# Función para crear directorios de destino
def crear_dir_dst():
    crear_un_directorio = input('Introduce el nombre del directorio: ')
    configuracion = config.obtener_configuracion()
    configuracion['DIR_DST'] = crear_un_directorio
    directorio = configuracion['DIR_DST']

    # Crear directorio de destino
    os.makedirs(directorio, exist_ok=True)

    users = []
    for i in range(1, 4):
        user = directorio + str(i)
        users.append(user)
    print(users)
    for user in users:
        # Utilizar el nombre del directorio como nombre de usuario
        nombre_usuario = os.path.basename(user)
        cmd = f'useradd {nombre_usuario}'
        os.system(cmd)
        print('Ejecutado:', cmd)

    dir = directorio + '_dst'
    if os.path.exists(dir):
        print('El directorio', dir, 'ya existe.')
    else:
        os.mkdir(dir)
        print('Creado:', dir)

    directorio_usuario = users
    midas = ['grande', 'mediano', 'pequeño']

    for usuario in directorio_usuario:
        dir_path = os.path.join(dir,os.path.basename(usuario))  # Utilizar el nombre del directorio como nombre de usuario
        os.makedirs(dir_path, exist_ok=True)  # Asegurar que el directorio exista
        print(f'Directorios "{dir_path}" creados.')
        shutil.chown(dir_path, usuario, usuario)
        print('Permisos cambiados para:', dir_path)

        for subdirectorio in midas:
            dir_path2 = os.path.join(dir_path, subdirectorio)
            os.makedirs(dir_path2, exist_ok=True)  # Asegurar que el directorio exista
            print(f'Directorios "{dir_path2}" creados.')


# Función para clasificar archivos
def classificar_arxius():
    return os.listdir('dani_init')


# Menú de configuración
def menu_configuración():
    while True:
        print('\n\tMENÚ de configuración')
        print('1. Ver configuración')
        print('2. Cargar configuración')
        print('3. Cambiar parámetros')
        print('4. Guardar configuración')
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


# Menú principal
def menu():
    while True:
        print('\n\tMENÚ PRINCIPAL\n')
        print('1. Configuración')
        print('2. Creación de directorios')
        print('3. Clasificación de archivos')
        print('4. Filtrado')
        print('5. Cambios de propietario y permisos')
        print('6. Comprobación')
        print('7. Compresión')
        print('8. Creación de informe')
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


# Si no se proporciona un nombre de archivo de configuración, mostrar un mensaje de error y salir
if len(sys.argv) < 2:
    print("Por favor, proporcione el nombre del archivo de configuración como argumento.")
    sys.exit(1)

# Obtener el nombre del archivo de configuración desde el argumento de línea de comandos
config_file = sys.argv[1]

# Llamar al menú principal
menu()
