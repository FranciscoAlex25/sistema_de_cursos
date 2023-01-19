import json
import os
from cursos import Curso


class UsuariosArea:
    def __init__(self):
        self.verificar_usuario()

    '''
        Verifica se o usuário que está tentando fazer login
         na área de usuário  existe e se já tem uma senha definida
    '''

    def verificar_usuario(self):
        self.usuario = input('DIGITE SEU NOME DE USUÁRIO: ').strip().lower()

        # busca a lista de todos os usuários da "base de dados"
        with open('clientes.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_clientes = json.load(arquivo)

        # verifica se usuário tem senha ou não. Se não tiver, define uma.
        for cliete in lista_de_clientes:
            if self.usuario in cliete.values() and cliete['_Cliente__senha'] == None:
                self.senha = input('DIGITE UMA SENHA, POR FAVOR: ')
                self.cadastrar_senha(self.usuario, self.senha)
                self.exibir_menu(self.usuario)

            elif self.usuario in cliete.values() and cliete['_Cliente__senha'] != None:
                self.senha = input(
                    f'DIGITE SUA SENHA DE CLIENTE {self.usuario}: ')
                self.exibir_menu(self.usuario)

    # exibe o menu de opções do usuário
    def exibir_menu(self, usuario):
        print()
        print(80 * '*')
        print(f'BEM VINDO(A) {usuario}'.center(80).capitalize())
        print(80 * '*')

        print(80 * '-')
        print('CURSOS MATRICULADOS (1) INCREVER-SE (2) SAIR(3)'.center(80))
        print(80 * '-')

        self.verificar_escolha()

    # verifica qual opção o usuário escolheu do menu e chama o método relacionado
    def verificar_escolha(self):
        self.escolha = input(
            f'DIGITE O NÚMERO DE SUA ESCOLHA {self.usuario}: '.capitalize())

        if self.escolha == '1':
            ...
        elif self.escolha == '2':
            os.system('clear')

            print(80 * '#')
            Curso.listar_cursos(self)
            print(80 * '#')

            self.opc = input('DIGITE O NOME DO CURSO QUE DESEJA FAZER: ')
            self.verificar_cursos_existe(self.opc)

    # cadastrar senha do usuário caso seja seu primeiro acesso
    def cadastrar_senha(self, usuario, senha):
        print('entrou no adastrar senha ')
        with open('clientes.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_clientes = json.load(arquivo)
            print('leu arquivo')

        for cliente in lista_de_clientes:
            if cliente['_Pessoa__nome'] == usuario:
                cliente.update({'_Cliente__senha': senha})
                with open('clientes.json', 'w+', encoding='UTF-8') as arquivo:
                    json.dump(lista_de_clientes, arquivo)
                break

    # verificar se o curso que o usuário digitou existe na "base de dados"
    def verificar_cursos_existe(self, curso_escolhido):

        with open('cursos.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_cursos = json.load(arquivo)

        for curso in lista_de_cursos:
            if curso_escolhido in curso.values():
                # passa um dicionário como parâmetro
                self.cadastrar_curso(curso)
                self.exibir_menu(self.usuario)

    # cadastra o usuário no curso que ele deseja
    def cadastrar_curso(self, cursos):

        with open('clientes.json', 'r', encoding='UTF-8') as arquivo:
            lista_de_clientes = json.load(arquivo)

        with open('cursos.json', 'r', encoding='UTF-8') as arquivos:
            lista_de_cursos = json.load(arquivos)

        # buscando usuários na base de dados
        for cliente in lista_de_clientes:
            # verifica se a pessoa logada está na "base de dados"
            if cliente['_Pessoa__nome'] == self.usuario:
                '''
                    Percorre todos os cursos cadastrados. Se o curso 
                    desejado pelo usuário estiver presente na "base de dados",
                    este curso é vinculado ao cliente
                '''
                for c in lista_de_cursos:
                    print(c)
                    if c['_Curso__nome'] == cursos['_Curso__nome']:
                        cliente.update({'_Cliente__curso': c})

                        # enviar o cliente com o curso cadastrado na base de dados
                        with open('clientes.json', 'w+', encoding='UTF-8') as arquivo:
                            json.dump(lista_de_clientes, arquivo)
                        break
