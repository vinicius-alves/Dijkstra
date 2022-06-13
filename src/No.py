import pandas as pd
from random import randrange

class No:
    
    def __init__(self, nome, conteudo = None):
        self.nome = nome
        self.arestas = []
        self.conteudo = conteudo
        self.tipo = 'vazio'
        self.df_imagens_presa = pd.read_csv('imagens_presa.csv')
        self.df_imagens_cacador = pd.read_csv('imagens_cacador.csv')
        self.df_imagens_cidade = pd.read_csv('imagens_cidades.csv')
        self.df_imagens_cidade_segura = pd.read_csv('imagens_cidade_segura.csv')
        
    def adicionar_aresta(self, aresta):
        self.arestas.append(aresta)
        
    def setar_no_com_cacador(self):
        self.tipo = 'cacador'
        
    def setar_no_com_presa(self):
        self.tipo = 'presa'
        
    def setar_no_como_cidade_segura(self):
        self.tipo = 'cidade_segura'
        
    def nos_alcancaveis(self):
        nos_vizinhos = []
        for aresta in self.arestas:
            if aresta.de == self.nome:
                dict_no = {'no': aresta.para, 'peso': aresta.peso}
                nos_vizinhos.append(dict_no)
        return nos_vizinhos
            
        
    def get_json(self):
        
        no_json = {"id": self.nome, "label": self.nome, "shape": "circularImage", "image": self.get_imagem_aleatoria()}
            
        return no_json
    
    def get_imagem_aleatoria(self):
        
        if self.tipo == 'presa':
            idx = randrange(self.df_imagens_presa.shape[0])
            return self.df_imagens_presa['link'].tolist()[idx]
        
        elif self.tipo == 'cacador':
            idx = randrange(self.df_imagens_cacador.shape[0])
            return self.df_imagens_cacador['link'].tolist()[idx]
        
        elif self.tipo == 'cidade_segura':
            idx = randrange(self.df_imagens_cidade_segura.shape[0])
            return self.df_imagens_cidade_segura['link'].tolist()[idx]
        
        else:
            idx = randrange(self.df_imagens_cidade.shape[0])
            return self.df_imagens_cidade['link'].tolist()[idx]
            