SEPARADOR = "-" * 35
MENSAGEM_ERRO_BUSCA = "\n>> Produto não encontrado. <<"
MENSAGEM_ERRO_NUMERO = "\n>> Digite um número válido. <<"
MENSAGEM_SUCESSO = "\n>> Operação realizada com sucesso. <<"
MENSAGEM_ENTRADA_INVALIDA = "\n>> Entrada inválida, tente novamente. <<"


def cadastrar_produtos(estoque):

    """
    Cadastra um novo produto no estoque.

    Solicita a descrição, quantidade, custo e preço de venda do produto ao usuário
    e gera o código de identificação incrementando no maior código do estoque.

    parametros:
        estoque: lista de dicionários representando os produtos.
    """
    

    descricao = input("Digite a descrição do produto: ")
    maior_codigo = max(estoque, key=lambda produto: produto['codigo'])['codigo']
    novo_codigo = maior_codigo + 1
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        custo = float(input("Digite o custo do produto: "))
        preco_venda = float(input("Digite o preço de venda do produto: "))
    except ValueError:

        print(MENSAGEM_ERRO_NUMERO)
        return

    # Cria um novo produto como dicionário usando os valores informados pelo usuário
    novo_produto = {
        "descricao": descricao,
        "codigo": novo_codigo,
        "quantidade": quantidade,
        "custo": custo,
        "preco_venda": preco_venda
    }

    # Adiciona o novo produto ao estoque
    estoque.append(novo_produto)

    print(MENSAGEM_SUCESSO)
    listar_produtos([novo_produto],"PRODUTO CADASTRADO")

def inserir_estoque_inicial(estoque_string):

    """
    Convente uma string formatada em uma lista de produtos.

    parametros:
        estoque_string: String contendo os dados do estoque inicial.
                        Os produtos são separados por '#' e os atributos
                        de cada produto por ';'.

    return:
        retorna uma lista contendo os dados processados, gerando o estoque inicial.
    """

    produtos = []

    # Divide os produtos da string em uma lista
    itens_estoque = estoque_string.split("#")


    # percorre os produtos dividindo os atributos e armazina em variáveis e crie um dicionário com os atributos.
    for item in itens_estoque:
        descricao, codigo, quantidade, custo, preco_venda = item.split(";")
        produto = {
            "descricao": descricao,
            "codigo": int(codigo),
            "quantidade": int(quantidade),
            "custo": float(custo),
            "preco_venda": float(preco_venda)
        }
        produtos.append(produto)
    return produtos

def listar_produtos(estoque, titulo = "LISTA DE PRODUTOS"):

    """
    Exibe produtos no terminal, podendo ser todos ou um grupo específico dependendo da chamada.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.

        titulo: título da lista, caso não receba o título irá exibir o título padrão
    """

    # Verifica se estoque/lista está vazio
    if not estoque:
        print("O estoque está vazio.")
        return
    
    print("\n" + titulo.center(70))
    print(SEPARADOR * 2)

    # Percorre o estoque/lista exibindo cada produto
   # for produto in estoque:
    """ print(SEPARADOR)
    print(f"Descrição: {produto['descricao']}")
    print(f"Código: {produto['codigo']}")
    print(f"Quantidade em estoque: {produto['quantidade']}")
    print(f"Custo: R${produto['custo']}")
    print(f"Preço de venda: R${produto['preco_venda']}") """

    cabecalho = f"{'Descrição'.ljust(25)}{'Código'.rjust(7)}{'Qtd'.rjust(6)}{'Custo'.rjust(10)}{'Preço'.rjust(9)}"
    print(cabecalho)
    print(SEPARADOR * 2)

    for produto in estoque:
        linha = f"{produto['descricao'].ljust(25)}{str(produto['codigo']).rjust(7)}{str(produto['quantidade']).rjust(6)}{f'R${produto['custo']}'.rjust(10)}{f'R${produto['preco_venda']:.2f}'.rjust(10)}"
        
        print(linha)

def ordenar_por_quantidade(estoque):

    """
    Ordena os produtos por quantidade de forma decrescente e exibe na tela

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    lista_ordenada = sorted(estoque, key=lambda produto: int(produto['quantidade']), reverse=True)

    # Chama a função de listagem passando a lista ordenada e o título da lista
    listar_produtos(lista_ordenada, "PRODUTOS ORDENADOS POR QUANTIDADE")

def buscar_produto(estoque):

    """
    Busca um produto no estoque de acordo com o tipo de informação que o usuário informar

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    entrada = input("\nDigite o código ou uma palavra chave do produto: ")

    # Caso a entrada do usuário seja um número será convertido pra int, caso seja texto será transformado em minúsculo.
    try:
        chave = int(entrada)
    except ValueError:
        chave = entrada.lower()

    resultados = []

    # Verifica o tipo da informação inserida pelo usuário e busca no estoque.
    if isinstance(chave, int):
        for item in estoque:
            if item.get("codigo") == chave:
                resultados.append(item)

    elif isinstance(chave, str):
        resultados = list(filter(lambda produto: chave in produto.get("descricao").lower(), estoque))
        
    # Exibe os produtos encontrados, caso não encontre informa ao usuário.
    if resultados:
        listar_produtos(resultados, "RESULTADOS DA BUSCA")
    else: 
        print(MENSAGEM_ERRO_BUSCA)

def remover_produto(estoque):

    """
    Remove um produto do estoque de acordo com o código informado pelo usuário.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    print(SEPARADOR)
    try:
        codigo_remover = int(input("\nDigite o código do produto que deseja remover: "))
    except ValueError:
        print(MENSAGEM_ERRO_NUMERO)
    for produto in estoque:
        if produto["codigo"] == codigo_remover:
            estoque.remove(produto)
            print(MENSAGEM_SUCESSO)
            return
        
    print(MENSAGEM_ERRO_BUSCA)

def consultar_esgotados(estoque):

    """
    Verifica quais produtos estão esgotados e exibe na tela.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    # Cria uma nova lista apenas com os produtos esgotados.
    produtos_esgotados = list(filter(lambda produto: produto['quantidade'] == 0, estoque))

    # Caso haja produtos na lista ele chama a função de listagem.
    if produtos_esgotados:
        listar_produtos(produtos_esgotados, "PRODUTOS ESGOTADOS")
    else:
        print("\n>> Não há produtos esgotados no estoque. <<")

def filtrar_baixa_quantidade(estoque, limite = 5):

    """
    Percorre o estoque e exibe os produto que possuam quantidade igual ou menor que um limite
    padrão ou definido pelo usuário.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.

        limite: recebe um limite mínimo pra quantidade dos produtos
    """

    resposta = input("\nDeseja definir um limite manualmente? caso não o valor padrão (5) será utilizado (sim/não):")

    if resposta.lower() == "sim":
        try:
            limite = int(input("\ndigite o limite desejado: "))

        except ValueError:
            print(MENSAGEM_ERRO_NUMERO)

    elif resposta.lower() == "não":
        print("\n>> Utilizando o valor padrão... <<")

    else:
        print(MENSAGEM_ENTRADA_INVALIDA)
        return
    
    # filtra os itens da lista pelo mínimo deifinido
    baixa_quantidade = list(filter(lambda produto: produto['quantidade'] <= limite, estoque))

    listar_produtos(baixa_quantidade, f"PRODUTOS COM QUANTIDADE {limite} OU MENOS")

def atualizar_estoque(estoque):

    """
    Atualiza a quantidade de um produto, podendo aumentar ou diminuir.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    codigo_produto = int(input("\nDigite o código do produto que deseja atualizar: "))

    for produto in estoque:
        if produto['codigo'] == codigo_produto:
            resposta = input("\nDigite 1 para entrada de produtos e 2 para saída de produtos: ")
            
            # Atualiza caso a resposta seja para aumentar quantidade
            if resposta == "1":
                try:
                    quantidade_entrada = int(input("Digite a quantidade de entrada: "))
                    if quantidade_entrada > 0:
                        produto['quantidade'] += quantidade_entrada
                        print(MENSAGEM_SUCESSO)
                        listar_produtos([produto], "PRODUTO ATUALIZADO") 
                        return
                    else: 
                        print("\n>> A quantidade deve ser um número positivo. <<")
                        return
                except ValueError:
                    print(MENSAGEM_ERRO_NUMERO)
                    return
                    
            # Atualiza caso a resposta seja para diminuir a quantidade
            elif resposta == "2":
                try:
                    quantidade_saida = int(input("Digite a quantidade de saída: "))
                    if quantidade_saida > 0:
                        if produto['quantidade'] >= quantidade_saida:
                            produto['quantidade'] -= quantidade_saida

                            print(MENSAGEM_SUCESSO)
                            listar_produtos([produto], "PRODUTO ATUALIZADO")
                            return 
                        else:
                            print(f"\n>> Erro: Quantidade em estoque insuficiente. ({produto['quantidade']}) <<")
                            return
                    else:
                        print("\n>> A quantidade deve ser um número positivo. <<")
                        return
                except ValueError:
                    print(MENSAGEM_ERRO_NUMERO)
                    return
            else:
                print(MENSAGEM_ENTRADA_INVALIDA)
                return
    print(MENSAGEM_ERRO_BUSCA)

def atualizar_preco(estoque):

    """
    Atualiza o preço de um produto especificado através do código.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    codigo_produto = int(input("\nDigite o código do produto que deseja atualizar: "))

    for produto in estoque:
        if produto['codigo'] == codigo_produto:
            try:
                novo_preco = float(input("\nDigite o novo preço do produto: "))
                if novo_preco > 0:
                    if novo_preco > produto['custo']:
                        produto['preco_venda'] = novo_preco
                        print(MENSAGEM_SUCESSO)
                        listar_produtos([produto], "PRODUTO ATUALIZADO")
                    else:
                        print("\n>> O preço deve ser maior que o custo do produto. <<")
                else:
                    print("\n>> O valor deve ser maior que zero. <<")
            except ValueError:
                print(MENSAGEM_ERRO_NUMERO)

def calcular_total_estoque(estoque, exibir_valor = True):

    """
    Calcula o valor total de todos os produtos do estoque, multiplicando pela quantidade de cada um

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.

        exibir_valor: Recebe um valor booleano que indica se o programa deve exibir o total na tela ou não
                      para fim de reutilização da função.
    """

    # Multiplica o preço do produto pela sua quantidade e soma todos os produtos
    total = sum(produto['preco_venda'] * produto['quantidade'] for produto in estoque)

    if exibir_valor:
        print(f"\n>> O valor total do estoque é R${total} <<")

    return total

def calcular_lucro(estoque):

    """
    Calcula o lucro dos produtos, subtraindo o faturamento total pelo custo dos produtos.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    total_custo = sum(produto['custo'] * produto['quantidade'] for produto in estoque)
    total_preco = calcular_total_estoque(estoque, False)
    lucro = total_preco - total_custo

    print(f"\n>> O lucro presumido do estoque é R${lucro} <<")

def relatorio_geral(estoque):

    """
    cria um relatório com todos os produtos e calcula os custo total e o faturamento dos produtos.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    separador_relatorio = "-" * 70

    print(separador_relatorio)
    print("RELATÓRIO GERAL DO ESTOQUE".center(70))
    print(separador_relatorio)

    cabecalho = f"{'Descrição'.ljust(25)}{'Código'.rjust(7)}{'Qtd'.rjust(6)}{'Custo'.rjust(10)}{'Preço'.rjust(9)}{'Soma total'.rjust(12)}"
    print(cabecalho)
    print(separador_relatorio)

    custo_total = 0
    faturamento_total = 0

    for produto in estoque:
        total_produto = produto['quantidade'] * produto['preco_venda']
        custo_total += produto['quantidade'] * produto['custo']
        faturamento_total += total_produto

        linha = f"{produto['descricao'].ljust(25)}{str(produto['codigo']).rjust(7)}{str(produto['quantidade']).rjust(6)}{f'R${produto['custo']}'.rjust(10)}{f'R${produto['preco_venda']:.2f}'.rjust(10)}{f'R${total_produto:.2f}'.rjust(12)}"
        
        print(linha)

    print(separador_relatorio)
    print(f"{'Custo total do estoque:'.ljust(52)}R${custo_total}")
    print(f"{'Fatutamento total do estoque:'. ljust(52)}R${faturamento_total}")
    print(separador_relatorio)

def menu(estoque):

    """
    Cria um menu para a chamada de cada função.

    parametros:
        estoque: recebe uma lista contendo um ou mais produtos a serem exibidos.
    """

    while True:
        print(SEPARADOR)
        print("MENU DE OPERAÇÕES")
        print(SEPARADOR)
        print("1 - Cadastrar produtos")
        print("2 - Listar produtos")
        print("3 - Listar ordenando por quantidade")
        print("4 - Buscar um produto")
        print("5 - Remover um produto")
        print("6 - Consultar produtos esgotados")
        print("7 - filtrar por quantidade mínima")
        print("8 - atualizar quantidade de um produto")
        print("9 - atualizar preço de um produto")
        print("10 - Calcular preço total do estoque")
        print("11 - Calcular lucro do estoque")
        print("12 - Relatório geral do estoque")
        print("0 - Sair")

        operacao = input("\nDigite o número da operação desejada: ")


        if operacao == '1':
            cadastrar_produtos(estoque)
        elif operacao == '2':
            listar_produtos(estoque)
        elif operacao == '3':
            ordenar_por_quantidade(estoque)
        elif operacao == '4':
            buscar_produto(estoque)
        elif operacao == '5':
            remover_produto(estoque)
        elif operacao == '6':
            consultar_esgotados(estoque)
        elif operacao == '7':
            filtrar_baixa_quantidade(estoque)
        elif operacao == '8':
            atualizar_estoque(estoque)
        elif operacao == '9':
            atualizar_preco(estoque)
        elif operacao == '10':
            calcular_total_estoque(estoque)
        elif operacao == '11':
            calcular_lucro(estoque)
        elif operacao == '12':
            relatorio_geral(estoque)
        elif operacao == '0':
            print("\nEncerrando programa...")
            break
        else:
            print(MENSAGEM_ERRO_NUMERO)

        continuar = input("\nDeseja continuar (sim/não)? ")
        if continuar.lower() == "não":
            print("\n>>Encerrando programa...<<")
            break
        elif continuar.lower() != "sim":
            print("\n>> Resposta inválida, reiniciando programa.")

estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
estoque = inserir_estoque_inicial(estoque_inicial)

menu(estoque)

