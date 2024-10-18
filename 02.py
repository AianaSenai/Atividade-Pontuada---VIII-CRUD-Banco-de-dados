import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

BANCO_FUNCIONARIOS = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=BANCO_FUNCIONARIOS)
session = Session()

Base = declarative_base()

class Funcionario(Base):
    __tablename___ = "funcionarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", String)
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", String)
    telefone = Column("telefone", String)

def __init__(self, nome: str, idade:str, cpf:str, setor:str, funcao:str, salario:str, telefone:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

Base.metadata.create_all(bind=BANCO_FUNCIONARIOS)

def salvar_funcionario(funcionario):
    session.add(funcionario)
    session.commit()

def listar_todos_funcionarios():
    return session.query(Funcionario).all()

def pesquisar_um_funcionario(cpf):
    return session.query(Funcionario).filter(Funcionario.cpf == cpf).first()
    

def atualizar_funcionario(cpf, novos_dados):
    funcionario = pesquisar_um_funcionario(cpf)
    if funcionario:
        for key, value in novos_dados.itens():
            setattr(funcionario, key, value)
        session.commit()
def excluir_funcionario(cpf):
    funcionario = pesquisar_um_funcionario(cpf)
    if funcionario:
        session.delete(funcionario)
        session.commit()

def menu():
    while True:
      print("\n     === RH System ===")
      print("       1 - A  dicionar funcionário")
      print("       2 - Consultar um funcionário")
      print("       3 - Atualizar os dados de um funcionário")
      print("       4 - Excluir um funcionário")
      print("       5 - Listar todos os funcionários")
      print("       0 - Sair do sistema.")
      
      escolha = input("Escolha uma opção")

      if escolha == "1":
          nome = input("Nome: ")
          idade = int(input("Idade: "))
          cpf = input("CPF: ")
          setor = input("Setor: ")
          funcao = input("Funcao: ")
          salario = float(input("Salario: "))
          telefone = int(input("Telefone"))


      



os.system("cls || clear")

#create
print("solicitando dados para o usuario")
inserir_nome = input("digite seu nome: ")
inserir_email = input("digite seu email : ")
inserir_senha = input("digite sua senha: ")


usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()


#listando usuarios do banco de dados
print("exibindo todos usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

#read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#delete
print("\nexcluindo um usuário. ")
email_usuario = input("informe o email do usuario para ser excluido: ")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print(f"{usuario.nome} excluido com sucesso")


#listando usuarios do banco de dados
print("exibindo todos usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

#read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#update
print("atualizando dados do  usuario")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()

novos_dados = Usuario(
    nome = input("digite seu nome: ")
    email = input("digite seu email : ")
    senha = input("digite sua senha: ")

)

usuario = novos_dados
session.add(usuario)
session.commit()

#fechando conexao
session.close()