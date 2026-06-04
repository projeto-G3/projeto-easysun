import src.menus as ui
import os
import serial
import time

def ler_ldr():
    try:
        print("\nLendo incidência solar pelo sensor LDR...")
        ser = serial.Serial("COM3", 9600, timeout=3)
        time.sleep(2)
        ser.readline()
        linha = ser.readline().decode("utf-8").strip()
        ser.close()
        partes = linha.split(",")
        if len(partes) == 4:
            raw = int(partes[1])
            incidencia = round(100 - (raw / 1023.0) * 100, 1)
            print(f"\nIncidência solar captada: {incidencia}%")
            return incidencia
        
    except Exception as e:
        print(f"\nErro ao ler LDR: {e}")
    
    return pedir_float("\nInforme a incidência solar manualmente (0-100): ")

def pedir_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("\n\033[1;31mInforme um valor numérico válido!\033[m")

def cadastrar_orcamento(escolha):
    if escolha == 1:
        os.system("cls")
        while True:
            cpf_cnpj_orcamento = input("\nQual o CPF/CPNJ do orçamento: ")
            cpf_cnpj_orcamento = cpf_cnpj_orcamento.replace("/", "").replace(".", "").replace("-","")
            if not cpf_cnpj_orcamento.isdigit() or (len(cpf_cnpj_orcamento) != 11 and len(cpf_cnpj_orcamento) != 14):
                print("\nCPF/CNPJ inválido.")
                continue
            else:
                if len(cpf_cnpj_orcamento) == 11:
                    cpf_cnpj_final = cpf_cnpj_orcamento[0:3] + "." + cpf_cnpj_orcamento[3:6] + "." + cpf_cnpj_orcamento[6:9] + "-" + cpf_cnpj_orcamento[9:11]
                    break
                else:
                    cpf_cnpj_final = cpf_cnpj_orcamento[0:2] + "." + cpf_cnpj_orcamento[2:5] + "." + cpf_cnpj_orcamento[5:8] + "/" + cpf_cnpj_orcamento[8:12] + "-" + cpf_cnpj_orcamento[12:14]
                    break

        marca_modulo = input("\nInforme a marca dos módulos: ").lower()
        modelo_modulo = input("\nQual o modelo do módulo: ").lower()
        marca_inversor = input("\nInforme a marca dos inversores: ").lower()
        modelo_inversor = input("\nQual o modelo do inversor: ").lower()
        potencia_kwp = pedir_float("\nQual a potência em KWP: ")
        geracao_anual = pedir_float("\nQual a geração anual prometida: ")
        preco_total = pedir_float("\nQual o preço total em R$")
        payback = pedir_float("\nQual o payback prometido: ")
        cidade = input("\nQual a cidade do orçamento: ").capitalize()
        incidencia_solar = ler_ldr()

        
    arquivo_existe = os.path.exists("data/orcamentos.csv")

    with open("data/orcamentos.csv", "a", newline = "", encoding = "utf-8") as arquivo:
        if not arquivo_existe:
            arquivo.write("cpf_cnpj_orcamento,marca_modulo,modelo_modulo,marca_inversor,modelo_inversor,potencia_kwp,geracao_anual,preco_total,payback,cidade,incidencia_solar\n")
        arquivo.write(f"{cpf_cnpj_final},{marca_modulo},{modelo_modulo},{marca_inversor},{modelo_inversor},{potencia_kwp},{geracao_anual},{preco_total},{payback},{cidade},{incidencia_solar}\n")

def verificar_orcamentos(escolha):
    if escolha == 2:
        os.system("cls")
        while True:
            cpf_cnpj_verificacao = input("\nInforme o CPF/CNPJ do orçamento que deseja vizualizar: ")
            cpf_cnpj_verificacao = cpf_cnpj_verificacao.replace("/", "").replace(".", "").replace("-", "")
            if not cpf_cnpj_verificacao.isdigit() or (len(cpf_cnpj_verificacao) != 11 and len(cpf_cnpj_verificacao) != 14):
                print("\nCPF/CNPJ inválido.")
                continue
            else:
                if len(cpf_cnpj_verificacao) == 11:
                    cpf_cnpj_verificacao = cpf_cnpj_verificacao[0:3] + "." + cpf_cnpj_verificacao[3:6] + "." + cpf_cnpj_verificacao[6:9] + "-" + cpf_cnpj_verificacao[9:11]
                else:
                    cpf_cnpj_verificacao = cpf_cnpj_verificacao[0:2] + "." + cpf_cnpj_verificacao[2:5] + "." + cpf_cnpj_verificacao[5:8] + "/" + cpf_cnpj_verificacao[8:12] + "-" + cpf_cnpj_verificacao[12:14]
                break

        with open("data/orcamentos.csv", "r", encoding = "utf-8") as arquivo:
            linhas = arquivo.readlines()

        orcamento_encontrado = []

        for linha in linhas:
            campos = linha.split(",")
            if cpf_cnpj_verificacao  == campos[0]:
                orcamento_encontrado.append(campos)
                

        if len(orcamento_encontrado) == 0:
            print("\nNenhum orçamento foi encontrado.")
            
        elif len(orcamento_encontrado) == 1:
                campos = orcamento_encontrado[0]
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
            
        else:
            print(f"\n{'=' * 40}")
            print(f"  {len(orcamento_encontrado)} orçamentos encontrados")
            print(f"{'=' * 40}")
            for i, campos in enumerate(orcamento_encontrado, start=1):
                    print(f"\n  [{i}] ORÇAMENTO")
                    print(f"      Módulo:       {campos[1]} - {campos[2]}")
                    print(f"      Inversor:     {campos[3]} - {campos[4]}")
                    print(f"      Potência:     {campos[5]} kWp")
                    print(f"      Geração:      {campos[6]} MWh/ano")
                    print(f"      Preço total:  R$ {campos[7]}")
                    print(f"      Payback:      {campos[8]} anos")
                    print(f"      Cidade:       {campos[9]}")
                    print(f"  {'-' * 38}")

def atualizar_orcamento(escolha):
    if escolha == 3:
        os.system("cls")
        while True:
            cpf_cnpj_verificacao = input("\nInforme o CPF/CNPJ do orçamento que deseja vizualizar: ")
            cpf_cnpj_verificacao = cpf_cnpj_verificacao.replace("/", "").replace(".", "").replace("-", "")
            if not cpf_cnpj_verificacao.isdigit() or (len(cpf_cnpj_verificacao) != 11 and len(cpf_cnpj_verificacao) != 14):
                print("\nCPF/CNPJ inválido.")
                continue
            else:
                if len(cpf_cnpj_verificacao) == 11:
                    cpf_cnpj_verificacao = cpf_cnpj_verificacao[0:3] + "." + cpf_cnpj_verificacao[3:6] + "." + cpf_cnpj_verificacao[6:9] + "-" + cpf_cnpj_verificacao[9:11]
                else:
                    cpf_cnpj_verificacao = cpf_cnpj_verificacao[0:2] + "." + cpf_cnpj_verificacao[2:5] + "." + cpf_cnpj_verificacao[5:8] + "/" + cpf_cnpj_verificacao[8:12] + "-" + cpf_cnpj_verificacao[12:14]
                break

        with open("data/orcamentos.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        linhas_novas = []

        def pedir_float_enter(mensagem, atual):
            while True:
                entrada = input(mensagem)

                if entrada == "":
                    return atual

                try:
                    return str(float(entrada))

                except ValueError:
                    print("\nInforme um valor numérico válido!")

        orcamentos_encontrados = []
        indices_encontrados = []

        for i, linha in enumerate(linhas):
            campos = linha.strip().split(",")
            if campos[0] == cpf_cnpj_verificacao:
                orcamentos_encontrados.append(campos)
                indices_encontrados.append(i)

        if len(orcamentos_encontrados) == 0:
            print("\nOrçamento não encontrado.")
            return

        if len(orcamentos_encontrados) > 1:
            print(f"\n{len(orcamentos_encontrados)} orçamentos encontrados para {cpf_cnpj_verificacao}:")
            for i, campos in enumerate(orcamentos_encontrados, start=1):
                print(f"\n  [{i}] Módulo: {campos[1]} - {campos[2]} | Inversor: {campos[3]} - {campos[4]} | Cidade: {campos[9].strip()}")
            while True:
                try:
                    escolha_idx = int(input(f"\nDigite o número do orçamento que deseja atualizar (1-{len(orcamentos_encontrados)}): "))
                    if 1 <= escolha_idx <= len(orcamentos_encontrados):
                        break
                    print(f"\nEscolha inválida.")
                except ValueError:
                    print("\nDigite um número válido.")
            escolha_idx -= 1
        else:
            escolha_idx = 0

        campos = orcamentos_encontrados[escolha_idx]
        encontrado = True

        print(f"\nOrçamento {cpf_cnpj_verificacao} encontrado!")
        print("Para manter o valor atual, deixe o campo em branco.\n")

        marca_modulo = input(f"Marca dos módulos [{campos[1]}]: ").lower() or campos[1]
        modelo_modulo = input(f"Modelo dos módulos [{campos[2]}]: ").lower() or campos[2]
        marca_inversor = input(f"Marca do inversor [{campos[3]}]: ").lower() or campos[3]
        modelo_inversor = input(f"Modelo do inversor [{campos[4]}]: ").lower() or campos[4]
        potencia_kwp = pedir_float_enter(f"Potência em KWP [{campos[5]}]: ",campos[5])
        geracao_anual = pedir_float_enter(f"Geração anual [{campos[6]}]: ",campos[6])
        preco_total = pedir_float_enter(f"Preço total R$ [{campos[7]}]: ",campos[7])
        payback = pedir_float_enter(f"Payback [{campos[8]}]: ",campos[8])
        cidade = input(f"Cidade [{campos[9].strip()}]: ").capitalize() or campos[9].strip()
        incidencia_solar = pedir_float_enter(f"Incidência solar [{campos[10].strip()}]: ", campos[10].strip())


        nova_linha = (f"{cpf_cnpj_verificacao},{marca_modulo},{modelo_modulo},{marca_inversor},{modelo_inversor},{potencia_kwp},{geracao_anual},{preco_total},{payback},{cidade},{incidencia_solar}\n")
        linhas[indices_encontrados[escolha_idx]] = nova_linha
        linhas_novas = linhas

        if not encontrado:
            print("\nOrçamento não encontrado.")
            return

        with open("data/orcamentos.csv", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas_novas)

        print(f"Orçamento {cpf_cnpj_verificacao} atualizado com sucesso!")

def excluir_orcamento(escolha):
    if escolha == 4:
        os.system("cls")

        while True:
            cpf_cnpj_verificacao = input("\nInforme o CPF/CNPJ do orçamento que deseja vizualizar: ")
            cpf_cnpj_verificacao = cpf_cnpj_verificacao.replace("/", "").replace(".", "").replace("-", "")
            if not cpf_cnpj_verificacao.isdigit() or (len(cpf_cnpj_verificacao) != 11 and len(cpf_cnpj_verificacao) != 14):
                print("\nCPF/CNPJ inválido.")
                continue
            else:
                if len(cpf_cnpj_verificacao) == 11:
                    cpf_cnpj_verificacao = cpf_cnpj_verificacao[0:3] + "." + cpf_cnpj_verificacao[3:6] + "." + cpf_cnpj_verificacao[6:9] + "-" + cpf_cnpj_verificacao[9:11]
                else:
                    cpf_cnpj_verificacao = cpf_cnpj_verificacao[0:2] + "." + cpf_cnpj_verificacao[2:5] + "." + cpf_cnpj_verificacao[5:8] + "/" + cpf_cnpj_verificacao[8:12] + "-" + cpf_cnpj_verificacao[12:14]
                break

        with open("data/orcamentos.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        orcamentos_encontrados = []
        indices_encontrados = []

        for i, linha in enumerate(linhas):
            campos = linha.strip().split(",")
            if campos[0] == cpf_cnpj_verificacao:
                orcamentos_encontrados.append(campos)
                indices_encontrados.append(i)

        if len(orcamentos_encontrados) == 0:
            print("Orçamento não encontrado.")
            return

        if len(orcamentos_encontrados) > 1:
            print(f"\n{len(orcamentos_encontrados)} orçamentos encontrados para {cpf_cnpj_verificacao}:")
            for i, campos in enumerate(orcamentos_encontrados, start=1):
                print(f"\n  [{i}] Módulo: {campos[1]} - {campos[2]} | Inversor: {campos[3]} - {campos[4]} | Cidade: {campos[9].strip()}")
            while True:
                try:
                    escolha_idx = int(input(f"\nDigite o número do orçamento que deseja deletar (1-{len(orcamentos_encontrados)}): "))
                    if 1 <= escolha_idx <= len(orcamentos_encontrados):
                        break
                    print(f"\nEscolha inválida.")
                except ValueError:
                    print("\nDigite um número válido.")
            escolha_idx -= 1
        else:
            escolha_idx = 0

        confirmacao = input(f"\nTem certeza que deseja deletar o orçamento {cpf_cnpj_verificacao}? (s/n): ").lower()
        if confirmacao != "s":
            print("\nOperação cancelada.")
            return

        linhas.pop(indices_encontrados[escolha_idx])
        linhas_novas = linhas

        with open("data/orcamentos.csv", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas_novas)

        print(f"Orçamento {cpf_cnpj_verificacao} deletado com sucesso!")

def score_orcamento(escolha):
    if escolha == 5:
        TARIFA = 0.83
        PRECO_MEDIO_KWP = 4500
        GERACAO_ESPERADA_KWP = 960

        os.system("cls")
        while True:
            cpf_cnpj = input("\nInforme o CPF/CNPJ do orçamento: ")
            cpf_cnpj = cpf_cnpj.replace("/", "").replace(".", "").replace("-", "")

            if not cpf_cnpj.isdigit() or (len(cpf_cnpj) != 11 and len(cpf_cnpj) != 14):
                print("\nCPF/CNPJ inválido.")
                continue
            else:
                if len(cpf_cnpj) == 11:
                    cpf_cnpj = cpf_cnpj[0:3] + "." + cpf_cnpj[3:6] + "." + cpf_cnpj[6:9] + "-" + cpf_cnpj[9:11]
                else:
                    cpf_cnpj = cpf_cnpj[0:2] + "." + cpf_cnpj[2:5] + "." + cpf_cnpj[5:8] + "/" + cpf_cnpj[8:12] + "-" + cpf_cnpj[12:14]
                break

        with open("data/orcamentos.csv", "r", encoding = "utf-8") as arquivo:

            linhas = arquivo.readlines()
            orcamentos_encontrados = []

            for linha in linhas:
                campos = linha.strip().split(",")
                if cpf_cnpj == campos[0]:
                    orcamentos_encontrados.append(campos)

            if len(orcamentos_encontrados) == 0:
                print("Nenhum orçamento encontrado nesse CPF.")
                return
            
            elif len(orcamentos_encontrados) > 1:
                print(f"\n{len(orcamentos_encontrados)} orçamentos encontrados:")
                for i, campos in enumerate(orcamentos_encontrados, start=1):
                    print(f"\n  [{i}] Módulo: {campos[1]} - {campos[2]} | Cidade: {campos[9].strip()}")
                    while True:
                        try:
                            idx = int(input(f"\nEscolha o orçamento (1-{len(orcamentos_encontrados)}): "))
                            if 1 <= idx <= len(orcamentos_encontrados):
                                break
                            print("\nEscolha inválida.")

                        except ValueError:
                            print("\nDigite um número válido.")

                campos = orcamentos_encontrados[idx - 1]  
            else:
                campos = orcamentos_encontrados[0]
            
            payback_prometido = float(campos[8])
            potencia = float(campos[5])
            geracao = float(campos[6])
            preco = float(campos[7])
            incidencia = float(campos[10].strip())

            economia_anual = geracao * TARIFA
            payback_real   = round(preco / economia_anual, 1)

            if payback_real <= 4:
                pts_payback = 30
                label_payback = "Excelente"
                icone_payback = "\033[1;32m✓\033[m"
            elif payback_real <= 6:
                pts_payback = 22
                label_payback = "Muito bom"
                icone_payback = "\033[1;32m✓\033[m"
            elif payback_real <= 8:
                pts_payback = 14
                label_payback = "Aceitável"
                icone_payback = "\033[1;33m~\033[m"
            else:
                pts_payback = 5
                label_payback = "Alto"
                icone_payback = "\033[1;31m✗\033[m"

            if incidencia >= 70:
                pts_incidencia = 30
                label_incidencia = "Alta"
                icone_incidencia = "\033[1;32m✓\033[m"
            elif incidencia >= 40:
                pts_incidencia = 18
                label_incidencia = "Média"
                icone_incidencia = "\033[1;33m~\033[m"
            else:
                pts_incidencia = 5
                label_incidencia = "Baixa"
                icone_incidencia = "\033[1;31m✗\033[m"

            preco_esperado = potencia * PRECO_MEDIO_KWP
            diferenca_preco = ((preco - preco_esperado) / preco_esperado) * 100

            if diferenca_preco <= -10:
                pts_preco = 20
                label_preco = "Ótimo preço"
                icone_preco = "\033[1;32m✓\033[m"
            elif diferenca_preco <= 10:
                pts_preco = 14
                label_preco = "Preço justo"
                icone_preco = "\033[1;32m✓\033[m"
            elif diferenca_preco <= 25:
                pts_preco = 7
                label_preco = "Acima da média"
                icone_preco = "\033[1;33m~\033[m"
            else:
                pts_preco = 2
                label_preco = "Preço alto"
                icone_preco = "\033[1;31m✗\033[m"

            geracao_esperada = round(potencia * GERACAO_ESPERADA_KWP, 1)
            diferenca_geracao = ((geracao - geracao_esperada) / geracao_esperada) * 100

            if diferenca_geracao >= 10:
                pts_geracao = 20
                label_geracao = "Acima do esperado"
                icone_geracao = "\033[1;32m✓\033[m"
            elif diferenca_geracao >= -10:
                pts_geracao = 14
                label_geracao = "Dentro do esperado"
                icone_geracao = "\033[1;32m✓\033[m"
            elif diferenca_geracao >= -25:
                pts_geracao = 7
                label_geracao = "Abaixo do esperado"
                icone_geracao = "\033[1;33m~\033[m"
            else:
                pts_geracao = 2
                label_geracao = "Muito abaixo"
                icone_geracao = "\033[1;31m✗\033[m"

            score = pts_payback + pts_incidencia + pts_preco + pts_geracao

            if score >= 85:
                classificacao = "\033[1;32mAltamente recomendado\033[m"
                emoji = "🟢"
            elif score >= 65:
                classificacao = "\033[1;32mBom\033[m"
                emoji = "🟡"
            elif score >= 40:
                classificacao = "\033[1;33mRegular\033[m"
                emoji = "🟠"
            else:
                classificacao = "\033[1;31mRuim\033[m"
                emoji = "🔴"

            print("\n" + "═" * 40)
            print("           SCORE EASYSUN")
            print("═" * 40)

            print(f"\n  Payback real:     {payback_real} anos  (+{pts_payback}pts)")
            print(f"  {icone_payback} {label_payback}")
            print(f"     Prometido: {payback_prometido} anos | Calculado: {payback_real} anos")

            if payback_real < payback_prometido:
                diff = round(payback_prometido - payback_real, 1)
                print(f"  \033[1;32m✓ Empresa foi conservadora — paga {diff} anos antes!\033[m")
            elif payback_real == payback_prometido:
                print(f"  \033[1;33m~ Payback exatamente como prometido.\033[m")
            else:
                diff = round(payback_real - payback_prometido, 1)
                print(f"  \033[1;31m✗ Atenção! Payback {diff} anos maior que o prometido.\033[m")

            print(f"\n  Incidência solar: {incidencia}%  (+{pts_incidencia}pts)")
            print(f"  {icone_incidencia} {label_incidencia}")

            print(f"\n  Preço total:      R$ {preco}  (+{pts_preco}pts)")
            print(f"  {icone_preco} {label_preco}")
            print(f"     Referência: R$ {preco_esperado:.0f} ({potencia} kWp × R$ {PRECO_MEDIO_KWP})")

            print(f"\n  Geração anual:    {geracao} kWh  (+{pts_geracao}pts)")
            print(f"  {icone_geracao} {label_geracao}")
            print(f"     Esperado: {geracao_esperada} kWh ({potencia} kWp × {GERACAO_ESPERADA_KWP} kWh/kWp)")

            print("\n" + "─" * 40)
            print(f"  SCORE FINAL: {score}/100")
            print(f"\n  {emoji} {classificacao}")
            print("═" * 40)