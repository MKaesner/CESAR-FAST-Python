import os

# Inicializando dicionário de votos
votos = {
    'Bart Simpson': 0,
    'Homer Simpson': 0,
    'Nulos': 0
}

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def apresentar_resultados(titulo):
    limpa_tela()  
    print(f"############ {titulo} ###################")
    for candidato, total_votos in votos.items():
        print(f"Total ({candidato}): {total_votos}")
    print(f"Total de votos NULOS: {votos['Nulos']}")
    print(f"Total de votos VÁLIDOS: {sum(votos.values()) - votos['Nulos']}")
    print("#################################################")

def registrar_voto(voto):
    global votos
    if voto in votos:
        votos[voto] += 1
    else:
        votos['Nulos'] += 1

# Captação de votos
for _ in range(5):
    apresentar_resultados("RESULTADOS PARCIAIS")
    voto = input("Digite o código do candidato (1-Bart e 2-Homer): ")
    if voto == '1':
        registrar_voto('Bart Simpson')
    elif voto == '2':
        registrar_voto('Homer Simpson')
    else:
        registrar_voto('Nulos')

# Tratando os possíveis resultados (VENCEDOR-EMPATE-ANULAÇÃO)
total_votos_validos = sum(votos.values()) - votos['Nulos']

if total_votos_validos == 0:
    apresentar_resultados("ELEIÇÃO ANULADA POR AUSÊNCIA DE VOTOS VÁLIDOS")
elif votos['Bart Simpson'] != votos['Homer Simpson']:
    apresentar_resultados("RESULTADOS FINAIS")
    mais_votado = max(votos, key=votos.get)
    menos_votado = min(votos, key=votos.get)
    print(f"O candidato MAIS votado: {mais_votado}  Totalizando: {votos[mais_votado]} votos.")
    print(f"O candidato MENOS votado: {menos_votado}  Totalizando: {votos[menos_votado]} votos.")
else:
    apresentar_resultados("ELEIÇÃO EMPATADA")
    for candidato, total_votos in votos.items():
        print(f"O candidato {candidato} totalizou: {total_votos} votos.")
