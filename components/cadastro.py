produtos = []; ## array para armazenar valores dos produtos


##Função para cadastrar produtos
def cadastros(identificador, nome, preco, estoque):
        
        ##Produtos e valores
        produto = {
        "id": identificador,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
        }
        ## Adicionando valores ao array
        produtos.append(produto)
        return produtos