# Projeto para criar cadastro de peças para uma empresa imaginária

# Importando componentes 
from components import cadastro
from components import menu

##Criando função para executar o cadastro de produtos
def main():
    #loop para adicionar mais de um produto
    while True:
        opcao = menu.opcoes()  # Obtém a opção do menu
        if opcao == "1":  # Adicionar produto
            identificador, nome, preco, estoque = menu.dados()  # Coleta os dados do produto
            cadastro.cadastros(identificador, nome, preco, estoque)
            print("Produto adicionado com sucesso!")
        elif opcao == "2":  # Parar
            resultado = "\n".join(f"{prod['nome']} (ID: {prod['id']}, Preço: R${prod['preco']}, Estoque: {prod['estoque']})" for prod in cadastro.produtos)
            print(f"Produtos cadastrados:\n{resultado}" )  # Exibe a lista de produtos antes de sair
            print("Saindo do programa.")
            break  # Encerra o loop
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()  # Chama a função principal
