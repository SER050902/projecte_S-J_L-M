import os
import shutil
import config
import sys

users = []
def crear_dir_dst():

    with open('config.cfg') as f:
        config_file = eval(f.read())

    directorio = config_file['DIR_DST']
    os.mkdir(directorio)
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
    with open('config.cfg') as f:
        configuracio = eval(f.read())

    DIR_INIT = configuracio["DIR_INIT"]
    DIR_DST = configuracio["DIR_DST"]
    MIDA_PETITA = configuracio["MIDA_PETITA"]
    MIDA_MITJANA = configuracio["MIDA_MITJANA"]


    for root, dirs, files in os.walk(DIR_INIT):
        for file in files:
            filepath = os.path.join(root,file)
            size = os.path.getsize(filepath)
            gran = DIR_DST + '/louay1'

            print(gran)
            print("Archivo:",file,'con la ruta', root,'con tamaño de',size)

            '''if size < MIDA_PETITA:
                shutil.copy(filepath,)'''


classificar_arxius()