class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, endereco, telefones, emails):
        self.contatos[nome] = {
            'endereco': endereco,
            'telefones': telefones,
            'emails': emails
        }

    def alterar_contato(self, nome, endereco=None, telefones=None, emails=None):
        if nome in self.contatos:
            if endereco:
                self.contatos[nome]['endereco'] = endereco
            if telefones:
                self.contatos[nome]['telefones'] = telefones
            if emails:
                self.contatos[nome]['emails'] = emails
            print(f"Contato {nome} alterado com sucesso.")
        else:
            print(f"Contato {nome} não encontrado.")

    def exibir_contato(self, nome):
        if nome in self.contatos:
            contato = self.contatos[nome]
            print(f"Nome: {nome}")
            print("Endereço:")
            for chave, valor in contato['endereco'].items():
                print(f"  {chave.capitalize()}: {valor}")
            print(f"Telefones: {', '.join(contato['telefones'])}")
            print(f"Emails: {', '.join(contato['emails'])}")
        else:
            print(f"Contato {nome} não encontrado.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado.")

    def listar_contatos(self):
        if self.contatos:
            for nome in self.contatos:
                print(f"Nome: {nome}")
        else:
            print("Nenhum contato registrado.")


def menu():
    agenda = Agenda()

    while True:
        print("\n--- Menu da Agenda ---")
        print("1. Adicionar Contato")
        print("2. Alterar Contato")
        print("3. Exibir Contato")
        print("4. Remover Contato")
        print("5. Listar Contatos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do contato: ")
            endereco = {
                'rua': input("Digite a rua: "),
                'numero': input("Digite o número: "),
                'complemento': input("Digite o complemento: "),
                'bairro': input("Digite o bairro: "),
                'municipio': input("Digite o município: "),
                'estado': input("Digite o estado: "),
                'cep': input("Digite o CEP: ")
            }
            telefones = input("Digite os telefones (separados por vírgula): ").split(',')
            emails = input("Digite os emails (separados por vírgula): ").split(',')
            agenda.adicionar_contato(nome, endereco, [telefone.strip() for telefone in telefones],
                                     [email.strip() for email in emails])

        elif opcao == '2':
            nome = input("Digite o nome do contato que deseja alterar: ")
            print("Deixe o campo em branco se não quiser alterar.")
            endereco = {}
            endereco['rua'] = input("Nova rua: ")
            endereco['numero'] = input("Novo número: ")
            endereco['complemento'] = input("Novo complemento: ")
            endereco['bairro'] = input("Novo bairro: ")
            endereco['municipio'] = input("Novo município: ")
            endereco['estado'] = input("Novo estado: ")
            endereco['cep'] = input("Novo CEP: ")

            endereco = {key: value for key, value in endereco.items() if value}

            telefones = input("Novos telefones (separados por vírgula): ")
            emails = input("Novos emails (separados por vírgula): ")

            telefones = [telefone.strip() for telefone in telefones.split(',')] if telefones else None
            emails = [email.strip() for email in emails.split(',')] if emails else None

            agenda.alterar_contato(nome, endereco if endereco else None, telefones if telefones else None,
                                   emails if emails else None)

        elif opcao == '3':
            nome = input("Digite o nome do contato que deseja exibir: ")
            agenda.exibir_contato(nome)

        elif opcao == '4':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)

        elif opcao == '5':
            agenda.listar_contatos()

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
