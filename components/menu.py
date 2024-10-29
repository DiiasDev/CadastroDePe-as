## Coletando dados para adicionar aos valores do array
def dados():
    identificador = int(input("Entre com o ID do produto: "))
    nome = input("Entre com o nome do produto: ")
    preco = float(input("Entre com o preço do produto: "))
    estoque = int(input("Quantidade de estoque do produto: "))
    return identificador,nome,preco,estoque

print("Seja bem vindo ao cadastros Dias !!")

##opção de continuar ou parar
def opcoes():
    opcao = input("1- Adicionar\n2- Parar\n")
    return opcao  # Retorna a opção selecionada
      