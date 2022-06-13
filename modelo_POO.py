class Voo:
    
    def __init__(self, numero_voo, data_voo, periodicidade, lista_de_cidades, assentos_disponiveis):
        self.numero = numero_voo
        self.data = data_voo
        self.periodicidade = periodicidade
        self.cidades = lista_de_cidades
        self.assentos = assentos_disponiveis

    def vendendo(self, quantidade):
        self.assentos = int(self.assentos) - int(quantidade)




    
