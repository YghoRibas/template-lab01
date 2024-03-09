import pandas as pd

df = pd.read_csv('./dataset/resultadosq2.txt', skiprows=1)

segundo_indice_coluna = 1

sumarized_data = df.groupby(df.columns[1]).agg({
    0: 'count', 
    2: 'sum',  
    4: 'sum'     
}).reset_index()

print(sumarized_data)
