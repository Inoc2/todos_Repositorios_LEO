def cadastro_usuario():
    while True:
        nome = input('Insira o nome a ser cadastrado. Insira "0" para cancelar.\n').capitalize()
        if nome == "0":
            break
        idade = int(input(f'Insira a idade do {nome}.\n'))
        if not 0 <= idade <= 150:
            print('Você inseriu uma idade inválida. Tente novamente')
            continue
        sexo = input(f'Insira o sexo do {nome} (M/F).\n')
        if sexo not in "MmFf":
            print('Você inseriu um sexo inválido. Tente novamente')
            continue
        telefone = input(f'Insira o telefone do {nome}.\n')

        with open('usuarios_cadastrados.txt', 'a', encoding='utf-8') as pasta_usuarios:
            pasta_usuarios.write(f'{nome} | {idade} | {sexo} | {telefone}\n')
            print(f'O/A {nome} foi cadastrado(a).')

cadastro_usuario()


