# Dicionário global para armazenar os usuários
banco_usuarios = []

# Função para cadastrar um usuário com campos obrigatórios e opcionais
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}

    # Solicitar dados para os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor

    # Solicitar dados para campos opcionais até que o usuário digite "sair"
    while True:
        campo = input("Digite um campo opcional ou 'sair' para encerrar: ")
        if campo.lower() == 'sair':
            break
        valor = input(f"Digite o valor para '{campo}': ")
        usuario[campo] = valor

    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para imprimir usuários com várias opções
def imprimir_usuarios(*args, **kwargs):
    opcao = int(input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\n"))

    if opcao == 1:
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == 2:
        nomes = args
        for nome in nomes:
            for usuario in banco_usuarios:
                if usuario.get("nome") == nome:
                    print(usuario)
    elif opcao == 3:
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(usuario)
    elif opcao == 4:
        nomes = args
        campos = kwargs.keys()
        for nome in nomes:
            for usuario in banco_usuarios:
                if usuario.get("nome") == nome and all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                    print(usuario)
    else:
        print("Opção inválida.")

# Função principal
def main():
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(",")
    
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == "2":
            imprimir_usuarios()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
