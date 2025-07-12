📚 Biblioteca Py - Sistema de Gerenciamento de Biblioteca
Este é um sistema simples de gerenciamento de biblioteca desenvolvido em Python, utilizando os princípios da Programação Orientada a Objetos (POO). O objetivo principal é praticar a criação e interação entre classes, o uso de estruturas de dados (listas) e a lógica de controle de fluxo para simular operações básicas de uma biblioteca.

✨ Funcionalidades
O sistema permite gerenciar livros, clientes e registrar transações de empréstimo e devolução.

Classes Implementadas:
Livro: Representa um livro individual com atributos como título, autor, ISBN e status de disponibilidade.
Cliente: Representa um cliente da biblioteca, com nome, telefone, e-mail, número de registro e status de impedimento (ativo/bloqueado).
Transacoes: Registra cada operação de empréstimo ou devolução, incluindo data, tipo de transação, cliente envolvido e o ISBN do livro.
Biblioteca: A classe principal que gerencia as coleções de Livros, Clientes e Transacoes. Contém os métodos para todas as operações do sistema.
Operações Suportadas:

Clientes:
[n] Novo Cliente: Cadastra um novo cliente na biblioteca.
[l] Listar Clientes: Exibe todos os clientes cadastrados.
[i] Impedir Cliente: Bloqueia um cliente, impedindo-o de realizar empréstimos.

Livros:
[c] Cadastrar Livro: Adiciona um novo livro ao acervo.
[m] Exibir Livros Cadastrados: Lista todos os livros disponíveis na biblioteca.
[b] Buscar Livro: Permite buscar livros por título ou autor.

Operações:
[e] Emprestar Livro: Registra o empréstimo de um livro para um cliente, alterando o status de disponibilidade do livro.
[d] Devolver Livro: Registra a devolução de um livro, tornando-o disponível novamente.
[t] Listar Transações: Exibe o histórico de todas as transações de empréstimo e devolução.
[q] Sair: Encerra o programa.

🚀 Como Executar
Pré-requisitos: Certifique-se de ter o Python 3 instalado em seu sistema.
Salvar o Código: Copie o código fornecido e salve-o em um arquivo chamado biblioteca.py (ou qualquer outro nome com extensão .py).
Executar: Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o comando:
python biblioteca.py

Interagir: O programa exibirá um menu. Digite a opção desejada e siga as instruções no console.

🤝 Colaboração
Este projeto foi desenvolvido com a assistência e orientação de um LLM (IA / Gemini), que me auxiliou na estruturação do código, na depuração de erros e na implementação de diversas funcionalidades.
Sinta-se à vontade para explorar o código, fazer modificações e adicionar novas funcionalidades!
