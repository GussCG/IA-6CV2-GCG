
#Autor: Gustavo Cerda García
#Practica 7: Dataset

#Programa que abre un dataset
#Convierte el dataset a CSV para facilitar su manejo
#Calcula el promedio, la varianza y la desviación estándar de cada columna
#Separa los datos en diferentes matrices, de acuerdo a la categoria de la última columna y repite el cálculo de promedio, varianza y desviación estándar

#Librerias
import pandas as pd #Libreria para manejo de datos

#Nombre: convertir_a_csv
#Desc: Convierte un archivo a CSV
#Entrada: 
# - archivo: Nombre del archivo a convertir
def convertir_a_csv(archivo):    
    try:
        archivo_salida = archivo.split('.')[0] + '.csv' # Nombre del archivo de salida
        
        # Leer el archivo
        df = pd.read_csv(archivo, header=None)
        
        # Convertir a CSV
        df.to_csv(archivo_salida, index=False)

        # Borrar la primera fila, ya que son los encabezados
        df = pd.read_csv(archivo_salida)
        df.to_csv(archivo_salida, index=False, header=False)

        print('Archivo convertido a CSV, con el nombre de {}\n'.format(archivo_salida))
    except FileNotFoundError:
        print('El archivo no existe\n')
    except Exception as e:
        print(f'Error: {e}\n')

# Nombre del archivo
archivo = 'dataset.data'

# Convertir a CSV
convertir_a_csv(archivo)

# ! De cada columna calcular el promedio, la varianza y la desviación estándar
# Leer el archivo
df = pd.read_csv('dataset.csv', header=None)

# print(df)

# Ignoramos la primera fila, ya que son los encabezados, empezamos en la columna 0
for i in range(0, df.shape[1] - 1):
    # Si no es numerico, no se puede calcular (es por las categorias)
    if not df[i].dtype == 'float64':
        continue
    print(f'Columna {i}')
    print(f'Promedio: {df[i].mean()}')
    print(f'Varianza: {df[i].var()}')
    print(f'Desviación estándar: {df[i].std()}')
    print()


# ! Separar los datos en diferentes matrices, de acuerdo a la categoria de la última columna y repetir el cálculo de promedio, varianza y desviación estándar
# Obtener las categorias, de la ultima columna, menos la primera fila que son los encabezados
categorias = df[df.shape[1] - 1][1:].unique() 

# Iterar sobre las categorias
for categoria in categorias:
    print(f'Categoría {categoria}')
    # Obtener las filas que coincidan con la categoria
    df_categoria = df[df[df.shape[1] - 1] == categoria]
    # Ignoramos la primera fila, ya que son los encabezados
    for i in range(0, df_categoria.shape[1] - 1):
        # Si no es numerico, no se puede calcular (es por las categorias)
        if not df_categoria[i].dtype == 'float64':
            continue
        print(f'Columna {i}')
        print(f'Promedio: {df_categoria[i].mean()}')
        print(f'Varianza: {df_categoria[i].var()}')
        print(f'Desviación estándar: {df_categoria[i].std()}')
        print()
    print()