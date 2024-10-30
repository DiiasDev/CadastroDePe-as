import criar_arquivo
import editar

op = input("Selecione a opção:\n1- Criar arquivo\n2- Editar arquivo\n")

if op == "1":
    criar_arquivo.criar()
elif op == "2":
    editar.edita()
else:
    print("Opção inválida")
