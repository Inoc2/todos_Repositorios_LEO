def cadastro_usuario():
    while True:
        nome = input('Insira o nome a ser cadastrado. Insira "0" para cancelar.\n').capitalize().strip()
        if nome == "0":
            break
        elif not nome.replace(" ", "").isalpha():
            print("Insira apenas caracteres do alfabeto e espaços. Tente novamente.")
            continue
        
        while True:    
            idade = input(f'Insira a idade do {nome}.\n')
            try:
                idade = int(idade)
            except ValueError:
                print("Foi inserido uma idade inválida. Tente novamente.")
                continue
            
            if not 0 <= idade <= 150:
                print('O intervalo da idade inserida é inválido (entre 0 e 150). Tente novamente.')
                continue    
            break
        
        while True:
            sexo = input(f'Insira o sexo do {nome} (M/F).\n').upper()
            if sexo[0] not in "MF":
                print('Você inseriu um sexo inválido. Tente novamente')
                continue
            sexo = sexo[0]
            break
            
        while True:
            telefone_inserido_pelo_usuario = input(f'Insira o telefone do {nome}.\n')
            telefone_valido_usuario = ""
            for character in telefone_inserido_pelo_usuario:
                if character in "0123456789":
                    telefone_valido_usuario += character
            if len(telefone_valido_usuario) < 8:
                print("Insira um número de telefone válido com pelo menos 8 caracteres.") 
                continue
            break
                                 
        with open('p1_list_usuarios_cadastrados.txt', 'a', encoding='utf-8') as pasta_usuarios:
            pasta_usuarios.write(f'{nome} | {idade} | {sexo} | {telefone_valido_usuario}\n')
            print(f'O/A {nome} foi cadastrado(a).')

cadastro_usuario()


