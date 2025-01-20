import os

# Função para limpar a tela, com suporte para diferentes sistemas operacionais
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# Dicionário contendo o portfólio de carros disponíveis (chave: código do carro, valor: [modelo, preço por dia])
portifolio = [
("Chevrolet Tracker", 120), 
("Chevrolet Onix", 90), 
("Chevrolet Spin", 150), 
("Hyunday HB20", 85),
("Hyundai Tucson", 120), 
("Fiat Uno", 60), 
("Fiat Mob", 70), 
("Fiat Pulse", 130 )          
]

def mostrar_portifolio(portifolio):
    for i, car in enumerate(portifolio):
        print(f"[{i}] {car[0]} - R$ {car[1]} /dia")

def mostrar_alugados(alugados):
    for i, car in enumerate(alugados):
        print(f"[{i}] {car[0]} - R$ {car[1]} /dia")

# Dicionário para armazenar os carros alugados (chave: código do carro, valor: [modelo, preço por dia])
alugados = []
temp = []

# Loop principal do programa
while True:
    limpar_tela()

    print("=" * 10)
    print("Bem vindo à locadora de carros!")
    print("=" * 10)

    # Menu principal
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    comando = input(">>> ")
    if comando not in ["0", "1", "2"]:
        limpar_tela()
        print("Digite um valor válido!")
        continue

    # Opção 0: Mostrar portfólio
    if comando == "0":
        limpar_tela()
        print("=" * 10)
        mostrar_portifolio(portifolio) 
    
    # Opção 1: Alugar um carro
    elif comando == "1":
        print("[ALUGAR] - veja o portifólio de carros disponíveis.\n")
        mostrar_portifolio(portifolio)
        print("=" * 10)
        print("Escolha o código do carro: ")
        try:
            cod_car = int(input(">>> "))
        except ValueError:
            limpar_tela()
            print("Digite um número válido!")
            continue

        if cod_car < 0 or cod_car >= len(portifolio):
            print("Carro não disponível ou já alugado! Escolha um código válido.")
            input("\nPressione Enter para continuar...")
            continue
        
        print("Escolha por quantos dias deseja alugar: ")
        try:
            dias = int(input(">>> "))
        except ValueError:
            limpar_tela()
            print("Digite um número válido!")
            continue
        car = portifolio[cod_car]
        limpar_tela()
        print(f"\nVocê escolheu {car[0]} por {dias} dias.")
        print(f"O aluguel totalizaria R$ {car[1] * dias}. Deseja alugar?")

        print("\n0 - SIM | 1 - NÃO")
        resp = input(">>> ")
        if resp not in ["0", "1"]:
            limpar_tela()
            print("Digite um valor válido.")
            continue
        if resp == "0":
            carro_alugado = portifolio.pop(cod_car)
            alugados.append(carro_alugado)
            print(f"\nParabéns, você alugou o {carro_alugado[0]} por {dias} dia(s)")


    # Opção 2: Devolver um carro
    elif comando == "2":
        if len(alugados) == 0:
            print("Não há carros alugados.")
            input("\nPressione Enter para continuar...")
        else: 
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_alugados(alugados)
        
            print("Escolha o código do carro que deseja devolver: ")
            try:
                cod_car = int(input(">>> "))
            except ValueError:
                limpar_tela()
                print("Digite um número válido!")
                continue
            
            if cod_car < 0 or cod_car >= len(alugados):
                print("Digite um código válido!")
                input("\nPressione Enter para continuar...")
                continue
            else:
                carro_devolvido = alugados.pop(cod_car)
                portifolio.append(carro_devolvido)
                print(f"Obrigado por devolver o carro {carro_devolvido[0]}.")

    
    print("=" * 10)
    print("0 - CONTINUAR | 1 - SAIR")
    resp = input(">>> ")
    if resp not in ["0", "1"]:
        limpar_tela()
        print("Digite um valor válido.")
        continue
    if resp == "1":
        break

