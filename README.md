🧠 Automação de Cadastro de Produtos com Python

Este projeto realiza a automação do cadastro de produtos em um sistema web utilizando Python e a biblioteca pyautogui. Ele simula ações humanas como abrir o navegador, preencher formulários e interagir com a interface gráfica.

📦 Instalação
Para rodar este projeto localmente, siga os passos abaixo:

bash

# Clone o repositório
```
git clone https://github.com/DiogoMarcondes03/py_automation_fill_products.git
```
# Acesse a pasta do projeto
```
cd py_automation_fill_products
```
# Instale as dependências
```
pip install pyautogui pandas
```
💡 Certifique-se de que o arquivo produtos.csv esteja na mesma pasta do script.

🚀 Passo a passo da automação
🔹 1. Abrir o navegador e acessar o sistema
O script inicia o navegador Google Chrome e acessa a URL de login:

Code
https://dlp.hashtagtreinamentos.com/python/intensivao/login
🔹 2. Realizar login
Preenche os campos de e-mail e senha e clica no botão de login usando coordenadas da tela.

🔹 3. Importar a base de produtos
Carrega o arquivo produtos.csv com os dados que serão cadastrados no sistema.

🔹 4. Cadastrar os produtos
Para cada linha da tabela:

Preenche os campos do formulário com os dados do produto.

Envia o formulário.

Faz scroll para garantir que o próximo produto possa ser visualizado.

🔹 5. Repetir o processo
O loop continua até que todos os produtos da base sejam cadastrados.

📁 Estrutura esperada do arquivo produtos.csv
Coluna	Descrição
codigo	Código do produto
marca	Marca do produto
tipo	Tipo ou modelo
categoria	Categoria do produto
preco_unitario	Preço unitário
custo	Custo de aquisição
obs	Observações (opcional)
⚠️ Observações importantes
As coordenadas de clique (x, y) são específicas para a resolução de tela usada durante o desenvolvimento. Podem precisar de ajustes em outras máquinas.

O sistema deve estar visível e acessível na tela antes de executar o script.

Evite interagir com o mouse ou teclado durante a execução da automação.
