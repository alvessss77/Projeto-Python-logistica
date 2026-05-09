import os

print("""𝙎𝙞𝙨𝙩𝙚𝙢𝙖 𝙙𝙚 𝙈𝙤𝙣𝙞𝙩𝙤𝙧𝙖𝙢𝙚𝙣𝙩𝙤 𝙙𝙚 𝙍𝙤𝙩𝙖𝙨
      """)


def analisar_velocidade(distancia, tempo):
    """Calcula a velocidade média e classifica o desempenho da viagem."""
    velocidade_media = distancia / tempo
    
    if velocidade_media > 110:
        return "Risco de Multa"
    elif 80 <= velocidade_media <= 110:
        return "Eficiente"
    elif 50 <= velocidade_media < 80:
        return "Lento"
    else:
        return "Congestionamento"


print("=== CONFIGURAÇÃO DO SISTEMA SMR ===")
nome_motorista = input("Nome do Motorista: ")
limite_diario = float(input("Limite Diário de Quilometragem (Km): "))
jornada_prevista = float(input("Jornada de Trabalho Prevista (horas): "))
quilometragens_rota = []  


while True:
    tempo_total = float(input("\nInforme o tempo total gasto na rota (horas): "))
    if tempo_total > 0:
        break
    print("[ERRO] O tempo deve ser maior que zero!")


paradas = int(input("Quantidade de paradas não programadas: "))
if paradas > 5:
    print("Alerta: Verifique a segurança do veículo")
else:
    print("Prosseguindo para análise de metas...")


print("\n--- Cadastro de Trechos (digite 0 para encerrar) ---")
while True:
    km_trecho = float(input("Quilometragem do trecho: "))
    if km_trecho <= 0:
        break
    quilometragens_rota.append(km_trecho)


distancia_total = 0
print("\n--- Detalhamento da Rota ---")
for km in quilometragens_rota:
    print(f"Trecho percorrido: {km} Km")
    distancia_total += km 


while True:
    nivel_combustivel = int(input("\nNível de Combustível Inicial (0 a 100): "))
    if 0 <= nivel_combustivel <= 100:
        break
    print("[ERRO] Valor inválido! Informe de 0 a 100.")


print("\n" + "="*30)
print("      RELATÓRIO FINAL SMR      ")
print("="*30)
print(f"Motorista: {nome_motorista}")
print(f"Distância Total: {distancia_total} Km")


classificacao = analisar_velocidade(distancia_total, tempo_total)
print(f"Classificação de Desempenho: {classificacao}")


if distancia_total < limite_diario and tempo_total <= jornada_prevista:
    print("PARABÉNS! Você ganhou o Prêmio de Consistência! 🏆")
else:
    print("Infelizmente as metas de consistência não foram atingidas.")

print(f"\nEncerrando sistema. Boa viagem, {nome_motorista}!")

# NOTAS PARA O PROFESSOR: UTILIZAMOS O APPEND PARA ADICIONAR ELEMENTOS NA LISTA #
# UTILIZAMOS O \N PARA TER UMA SEPARAÇÃO E FICAR MAIS APRESENTÁVEL #
# UTILIZAMOS O F PARA FACILITAR E UNIR AS VARIÁVEIS #
# UTILIZAMOS TAMBÉM ASPAS TRIPLAS PARA MELHOR VISUALIZAÇÃO DA APLICAÇÃO #
# PROGRAMA FEITO POR DANIEL PASSIANI E GABRIEL OBER COM ASSISTÊNCIA DAS ANOTAÇÕES DO GOOGLE KEEP FEITAS EM AULA #