# ☀️ EasySun — Solar Truth Analyzer

> **Descubra a verdade sobre seu orçamento solar.**

EasySun é uma plataforma que permite ao consumidor analisar orçamentos de energia solar recebidos de empresas instaladoras, identificando se o payback prometido é real, se os componentes são de qualidade e se o preço é justo — com base em dados técnicos reais.

---

## 🚀 Funcionalidades

- **📄 Upload de Orçamentos em PDF** — Envie o orçamento recebido e permita que a IA extraia automaticamente as informações relevantes.
- **✍️ Preenchimento Manual** — Insira os dados do orçamento por meio de um formulário simples e intuitivo.
- **🤖 Análise Inteligente** — Avaliação técnica dos equipamentos, estimativa de geração energética e cálculo do payback real do sistema.
- **🔌 Simulação de Incidência Solar** — Leitura de luminosidade em tempo real via Arduino + sensor LDR, capturada no momento do cadastro.

---

## 🛠️ Tecnologias Utilizadas

| Camada           | Tecnologia        |
|------------------|-------------------|
| Backend / Lógica | Python            |
| Armazenamento    | CSV               |
| Hardware         | Arduino UNO + LDR |
| Versionamento    | Git + GitHub      |

---

## 📁 Estrutura do Projeto (CRUD)

```
easysun-crud/
├── data/
│   └── orcamentos.csv       # Armazenamento dos orçamentos cadastrados
├── src/                     # Módulos e funções do sistema
├── main.py                  # Ponto de entrada e menu principal
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔌 Integração com Arduino + Sensor LDR

O EasySun conta com uma camada de simulação de incidência solar utilizando hardware físico.

### Como funciona

- Um **sensor LDR** conectado a um **Arduino UNO** realiza leituras de luminosidade ambiente.
- O Arduino transmite os dados via **comunicação serial (USB)** para o computador.
- O Python captura o valor no momento do **cadastro de um orçamento** e o armazena no CSV, simulando a incidência solar no local do cliente.

### Componentes necessários

| Componente  | Descrição                        |
|-------------|----------------------------------|
| Arduino UNO | Microcontrolador principal       |
| Sensor LDR  | Leitura de luminosidade ambiente |
| Cabo USB    | Comunicação serial com o PC      |

---

## ▶️ Como Executar

**Pré-requisitos:** Python 3.x instalado e Arduino UNO conectado via USB na porta **COM3**.

```bash
# Clone o repositório
git clone https://github.com/projeto-G3/projeto-easysun.git

# Acesse a pasta do projeto
cd projeto-easysun

# Execute o programa
python main.py
```

> Ao cadastrar um orçamento, a leitura de luminosidade será capturada automaticamente pelo sensor LDR e salva no CSV.

---

## 🌞 Nossa Missão

Democratizar o acesso à informação no mercado de energia solar, ajudando consumidores a investirem com mais confiança, transparência e segurança.

---

## 👥 Equipe — Grupo G3

| Nome              |
|-------------------|
| Adriano Filho     |
| Mateus Aguiar     |
| João Gabriel      |
| Cecília de Moraes |
| Suri Savitri      |
| Sofia Drunen      |

---

*Projeto desenvolvido para a disciplina Projeto-1 — CESAR School.