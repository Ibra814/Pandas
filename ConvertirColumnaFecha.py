import pandas as pd
df['fecha'] = pd.to_datetime(df['fecha']).dt.strftime('%Y-%m-%d')
