import numpy as np
from .Heap import Heap

def dijkstra(grafo, no_inicial_nome):
    
    mapa_distancias = {}
    for no in grafo.nos:
        mapa_distancias[no.nome] = np.inf
    
    mapa_distancias[no_inicial_nome] = 0

    heap = Heap(len(grafo.nos))
    heap.inserir(0, no_inicial_nome)
    
    nos_visitados = []

    while not heap.heap_vazia():
        no_atual_nome = heap.pop()['conteudo']
        nos_visitados.append(no_atual_nome)

        no = grafo.get_no(no_atual_nome)
        for no_dict in no.nos_alcancaveis():
            vizinho = no_dict['no']
            distancia = no_dict['peso']
            if vizinho not in nos_visitados:
                novo_custo = mapa_distancias[no_atual_nome] + distancia
                if novo_custo <  mapa_distancias[vizinho] :
                    heap.inserir(novo_custo, vizinho)
                    mapa_distancias[vizinho] = novo_custo
    return mapa_distancias