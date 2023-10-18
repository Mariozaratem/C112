import os
import shutil

from_dir = r"C:\\Users\\mzara\\OneDrive\\Documentos\\BYJU\\Python\\Python 4\\Imagenes_Archivos"
to_dir = r"C:\\Users\\mzara\\OneDrive\\Documentos\\BYJU\\Python\\Python 4\\Documentos_Archivos"

# Lista de extensiones válidas
valid_extensions = ['.txt', '.doc', '.docx', '.pdf']

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    # Comprueba si la extensión del archivo está en blanco
    if not file_name:
        continue  # Salta al siguiente archivo si la extensión está en blanco

    # Obtiene la extensión del archivo
    file_extension = os.path.splitext(file_name)[1]

    # Comprueba si la extensión es válida
    if file_extension in valid_extensions:
        # Crea las rutas
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)

        # Comprueba si la carpeta/directorio de destino existe
        if os.path.exists(path2):
            # Comprueba si la ruta de destino existe en path2
            if os.path.exists(path3):
                print(f"El archivo '{file_name}' ya existe en la carpeta de destino.")
            else:
                print(f"Moviendo '{file_name}' a la carpeta de destino.")
                shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print(f"Creada la carpeta de destino: {path2}")
            print(f"Moviendo '{file_name}' a la carpeta de destino.")
            shutil.move(path1, path3)
    else:
        print(f"El archivo '{file_name}' no tiene una extensión válida.")

print("Archivos procesados correctamente.")