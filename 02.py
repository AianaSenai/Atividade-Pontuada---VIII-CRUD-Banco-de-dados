import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando bando de dados.
Meu_banco = create_engine("sqlite:///meubanco.db")

#criando conexão com banco de dados.
Session = sessionmaker(bind=Meu_banco)
session = Session()

#criando tabela
Base = declarative_base()

class funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", String)
    cpf = Column("cpf", String)
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", String)
    telefone = Column("telefone", String)  

    #Atributos da classe.

    def __init__(self, nome, idade, cpf, setor, funcao, salario, telefone):
        self.nome = nome
        self.idade = idade
        self.cfp = cpf
        self.sertor = setor
        self.funcao = funcao
        self.salaio = salario
        self.telefone = telefone

#Criando tabela no banco de dados.
Base.metadata.create_all(bind=Meu_banco)

#Salvar no banco de dados.
os.system("cls || clear")

print("======= Solicitando dados para o usuário =======")
inserir_nome = input("\nDigite seu nome: ")
inserir_idade = input("Digite sua idade: ")
inserir_cpf = input("Digite seu cpf: ")
inserir_setor = input("Digite seu setor: ")
inserir_funcao = input("Digite sua função: ")
