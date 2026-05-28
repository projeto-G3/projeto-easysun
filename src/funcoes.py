import src.menus as ui
import os
import uuid

def pedir_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("\n\033[1;31mInforme um valor numérico válido!\033[m")

def cadastrar_orcamento(escolha):
    if escolha == 1:
        os.system("cls")
        marca_modulo = input("\nInforme a marca dos módulos: ").lower()
        modelo_modulo = input("\nQual o modelo do módulo: ").lower()
        marca_inversor = input("\nInforme a marca dos inversores: ").lower()
        modelo_inversor = input("\nQual o modelo do inversor: ").lower()
        potencia_kwp = pedir_float("\nQual a potência em KWP: ")
        geracao_anual = pedir_float("\nQual a geração anual prometida: ")
        preco_total = pedir_float("\nQual o preço total em R$")
        payback = pedir_float("\nQual o payback prometido: ")
        cidade = input("\nQual a cidade do orçamento: ").capitalize()
        id_orcamento = str(uuid.uuid4())[:8]
        print(f"\nEsse {id_orcamento} é o seu ID de orçamento.")

    arquivo_existe = os.path.exists("data/orcamentos.csv")

    with open("data/orcamentos.csv", "a", newline = "", encoding = "utf-8") as arquivo:
        if not arquivo_existe:
            arquivo.write("id_orcamento,marca_modulo,modelo_modulo,marca_inversor,modelo_inversor,potencia_kwp,geracao_anual,preco_total,payback,cidade\n")
        arquivo.write(f"{id_orcamento},{marca_modulo},{modelo_modulo},{marca_inversor},{modelo_inversor},{potencia_kwp},{geracao_anual},{preco_total},{payback},{cidade}\n")

def verificar_orcamentos(escolha):
    if escolha == 2:
        os.system("cls")
        id_verificacao = input("Informe o ID do orçamento que deseja vizualizar: ")

        with open("data/orcamentos.csv", "r", encoding = "utf-8") as arquivo:
            linhas = arquivo.readlines()

        orcamento_encontrado = 0

        for linha in linhas:
            campos = linha.split(",")
            if id_verificacao == campos[0]:
                orcamento_encontrado + 1
                print("=" * 40)
                print(f"  ORÇAMENTO {campos[0]}")
                print("=" * 40)
                print(f"  Módulo:      {campos[1]} - {campos[2]}")
                print(f"  Inversor:    {campos[3]} - {campos[4]}")
                print(f"  Potência:    {campos[5]} kWp")
                print(f"  Geração:     {campos[6]} MWh/ano")
                print(f"  Preço total: R$ {campos[7]}")
                print(f"  Payback:     {campos[8]} anos")
                print(f"  Cidade:      {campos[9]}")
                print("=" * 40)
            
        if orcamento_encontrado == 0:
            os.system("cls")
            print("\nId inválido.")
