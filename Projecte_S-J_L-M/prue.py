import sys
import os


def create_directory(directory_path):
    # Crear el directorio si no existe
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directorio '{directory_path}' creado exitosamente.")
    else:
        print(f"El directorio '{directory_path}' ya existe.")


def create_directories(config_file, option):
    # Verificar si el archivo de configuración existe
    if not os.path.exists(config_file):
        print(f"El archivo de configuración '{config_file}' no existe.")
        return

    # Abrir el archivo de configuración
    with open(config_file, 'r') as f:
        lines = f.readlines()
        # Leer las líneas del archivo de configuración
        for line in lines:
            # Dividir la línea en la clave y el valor
            key, value = map(str.strip, line.split(',', 1))
            if option == 1 and key == 'dir_init':
                create_directory(value)
            elif option == 2 and key == 'dir_dst':
                create_directory(value)


def print_menu():
    print("Menú:")
    print("1. Crear directorio")
    print("2. Crear subdirectorio")


if __name__ == "__main__":
    # Verificar si se proporcionó un argumento de línea de comandos
    if len(sys.argv) < 2:
        print("Por favor, proporcione el nombre del archivo de configuración como argumento.")
        sys.exit(1)

    # Obtener el nombre del archivo de configuración desde el argumento de línea de comandos
    config_file = sys.argv[1]

    # Imprimir el menú
    print_menu()

    # Pedir al usuario que elija una opción
    try:
        option = int(input("Seleccione una opción (1 o 2): "))
        if option not in [1, 2]:
            raise ValueError("Opción no válida.")
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

    # Llamar a la función para crear el directorio o subdirectorio especificado en el archivo de configuración
    create_directories(config_file, option)

print_menu()