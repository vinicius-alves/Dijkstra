from src import *
import pandas as pd

# Basta selecionar a entrada aqui e rodar o código
entrada = 'entradas\\Entrada1.txt'
g = ConstrutorDeGrafo().construir_grafo(entrada)

dists_list = []
for no in g.nos:
    if no.tipo in ['presa','cacador']:
        mapa_distancias = dijkstra(g, no.nome)
        mapa_distancias['tipo_no'] = no.tipo
        dists_list.append(mapa_distancias)
        
df = pd.DataFrame(dists_list)
df = df.groupby('tipo_no', as_index = False).max()
df = df.T
df['tipo_no'] = df.index
df.columns = df[:1].values[0]
df = df.rename({'tipo_no':'no'}, axis =1)
df = df[1:].reset_index(drop = True)
df = df[df['presa']<df['cacador']]

mensagem = ''
if df.shape[0] > 0:
    mensagem += 'O REINO ESTÁ SALVO!\n'
    mensagem += str(df.shape[0]) + ' cidade(s) seguras\n'
    lista_cidades = df['no'].astype('str').tolist()
    for no in g.nos:
        if no.nome in df['no']:
            no.setar_no_como_cidade_segura()
    mensagem += 'Cidade(s) seguras: '+' '.join(lista_cidades)
    
else:
     mensagem +="INFELIZMENTE O PRECONCEITO VENCEU :("
        
# Printando no console
print(mensagem)

# Printando no navegador
# Nota: há 4 tipos de nós:
# nó com personagem lgbt: cidade em que há algum membro lgbt
# nó com biroliro: cidade representada por imagens do rei do gado
# nó cidade segura: cidade que lgbts conseguem se reunir, representada por cidade com bandeira lgbt no fundo
# nó cidade não segura: cidade não segura para lgbts, representada por uma cidade preto e branco
g.printar_grafo(mensagem)