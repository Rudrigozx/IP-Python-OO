from modelo_POO import Voo
from viewer_POO import Interface
import datetime
import os

class Aeroporto:
    
    def __init__(self):
        self.voo = list()
        self.viewer = Interface()
        

        
    def menu(self):
        return self.viewer.menu_visao()

        
    def cadastro(self):
        cidades=list()
        numero_voo, dia, mes, ano, periodicidade, cidades, assentos = self.viewer.dados_cadastro()
        data = datetime.datetime(int(ano),int(mes),int(dia))
        for voo in self.voo:
            if numero_voo == voo.numero:
                alertas='Numero de voo em uso!!!'
                return self.viewer.alerta(alertas)
        if periodicidade=='diario':
            for i in range(365):
               date=data + datetime.timedelta(days=i)
               self.voo.append(Voo(numero_voo, date, periodicidade, cidades, assentos))
               
           
        elif periodicidade=='semanal':
            for i in range(52):
                date=data + datetime.timedelta(weeks=i)
                self.voo.append(Voo(numero_voo, date, periodicidade, cidades, assentos))


    def exibir(self):
        tamanho=len(self.voo)
        if  self.verificar_vazio(self.voo)== None:
            alertas='Nenhum voo cadastrado!!!'
            return self.viewer.alerta(alertas)
        else:
            return self.viewer.imprime_voo(self.voo,tamanho)


    def verificar_vazio(self, lista):
    
        for verificador in lista:
            return verificador


    def buscar_destino(self):
        busca_lista=[]
        dia,mes,ano,destino = self.viewer.dados_busca_destino()
        data_voo= datetime.datetime(int(ano),int(mes),int(dia))
        for voo in self.voo:
            if destino == voo.cidades[-1] and data_voo == voo.data:
                busca_lista.append(voo)
        tamanho=len(busca_lista)
        if  self.verificar_vazio(busca_lista)== None:
            alertas='Nenhum voo encontrado!!!'
            return self.viewer.alerta(alertas),self.menu()
        else:
            return self.viewer.imprime_voo(busca_lista,tamanho)

    def buscar_escala(self):
        busca_lista_escala=[]
        dia,mes,ano,escala = self.viewer.dados_busca_escala()
        data_voo_escala = datetime.datetime(int(ano),int(mes),int(dia))
        for voo in self.voo:
            for i in range(len(voo.cidades)-2):
                if escala == voo.cidades[i+1] and data_voo_escala == voo.data:
                    busca_lista_escala.append(voo)
        tamanho = len(busca_lista_escala)
        if  self.verificar_vazio(busca_lista_escala)== None:
            alertas='Nenhum voo encontrado!!!'
            return self.viewer.alerta(alertas)
        else:
            return self.viewer.imprime_voo(busca_lista_escala,tamanho)


    def buscar_venda(self):
        global busca_lista_venda
        busca_lista_venda=[]
        
        dia,mes,ano,destino_pessoal, origem_pessoal = self.viewer.dados_venda()
        data_voo_venda = datetime.datetime(int(ano),int(mes),int(dia))
        for voo in self.voo:
            for cidade in voo.cidades[1:]: 
                if destino_pessoal== cidade :
                    if data_voo_venda == voo.data and origem_pessoal == voo.cidades[0]:
                        busca_lista_venda.append(voo)
        tamanho = len(busca_lista_venda)
        if  self.verificar_vazio(busca_lista_venda)== None:
            alertas='Nenhum voo encontrado!!!'
            return self.viewer.alerta(alertas)
        else:
            return self.viewer.imprime_voo(busca_lista_venda,tamanho)


    def venda(self):
        
        global busca_lista_venda
        self.buscar_venda()
        if self.verificar_vazio(busca_lista_venda)== None:
            alertas='Erro na venda!!!'
            return self.viewer.alerta(alertas)
        else:
            numero_voo,quantidade = self.viewer.vender()
            for voo in busca_lista_venda:
                    if numero_voo == voo.numero:
                      for voos in  self.voo:
                          if voo==voos:
                              if int(voos.assentos) >= int(quantidade) and int(quantidade) > 0:
                                  meu_voo = Voo(voos.numero, voos.data, voos.periodicidade, voos.cidades, voos.assentos )
                                  meu_voo.vendendo(quantidade)
                                  voos.assentos = meu_voo.assentos
                                  alertas='Vendido com sucesso!!!'
                                  return self.viewer.alerta(alertas)
 

                              else:  
                                  alertas='Erro na venda!!!'
                                  return self.viewer.alerta(alertas)
        
            



    def carregar(self):
        if os.path.isfile('dados_voo.csv'):
            cidades=list()
            bd = open('dados_voo.csv','r')
            for line in bd:
              numero, data, periodicidade, cidade, assentos = line.split(";")
              cidades=cidade[1:].split(",")
              date= datetime.datetime(int(data[:4]),int(data[5:7]),int(data[8:10]))
              self.voo.append(Voo(numero, date, periodicidade, cidades, int(assentos)))
            bd.close()

    

    def salvar(self):
        cidade=''
        bd = open('dados_voo.csv','w')    
        for voo in self.voo:
            cidade=''
            for cidades in voo.cidades:
                cidade=cidade + ',' + cidades
        
            bd.write("{};{};{};{};{}\n".format(voo.numero, voo.data, voo.periodicidade, cidade, voo.assentos))                          
        bd.close()

