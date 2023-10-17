import os
import pandas as pd

def limpa_tela():  
    os.system('cls' if os.name == 'nt' else 'clear')

def carregando_dataset(caminho, arquivo): 
    return pd.read_csv(os.path.join(caminho, arquivo), encoding='latin1', parse_dates=['data_vacinacao'])

def filtro_1(df): 
    return df[(df['municipio'] == 'RECIFE') & 
              (df['sexo'] == 'FEMININO') & 
              ((df['raca_cor'] == 'PARDA') | (df['raca_cor'] == 'PRETA')) & 
              (df['idade'] > 60)]

def filtro_2(df): 
    return df[(df['data_vacinacao'].dt.month.isin([4, 5])) & 
              (df['municipio'] == 'RECIFE') & 
              (df['raca_cor'] == 'PRETA') & 
              (df['sexo'] == 'MASCULINO')]

def formatando_data(df): 
    df['data_vacinacao'] = df['data_vacinacao'].dt.strftime('%d-%m-%Y')
    return df

def display_results(resultado, QtdReg, num_registros, colunas):
    print(f'Amostra dos primeiros {QtdReg} resultados, totalizando: ({num_registros} registros): ordenados por data(+), município e idade(-)')
    print(resultado.head(QtdReg)[colunas].to_string(index=False))

# Constantes e Parâmetros
arquivo = "vacinados.csv"
caminho = r"C:\MKaesner"
QtdReg = 5 # Definido o número de registros para exibição parcial
colunas_exibir = ['_id', 'idade', 'sexo', 'raca_cor', 'municipio', 'data_vacinacao']

# Limpa a tela do console
limpa_tela()

# Carrega o dataset
df = carregando_dataset(caminho, arquivo)

# Totalizando registros do dataset
num_registros = len(df)

# Aplicando Filtro 1
resultado_filtro_1 = filtro_1(df)
resultado_filtro_1 = resultado_filtro_1.sort_values(by=['data_vacinacao', 'municipio', 'idade'], ascending=[True, True, False])
num_registros_filtro_1 = resultado_filtro_1.shape[0]

# Aplicando Filtro 2
resultado_filtro_2 = filtro_2(df)
resultado_filtro_2 = resultado_filtro_2.sort_values(by=['data_vacinacao', 'municipio', 'idade'], ascending=[True, True, False])
num_registros_filtro_2 = resultado_filtro_2.shape[0]

# Formatando datas
resultado_filtro_1 = formatando_data(resultado_filtro_1)
resultado_filtro_2 = formatando_data(resultado_filtro_2)

# Exibindo resultados
print(f'O número de registros no dataset é: {num_registros}')
display_results(resultado_filtro_1, QtdReg, num_registros_filtro_1, colunas_exibir)
display_results(resultado_filtro_2, QtdReg, num_registros_filtro_2, colunas_exibir)

