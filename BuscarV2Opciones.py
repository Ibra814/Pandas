import pandas as pd

# Leer archivos
df = pd.read_excel("Json.xlsx")
data = pd.read_excel("Facturar.xlsx")

# Definir las columnas clave en cada DataFrame
columnas_clave_df = ["id", "documento", "cups"]     # en df
columnas_clave_data = ["id", "documento", "cup"]    # en data

# Columnas que se van a mapear: {columna_df: columna_data}
columnas_a_mapear = {
    "dx": "dx",
    "profesional": "profesional",
    "cuota": "copago",
    "num_cuota": "factura_encontrada",
    "valor_unitario": "valor_unitario",
    "factura": "factura",
    "autorizacion": "autorizacion",
}

# Crear columnas clave combinadas para unir
df["__clave__"] = df[columnas_clave_df].astype(str).agg("||".join, axis=1)
data["__clave__"] = data[columnas_clave_data].astype(str).agg("||".join, axis=1)

# Realizar los mapeos usando la clave combinada
for col_df, col_data in columnas_a_mapear.items():
    diccionario = dict(zip(data["__clave__"], data[col_data]))
    df[col_df] = df["__clave__"].map(diccionario)

# Eliminar columna temporal
df.drop(columns="__clave__", inplace=True)

# Guardar resultado
df.to_excel("Jsonxlsx.xlsx", index=False)
