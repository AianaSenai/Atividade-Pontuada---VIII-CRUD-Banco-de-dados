#Alunas: Jamile e Aiana
#Turma: G93313

import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando o banco de dados
Meu_banco = create_engine("sqlite:///meubanco.db")

# Criando conexão com o banco de dados
Session = sessionmaker(bind=Meu_banco)
session = Session()

# Criando tabela
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    cpf = Column("cpf", String, unique=True)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Float)
    telefone = Column("telefone", String)

    def __init__(self, nome: str, idade: int, cpf: str, setor: str, funcao: str, salario: float, telefone: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

# Criando a tabela no banco de dados
Base.metadata.create_all(bind=Meu_banco)

#Salvar no banco de dados.
os.system("cls || clear")

def salvar_funcionario(funcionario):
    session.add(funcionario)
    session.commit()
    print("Funcionário salvo com sucesso!")

def listar_todos_funcionarios():
    return session.query(Funcionario).all()

def pesquisar_um_funcionario(cpf):
    return session.query(Funcionario).filter_by(cpf=cpf).first()

def atualizar_funcionario(funcionario_atualizado):
    funcionario = session.query(Funcionario).filter_by(id=funcionario_atualizado.id).first()
    if funcionario:
        funcionario.nome = funcionario_atualizado.nome
        funcionario.idade = funcionario_atualizado.idade
        funcionario.setor = funcionario_atualizado.setor
        funcionario.funcao = funcionario_atualizado.funcao
        funcionario.salario = funcionario_atualizado.salario
        funcionario.telefone = funcionario_atualizado.telefone
        session.commit()
        print("Funcionário atualizado com sucesso!")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario(cpf):
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print(f"{funcionario.nome} excluído com sucesso.")
    else:
        print("Funcionário não encontrado.")

def menu():
    while True:
        print("""          ======= RH System ======= 
----------------------------------------------
|  1 - Adicionar funcionário                 |
|  2 - Consultar um funcionário              |
|  3 - Atualizar os dados de um funcionário  |
|  4 - Excluir um funcionário                |
|  5 - Listar todos os funcionários          |
|  0 - Sair do sistema                       |
----------------------------------------------              
              """)

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            os.system("cls || clear")
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            cpf = input("Digite o CPF: ")
            setor = input("Digite o setor: ")
            funcao = input("Digite a função: ")
            salario = float(input("Digite o salário: "))
            telefone = input("Digite o telefone: ")
            funcionario = Funcionario(nome, idade, cpf, setor, funcao, salario, telefone)
            salvar_funcionario(funcionario)

        elif opcao == '2':
            os.system("cls || clear")
            cpf = input("Digite o CPF do funcionário: ")
            funcionario = pesquisar_um_funcionario(cpf)
            if funcionario:
                print(f"Funcionário: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Função: {funcionario.funcao}, Salário: {funcionario.salario}, Telefone: {funcionario.telefone}")
            else:
                print("Funcionário não encontrado.")

        elif opcao == '3':
            os.system("cls || clear")
            cpf = input("Digite o CPF do funcionário a ser atualizado: ")
            funcionario = pesquisar_um_funcionario(cpf)
            if funcionario:
                funcionario.nome = input("Digite o novo nome: ") or funcionario.nome
                funcionario.idade = int(input("Digite a nova idade: ") or funcionario.idade)
                funcionario.setor = input("Digite o novo setor: ") or funcionario.setor
                funcionario.funcao = input("Digite a nova função: ") or funcionario.funcao
                funcionario.salario = float(input("Digite o novo salário: ") or funcionario.salario)
                funcionario.telefone = input("Digite o novo telefone: ") or funcionario.telefone
                atualizar_funcionario(funcionario)
            else:
                print("Funcionário não encontrado.")

        elif opcao == '4':
            os.system("cls || clear")
            cpf = input("Digite o CPF do funcionário a ser excluído: ")
            excluir_funcionario(cpf)

        elif opcao == '5':
            os.system("cls || clear")
            funcionarios = listar_todos_funcionarios()
            print("Lista de Funcionários:")
            for f in funcionarios:
                print(f"{f.id} - {f.nome} - {f.cpf} - {f.setor} - {f.funcao} - R${f.salario} - {f.telefone}")

        elif opcao == '0':
            session.close()
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

