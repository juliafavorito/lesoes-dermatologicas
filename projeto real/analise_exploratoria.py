import pandas as pd
import os
import pandas as pd

# Descobre a pasta onde o seu script Python está rodando
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Junta a pasta com o nome do arquivo de forma segura
caminho_completo = os.path.join(diretorio_atual, 'metadata.csv')

df = pd.read_csv(caminho_completo)
print(df.info())
print(df.head())
print(df.shape)