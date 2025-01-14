import os
import time

# Função para limpar a tela, com suporte para diferentes sistemas operacionais
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Dicionário contendo o portfólio de carros disponíveis (chave: código do carro, valor: [modelo, preço por dia])
portifolio = {
"0": ["Chevrolet Tracker", 120], 
"1": ["Chevrolet Onix", 90], 
"2": ["Chevrolet Spin", 150], 
"3": ["Hyunday HB20", 85],
"4": ["Hyundai Tucson", 120], 
"5": ["Fiat Uno", 60], 
"6": ["Fiat Mob", 70], 
"7": ["Fiat Pulse", 130]
}

# Dicionário para armazenar os carros alugados (chave: código do carro, valor: [modelo, preço por dia])
rent = {}

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
        print("=" * 10)
        for cod, desc in portifolio.items():
            print(f"[{cod}] {desc[0]} - R$ {desc[1]} /dia")  
        print("=" * 10)
        print("0 - CONTINUAR, 1 - SAIR")
        resp = input(">>> ")
        if resp not in ["0", "1"]:
            limpar_tela()
            print("Digite um valor válido!")
            continue
        elif resp == "1":
            limpar_tela()
            break
        else:
            limpar_tela()
    
    # Opção 1: Alugar um carro
    elif comando == "1":
        print("=" * 10)
        print("Escolha o código do carro: ")
        cod_car = (input(">>> "))
        if cod_car not in list(portifolio.keys()):
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
            temp = portifolio.pop(cod_car, None)
            if temp is not None:
                rent[cod_car] = temp
            print(f"\nParabéns, você alugou o {car[0]} por {dias} dia(s).")

        print("=" * 10)
        print("0 - CONTINUAR | 1 - SAIR")
        resp = input(">>> ")
        if resp not in ["0", "1"]:
            limpar_tela()
            print("Digite um valor válido.")
            continue
        if resp == "1":
            break

    # Opção 2: Devolver um carro
    elif comando == "2":
        if len(rent) == 0:
            print("Não há carros alugados.")
            time.sleep(2)
        else: 
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            for cod, desc in rent.items():
                print(f"[{cod}] {desc[0]} - R$ {desc[1]} /dia")
        
            print("Escolha o código do carro que deseja devolver: ")
            cod_car = input(">>> ")
            if cod_car not in list(rent.keys()):
                limpar_tela()
                print("Digite um código válido!")
                continue
            else:
                car = list(rent[cod_car])
                temp = rent.pop(cod_car, None)
                if temp is not None:
                    portifolio[cod_car] = temp
                print(f"Obrigado por devolver o carro {car[0]}")

                print("=" * 10)
                print("0 - CONTINUAR | 1 - SAIR")
                resp = input(">>> ")
                if resp not in ["0", "1"]:
                    limpar_tela()
                    print("Digite um valor válido.")
                    continue
                if resp == "1":
                    limpar_tela()
                    break

