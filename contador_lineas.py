# Define el nombre del archivo que contiene las instrucciones SQL
nombre_archivo = '/Users/carmen/Documents/sta/MDS/archivos_carga_bd/DMI_31122022_concolumnas_7_8.sql'

# Inicializa un contador
contador = 0

# Abre el archivo para leer
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    # Recorre cada línea en el archivo
    for linea in archivo:
        # Quita los espacios en blanco al final de la línea y verifica si termina con ;
        if linea.strip().endswith(';'):
            contador += 1

# Imprime el total de líneas que terminan con ;
print(f"Total de líneas que terminan con ';': {contador}")
