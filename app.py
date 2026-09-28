# Programa de pesquisa de satisfação - TudoWeb

# Contadores das respostas
excelente = 0
ruim = 0

# Repetição para realizar a pesquisa com 50 entrevistados
for i in range(50):

    # Entrada dos dados do entrevistado
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    # Apresentação das opções de atendimento
    print("\nOpções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    # Verificação da opinião e atualização dos contadores
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

# Exibição do resultado final da pesquisa
print("\n--- RESULTADO DA PESQUISA ---")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")

