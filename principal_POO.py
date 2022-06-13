from controle_POO import Aeroporto
import os


meu_aeroporto = Aeroporto()
meu_aeroporto.carregar()
opcao = meu_aeroporto.menu()

while opcao!=0:
     
    if opcao==1:
        os.system('cls') or None
        meu_aeroporto.cadastro()

    elif opcao==2:
        os.system('cls') or None
        meu_aeroporto.exibir()
        
    elif opcao==3:
        os.system('cls') or None
        meu_aeroporto.buscar_destino()

    elif opcao==4:
        os.system('cls') or None
        meu_aeroporto.buscar_escala()

    elif opcao==5:
        os.system('cls') or None
        meu_aeroporto.venda()
    opcao= meu_aeroporto.menu()
meu_aeroporto.salvar()
