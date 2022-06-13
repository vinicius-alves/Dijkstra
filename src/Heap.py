import numpy as np

class Heap:
  
    def __init__(self, tamanho_maximo):
          
        self.tamanho_maximo = tamanho_maximo
        self.tamanho_atual = 0
        
        self.heap = [] 
        for i in range(tamanho_maximo):
            no_vazio = {'conteudo':None, 'prioridade':-np.inf}
            self.heap.append(no_vazio)
        
        self.heap[0] =  {'conteudo':None, 'prioridade':np.inf}
  
    
    def heap_vazia(self):
        return self.tamanho_atual <= 0
    
    def filho_direito(self, posicao) -> int:
        return (2 * posicao) + 1
    
    def filho_esquerdo(self, posicao) -> int:
        return 2 * posicao
    
    def pai(self, posicao) -> int:
        return posicao//2
    
    def folha(self, posicao) -> bool:
        if posicao > self.tamanho_atual//2:
            return True
        elif posicao > self.tamanho_atual:
            return False
        else:
            return False
   
  
    def trocar_no(self, posicao_a, posicao_b):
        temp = self.heap[posicao_a]
        self.heap[posicao_a] = self.heap[posicao_b]
        self.heap[posicao_b] = temp
    
    def corrige_heap_descendo(self, posicao):
  
        while not self.folha(posicao):
            
            maior = posicao
            
            if (self.heap[self.filho_esquerdo(posicao)]['prioridade'] > self.heap[maior]['prioridade'] ):
                maior = self.filho_esquerdo(posicao)
                
            if (self.heap[self.filho_direito(posicao)]['prioridade'] > self.heap[maior]['prioridade'] ):
                maior = self.filho_direito(posicao)
                
            if maior != posicao:
                self.trocar_no(posicao, maior)                
                posicao = maior
            else:
                break
            
        return
        
    def pop(self):
        
        if self.heap_vazia():
            raise ValueError('Heap vazia')
  
        pop_no = self.heap[1]
        self.heap[1] = self.heap[self.tamanho_atual]
        self.heap[self.tamanho_atual] = {'conteudo':None, 'prioridade':-np.inf}
        self.tamanho_atual -= 1
        self.corrige_heap_descendo(1)
          
        return pop_no        
  
    def inserir(self, prioridade, elemento):
          
        if self.tamanho_atual >= self.tamanho_maximo:
            return
        self.tamanho_atual += 1
        self.heap[self.tamanho_atual] = {'conteudo':elemento, 'prioridade':prioridade}
  
        posicao = self.tamanho_atual
  
        self.corrige_heap_subindo(posicao)
            
    def corrige_heap_subindo(self, posicao):
        
         while self.heap[posicao]['prioridade'] > self.heap[self.pai(posicao)]['prioridade']:
            self.trocar_no(posicao, self.pai(posicao))
            posicao = self.pai(posicao)
  
    
    