# 🖥️ Automação de Inserção de Dados via PyAutoGUI

Este projeto utiliza **Python**, **Pandas** e **PyAutoGUI** para automatizar o preenchimento de formulários em uma página web específica. Ele faz a leitura de dados de um arquivo CSV, insere as informações automaticamente nos campos apropriados e realiza a submissão do formulário.

## 🚀 Funcionalidades

- 🌐 **Acessa automaticamente um site de login pré-definido.**
- 🔑 **Faz o login usando credenciais fornecidas no script.**
- 📋 **Lê um arquivo CSV contendo os dados a serem inseridos.**
- ✍️ **Preenche automaticamente os campos de formulário com base no arquivo CSV.**

## 📋 Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- **Python 3.8+**
- Pacotes Python necessários:
  ```bash
  pip install pyautogui pandas

## 🧑‍💻 Como usar
Clone este repositório em sua máquina local:

```bash
git clone https://github.com/DiogoMarcondes03/py_form_automation.git
cd py_form_automation
```
Certifique-se de que o arquivo produtos.csv está no mesmo diretório do script. Ele deve ter o seguinte formato:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
1234,Marca1,Tipo1,Categoria1,100.00,90.00,Observação1
5678,Marca2,Tipo2,Categoria2,200.00,180.00,Observação2
```
Execute o script no terminal:

```bash
python nome_do_arquivo.py
```

O script abrirá o navegador, fará o login no site e preencherá os formulários automaticamente com os dados fornecidos no arquivo CSV.

## ⚠️ Avisos
Uso Responsável: Certifique-se de que você tem permissão para automatizar tarefas no site em questão.

## Credenciais: Lembre-se de alterar as credenciais (e-mail e senha) no script para garantir segurança.

📈 Próximos passos
🔄 Melhorar a dinâmica do script para capturar elementos baseados em seletores mais robustos (ex.: XPath dinâmicos).

⏱️ Adicionar funcionalidade para agendar a execução automática em intervalos regulares.
