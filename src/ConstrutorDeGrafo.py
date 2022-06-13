from .Grafo import Grafo

class ConstrutorDeGrafo:
    
    def construir_grafo (self,caminho_arquivo_txt):
        g = Grafo()

        f = open(caminho_arquivo_txt, "r")
        line = f.readline()
        counter = 0
        counter_presa = 0
        while(line):
            line = line.split('\n')[0]
            array = line.split(' ')
            array = [int(i) for i in array]

            if counter == 0:
                numero_cidades  = array[0]
                numero_estradas = array[1]
                numero_membros  = array[2]

                g.inicializar_estrutura(numero_cidades, numero_estradas , numero_membros)

            elif len(array) == 3:
                de   = array[0]
                para = array[1]
                peso = array[2]
                g.adicionar_aresta(de, para, peso)

            elif counter_presa < numero_membros:
                no =  array[0]
                g.setar_no_com_presa(no)

                counter_presa+=1 
            else:
                no =  array[0]
                g.setar_no_com_cacador(no)

            line = f.readline()
            counter+=1

        f.close()
        
        return g