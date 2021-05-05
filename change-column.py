import pandas as pd
path_from = input("Digite o caminho completo do arquivo de entrada: ")
path_to = input("Digite o caminho completo do arquivo de saida: ")
header_column = input("Digite o nome da coluna: ")
str_from = input("Atual valor da célula: ")
str_to = input("Valor que quer inserir na célula: ")
df = pd.read_csv(
    path_from, delimiter=';')
print(df)
df[header_column] = df[header_column].replace({str_from: str_to})
df.to_csv(
    path_to, index=False)
