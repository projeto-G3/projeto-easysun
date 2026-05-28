import src.menus as ui
import src.funcoes as fc
import os
os.system("cls")

while True:
    escolha = int(input(ui.MENU_PRINCIPAL))
    if escolha == 1:
        fc.cadastrar_orcamento(escolha)

    elif escolha == 2:
        fc.verificar_orcamentos(escolha)
    
    elif escolha == 3:
        fc.atualizar_orcamento(escolha)
    
    elif escolha == 4:
        fc.excluir_orcamento(escolha)

    opcao = int(input(ui.MENU_SAIDA))
    if opcao == 1:
        os.system("cls")
        continue
    
    elif opcao == 2:
        os.system("cls")
        print("\n\033[1;31mProgama encerrado.\033[m")
        break

    else:
        print("Valor inválido.")

    if escolha < 1 or escolha > 5:
        os.system("cls")
        print("\n\033[1;31mOpção inválida\033[m\nDigite um valor válido")
        continue