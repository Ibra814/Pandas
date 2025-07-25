#Este codigo es para completar la informacion de un excel desde otro excel con una sola condicion
#las columnas en el excel ya deben existir, deben estar vacias

import pandas as pd
import numpy as np

# Leer archivos
df = pd.read_excel("Json.xlsx") #Excel el cual vamos a completar
data = pd.read_excel("Facturar.xlsx") #Excel de la base maestra

columna_clave_df = "id" #nombre de la columna en df
columna_clave_data = "id" #nombre de la columna en data

#las claves del diccionario es el nombre de las filas del excel df, los valores del diccionario son las columnas de la base maestra
columnas_a_mapear = {
    "documento": "documento",
    "cups": "cup",
    "dx": "dx",
    "profesional": "profesional",
    "cuota": "copago",
    "num_cuota": "factura_encontrada",
    "valor_unitario": "valor_unitario",
    "factura": "factura",
    "autorizacion": "autorizacion",
}

# Aplicar mapeo respetando las claves diferentes
for col_df, col_data in columnas_a_mapear.items():
    diccionario = dict(zip(data[columna_clave_data], data[col_data]))
    df[col_df] = df[columna_clave_df].map(diccionario)


# Guardar resultado
df.to_excel("Jsonxlsx", index=False)
