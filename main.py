import time

class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def __str__(self):
        if self.disponivel:
            disponibilidade = "Disponível"
        else:
            disponibilidade = "Indisponível"
        return f"[{disponibilidade}] | {self.titulo} - {self.autor} ({self.isbn})"

class Cliente:
    def __init__(self, nome, telefone, email, status=True, motivo="OK", nro_registro=None):
        self.nro_registro = nro_registro
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.status = status
        self.motivo = motivo
    
    def __str__(self):
        if self.status:
            if self.nro_registro:
                return f"({self.nro_registro}) {self.nome.title()} | Telefone: {self.telefone} | E-Mail: {self.email}"
            else:
                return f"(---) {self.nome.title()} | Telefone: {self.telefone} | E-Mail: {self.email}"
        else:
            return f"------------------------------ Cliente Bloqueado ------------------------------\n({self.nro_registro}) {self.nome.title()} | Telefone: {self.telefone} | E-Mail: {self.email}\n{self.motivo.title()}\n--------------------------------------------------------------------------------"

class Transacoes:
    def __init__(self, data, tipo, cliente_nro_registro, isbn):
        self.data = data # Timestamp (float)
        self.tipo = tipo # 1 para Empréstimo, 2 para Devolução (int)
        self.cliente_nro_registro = cliente_nro_registro # Número de registro do cliente (int)
        self.isbn = isbn # ISBN do livro (string)

    def __str__(self):
        tipo_transacao = ""
        if self.tipo == 1: 
            tipo_transacao = "Empréstimo"
        elif self.tipo == 2:
            tipo_transacao = "Devolução"

        # Formata o timestamp para uma data/hora legível
        data_formatada = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.data))

        return (f"Data: {data_formatada} | Tipo: {tipo_transacao} | "
                f"Cliente Reg: {self.cliente_nro_registro} | ISBN: {self.isbn}")

class Biblioteca:
    def __init__(self):
        self.livros =[]
        self.clientes = []
        self.transacoes = []
        self._proximo_id_cliente = 1

    def adicionar_livros (self, titulo, autor, isbn):
        livro = Livro(titulo=titulo, autor=autor, isbn=isbn)
        self.livros.append(livro)
        print (f"Livro '{titulo.title()}' cadastrado com sucesso.")
    
    def listar_livros(self):
        if not self.livros:
            print ("Nenhum livro cadastrado")
            return
        print("\n--- Livros na Biblioteca ---")
        for livro in self.livros:
            print(livro)
    
    def buscar_livro (self, termo_busca):
        livros_encontrados = []
        termo_busca_lower = termo_busca.lower()
        for livro in self.livros:
            if termo_busca_lower in livro.titulo.lower() or termo_busca_lower in livro.autor.lower():
                livros_encontrados.append(livro)
        return livros_encontrados
    
    def emprestar_livro(self, isbn, cliente_obj): # Recebe o objeto Cliente
        livro_localizado = None
        for livro in self.livros:
            if isbn == livro.isbn:
                livro_localizado = livro
                break
        if livro_localizado:
            if livro_localizado.disponivel:
                livro_localizado.disponivel = False
                grava_transacao = Transacoes(data=time.time(), tipo=1, cliente_nro_registro=cliente_obj.nro_registro, isbn=isbn)
                self.transacoes.append(grava_transacao)
                print (f"Livro '{livro_localizado.titulo}' emprestado com sucesso ao cliente {cliente_obj.nome.title()}.")
                return True # Indica sucesso no empréstimo
            else:
                print(f"Livro '{livro_localizado.titulo}' já está emprestado.")
                return False # Indica que o livro já estava emprestado
        else:
            print(f"Erro: Livro com ISBN '{isbn}' não encontrado na biblioteca.")
            return False # Indica que o livro não foi encontrado

    def devolver_livro(self, isbn, cliente_nro_registro):
        livro_localizado = None
        for livro in self.livros:
            if isbn == livro.isbn:
                livro_localizado = livro
                break
        if livro_localizado:
            if not livro_localizado.disponivel:
                livro_localizado.disponivel = True
                # Grava a transação de devolução
                grava_transacao = Transacoes(data=time.time(), tipo=2, cliente_nro_registro=cliente_nro_registro, isbn=isbn)
                self.transacoes.append(grava_transacao)
                print(f"Livro '{livro_localizado.titulo}' devolvido com sucesso!")
                return True # Indica sucesso na devolução
            else:
                print(f"Erro: Livro '{livro_localizado.titulo}' já está disponível na biblioteca.")
                return False # Indica que o livro já estava disponível
        else:
            print(f"Erro: Livro com ISBN '{isbn}' não encontrado na biblioteca.")
            return False # Indica que o livro não foi encontrado

    def cadastrar_cliente (self, nome, telefone, email):
        # Tratamento dados
        novo_cliente_nome = nome.strip().lower()
        novo_cliente_telefone = telefone.strip()
        novo_cliente_email = email.strip().lower()

        if novo_cliente_nome and novo_cliente_telefone and novo_cliente_email:
            novo_cliente = Cliente(nome=novo_cliente_nome, telefone=novo_cliente_telefone, email=novo_cliente_email, nro_registro=self._proximo_id_cliente)
            self.clientes.append(novo_cliente)
            self._proximo_id_cliente += 1
            print (f"Cliente '{novo_cliente_nome.title()}' cadastrado com sucesso. Registro: {novo_cliente.nro_registro}")
            return True
        else:
            print (f"Erro ao cadastrar o cliente. Todos os campos são obrigatórios.")
            return False

    def listar_clientes(self):
        if not self.clientes:
            print ("Nenhum cliente cadastrado")
            return 
        print("\n--- Clientes ---")
        for cliente in self.clientes:
            print(cliente)
        return True # Retorna True se houver clientes listados
    
    def buscar_cliente_por_registro(self, nro_registro):
        for cliente in self.clientes:
            if cliente.nro_registro == nro_registro:
                return cliente # Retorna o objeto Cliente se encontrado
        return None # Retorna None se não encontrado

    def impedir_cliente(self, nro_registro):
        cliente_localizado = self.buscar_cliente_por_registro(nro_registro)
        
        if cliente_localizado:
            if cliente_localizado.status:
                cliente_localizado.status = False
                motivo_impedimento = input("Digite o motivo do impedimento: ").strip().lower()
                if motivo_impedimento:
                    cliente_localizado.motivo = motivo_impedimento
                    print(f"Cliente '{cliente_localizado.nome.title()}' impedido com sucesso. Motivo: {cliente_localizado.motivo.title()}")
                else:
                    print(f"Não é possível prosseguir sem um motivo para o inpedimento.")
            else:
                print(f"Cliente '{cliente_localizado.nome.title()}' já está impedido. Motivo atual: {cliente_localizado.motivo.title()}")
        else:
            print(f"Erro: Cliente com registro '{nro_registro}' não encontrado.")

    def listar_transacoes(self):
        if not self.transacoes:
            print("\nNenhuma transação registrada.")
            return
        print("\n--- Histórico de Transações ---")
        for transacao in self.transacoes:
            print(transacao)


minha_biblioteca = Biblioteca()

nome_programa = "Biblioteca Py".center(32,"-")
boas_vindas = "Seja Bem Vind@!".center(32)

menu = f"""
{nome_programa}
{boas_vindas}
Selecione uma das opções abaixo:

-> Clientes
[n]\tNovo Cliente
[l]\tListar Clientes
[i]\tImpedir Cliente
-> Livros
[c]\tCadastrar Livro
[m]\tExibir Livros Cadastrados
[b]\tBuscar Livro
-> Operações
[e]\tEmprestar Livro
[d]\tDevolver Livro
[t]\tListar Transações

[q] Sair
=> """

while True:
    opcao = input(menu).strip().lower()

    if opcao[0] == "n":
        print ("--- Novo Cliente ---")
        input_nome_cliente = input("Digite o nome do Cliente: ")
        input_telefone_cliente = input("Digite o telefone do Cliente: ")
        input_email_cliente = input("Digite o e-mail do Cliente: ")
        minha_biblioteca.cadastrar_cliente(nome=input_nome_cliente, telefone=input_telefone_cliente, email=input_email_cliente)
    
    elif opcao[0] == "l":
        minha_biblioteca.listar_clientes()
        input("Pressione Enter para retornar.")
    
    elif opcao[0] == "i":
        minha_biblioteca.listar_clientes()
        nro_cliente_impedir = input("Digite o número de registro do cliente para iniciar o impedimento: ").strip()
        # Validação básica para garantir que é um número antes de converter
        if nro_cliente_impedir.isdigit():
            nro_cliente_impedir = int(nro_cliente_impedir)
            minha_biblioteca.impedir_cliente(nro_registro=nro_cliente_impedir)
        else:
            print("\nNúmero de registro inválido. Por favor, digite apenas números.")
        input("Pressione Enter para retornar.")


    elif opcao[0] == "c":
        print("Vamos dar início ao cadastro de livros..")
        titulo_inserido = input("Digite o título do livro: ").strip().lower()
        autor_inserido = input("Digite o autor do livro: ").strip().lower()
        isbn_inserido = input("Digite o isbn do livro: ").strip()

        if titulo_inserido and autor_inserido and isbn_inserido:
            minha_biblioteca.adicionar_livros(titulo=titulo_inserido, autor=autor_inserido, isbn=isbn_inserido)
        else:
            print ("Algum dado informado foi inválido. Todos os campos são obrigatórios.")
        input("Pressione Enter para retornar.")

    elif opcao[0] == "b":
        termo_livro_buscar = input("Digite o ~termo~ para buscar no [TITULO] e no [AUTOR] do livro: ").strip()
        livros_busca = minha_biblioteca.buscar_livro(termo_busca=termo_livro_buscar)
        if livros_busca:
            print("\n--- Resultados da Busca ---")
            for livro in livros_busca:
                print (livro)
        else:
            print("\nNenhum livro encontrado com o termo informado.")
        input("Pressione Enter para continuar...")

    elif opcao == "m":
        minha_biblioteca.listar_livros() # Chamando o método listar_livros diretamente
        input("Pressione Enter para retornar.")
        
    elif opcao == "e":
        print("\n--- Empréstimo de Livro ---")
        if not minha_biblioteca.listar_clientes(): # Apenas chama para exibir e verifica se há clientes
            print("Não há clientes cadastrados para realizar empréstimos.")
            input("Pressione Enter para retornar.")
            continue # Volta ao menu principal

        nro_cliente_emprestar_str = input("Digite o número de registro do cliente para o empréstimo: ").strip()
        if not nro_cliente_emprestar_str.isdigit():
            print("\nNúmero de registro inválido. Por favor, digite apenas números.")
            input("Pressione Enter para retornar.")
            continue

        nro_cliente_emprestar = int(nro_cliente_emprestar_str)
        cliente_emprestimo = minha_biblioteca.buscar_cliente_por_registro(nro_cliente_emprestar)

        if cliente_emprestimo:
            if cliente_emprestimo.status: # Verifica se o cliente não está impedido
                minha_biblioteca.listar_livros() # Exibe os livros disponíveis
                if not minha_biblioteca.livros: # Verifica se há livros para emprestar
                    print("Não há livros cadastrados para empréstimo.")
                    input("Pressione Enter para retornar.")
                    continue

                isbn_emprestar = input("Digite o ISBN do livro a ser emprestado: ").strip() # Corrigido para string
                minha_biblioteca.emprestar_livro(isbn=isbn_emprestar, cliente_obj=cliente_emprestimo) # Passa o objeto cliente
            else:
                print(f"Cliente '{cliente_emprestimo.nome.title()}' está impedido de realizar empréstimos. Motivo: {cliente_emprestimo.motivo.title()}")
        else:
            print(f"Cliente com registro '{nro_cliente_emprestar}' não encontrado.")
        input("Pressione Enter para retornar.")


    elif opcao == "d":
        print("\n--- Devolução de Livro ---")
        if not minha_biblioteca.listar_clientes(): # Verifica se há clientes para associar a devolução
            print("Não há clientes cadastrados. Não é possível registrar a devolução de um cliente específico.")
            input("Pressione Enter para retornar.")
            continue

        nro_cliente_devolver_str = input("Digite o número de registro do cliente que está devolvendo: ").strip()
        if not nro_cliente_devolver_str.isdigit():
            print("\nNúmero de registro inválido. Por favor, digite apenas números.")
            input("Pressione Enter para retornar.")
            continue
        
        nro_cliente_devolver = int(nro_cliente_devolver_str)
        cliente_devolucao = minha_biblioteca.buscar_cliente_por_registro(nro_cliente_devolver)

        if cliente_devolucao:
            minha_biblioteca.listar_livros()
            if not minha_biblioteca.livros:
                print("Não há livros para devolver.")
                input("Pressione Enter para retornar.")
                continue

            isbn_devolver = input("Digite o ISBN do livro a ser devolvido: ").strip() # Corrigido para str
            minha_biblioteca.devolver_livro(isbn=isbn_devolver, cliente_nro_registro=cliente_devolucao.nro_registro) # Passa o nro_registro do cliente
        else:
            print(f"Cliente com registro '{nro_cliente_devolver}' não encontrado.")
        input("Pressione Enter para retornar.")

    elif opcao == "t":
        minha_biblioteca.listar_transacoes()
        input("Pressione Enter para retornar.")

    elif opcao == "q":
        print ("Encerrando...")
        break

    else:
        print("Opção inválida.")
