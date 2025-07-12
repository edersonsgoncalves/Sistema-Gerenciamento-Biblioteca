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
    def __init__(self, data, tipo, cliente, isbn):
        self.data = data
        self.tipo = int(tipo)
        self.cliente = int(cliente)
        self.isbn = isbn

    def __str__(self):
        if self.tipo == "1":
            tipo_transacao = "Empréstimo"
        elif self.tipo == "2":
            tipo_transacao = "Devolução"

        return f"{self.data} | {tipo_transacao} | Cliente: {self.cliente} | ISBN: {self.isbn}"

class Biblioteca:
    def __init__(self):
        self.livros =[]
        self.clientes = []
        self.transacoes = []
        self._proximo_id_cliente = 1

    def adicionar_livros (self, titulo, autor, isbn):
        livro = Livro(titulo=titulo, autor=autor, isbn=isbn)
        self.livros.append(livro)
        print ("Livro cadastrado com sucesso.")
    
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
    
    def emprestar_livro(self, isbn, cliente):
        livro_localizado = None
        for livro in self.livros:
            if isbn == livro.isbn:
                livro_localizado = livro
                break
        if livro_localizado:
            if livro_localizado.disponivel:
                livro_localizado.disponivel = False
                grava_transacao = Transacoes(data=time.now(), tipo=1, cliente=cliente, isbn=isbn)
                self.transacoes.append(grava_transacao)
                print (f"Livro {livro_localizado.titulo} emprestado com sucesso.")
            else:
                print(f"Livro '{livro_localizado.titulo}' já está emprestado.")

    def devolver_livro(self, isbn):
        livro_localizado = None
        for livro in self.livros:
            if isbn == livro.isbn:
                livro_localizado = livro
                break
        if livro_localizado:
            if not livro_localizado.disponivel:
                livro_localizado.disponivel = True
                print(f"Livro '{livro_localizado.titulo}' devolvido com sucesso!")
            else:
                print(f"Erro: Livro '{livro_localizado.titulo}' já está disponível na biblioteca.")
        else:
            print(f"Erro: Livro com ISBN '{isbn}' não encontrado na biblioteca.")

    def cadastrar_cliente (self, nome, telefone, email):
        # Tratamento dados
        novo_cliente_nome = nome.strip().lower()
        novo_cliente_telefone = telefone.strip()
        novo_cliente_email = email.strip().lower()

        if novo_cliente_nome and novo_cliente_telefone and novo_cliente_email:
            novo_cliente = Cliente(nome=novo_cliente_nome, telefone=novo_cliente_telefone, email=novo_cliente_email, nro_registro=self._proximo_id_cliente)
            self.clientes.append(novo_cliente)
            self._proximo_id_cliente += 1
            print (f"Cliente '{novo_cliente_nome}' cadastrado com sucesso.")
        else:
            print (f"Erro ao cadastrar o cliente '{novo_cliente_nome}'.")

    def listar_clientes(self):
        if not self.clientes:
            print ("Nenhum cliente cadastrado")
            return 
        print("\n--- Clientes ---")
        for cliente in self.clientes:
            print(cliente)
    
    def impedir_cliente(self, nro_registro):
        cliente_localizado = None
        for cliente in self.clientes:
            if nro_registro == cliente.nro_registro:
                cliente_localizado = cliente
                break
        if cliente_localizado:
            if cliente_localizado.status:
                cliente_localizado.status = False
                motivo_impedimento = input("Digite o motivo do impedimento: ").strip().lower()
                if motivo_impedimento:
                    cliente_localizado.motivo = motivo_impedimento
            else:
                print(f"Cliente '{cliente_localizado.nome}' já está impedido.")

    def buscar_cliente_registro (self, nro_registro):
            for cliente in self.clientes:
                if nro_registro == cliente.nro_registro:
                    return cliente
            return None

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

[q] Sair
=> """

while True:
    opcao = input(menu).strip()

    if opcao[0] == "n":
        print ("--- Novo Cliente ---")
        input_nome_cliente = input("Digite o nome do Cliente: ")
        input_telefone_cliente = input("Digite o telefone do Cliente: ")
        input_email_cliente = input("Digite o e-mail do Cliente: ")
        novo_cliente = minha_biblioteca.cadastrar_cliente(nome=input_nome_cliente, telefone=input_telefone_cliente, email=input_email_cliente)
    
    elif opcao[0] == "l":
        minha_biblioteca.listar_clientes()
        input("Pressione Enter para retornar.")
    
    elif opcao[0] == "i":
        minha_biblioteca.listar_clientes()
        nro_cliente_impedir = int(input("Digite o número de registro do cliente para iniciar o impedimento: ").strip())
        minha_biblioteca.impedir_cliente(nro_registro=nro_cliente_impedir)

    elif opcao[0] == "c":
        print("Vamos dar início ao cadastro de livros..")
        titulo_inserido = input("Digite o título do livro: ").strip().lower()
        autor_inserido = input("Digite o autor do livro: ").strip().lower()
        isbn_inserido = input("Digite o isbn do livro: ").strip()

        if titulo_inserido and autor_inserido and isbn_inserido:
            novo_livro = minha_biblioteca.adicionar_livros(titulo=titulo_inserido, autor=autor_inserido, isbn=isbn_inserido)
        else:
            print ("Algum dado informado foi inválido")

    elif opcao[0] == "b":
        termo_livro_buscar = input("Digite o ~termo~ para buscar no [TITULO] e no [AUTOR] do livro: ").strip()
        livros_busca = minha_biblioteca.buscar_livro(termo_busca=termo_livro_buscar)
        if livros_busca:
            for livro in livros_busca:
                print (livro)
            input("Pressione enter para continuar...")

    elif opcao[0] == "m":
        if minha_biblioteca.livros:
            for livro in minha_biblioteca.livros:
                print (livro)
            input("Digite enter para retornar.")
        else:
            print ("Nenhum livro cadastrado.")
            input("Digite enter para retornar.")
    
    elif opcao[0] == "e":
        if minha_biblioteca.clientes:
            print("Vamos iniciar o processo de empréstimo...")
            minha_biblioteca.listar_clientes()
            nro_cliente_emprestar = int(input("Digite o número de registro do cliente para iniciar o empréstimo: ").strip())
            buscar_cliente = minha_biblioteca.buscar_cliente_registro(nro_registro=nro_cliente_emprestar)

            if buscar_cliente:
                 if minha_biblioteca.livros:
                    for livro in minha_biblioteca.livros:
                        print (livro)
                    livro_emprestimo = int(input("Digite o ~ISBN~ do livro que será emprestado"))
                    minha_biblioteca.emprestar_livro(isbn=livro_emprestimo, cliente=buscar_cliente)

            else:
                print ("erro")
        else:
            pass

    elif opcao[0] == "d":
        if minha_biblioteca.livros:
            for livro in minha_biblioteca.livros:
                print (livro)
            nro_livro_devolver = str(input("Digite o ~ISBN~ do livro: ").strip())
            minha_biblioteca.devolver_livro(isbn=nro_livro_devolver)
            input("Digite enter para retornar.")
        else:
            print ("Nenhum livro cadastrado.")
            input("Digite enter para retornar.")

    elif opcao[0] == "q":
        print ("Encerrando...")
        break

    else:
        print("Opção inválida.")

