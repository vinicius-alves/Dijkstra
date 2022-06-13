import json
import os
import webbrowser
from .No import No
from .Aresta import Aresta

class Grafo:
    
    def __init__(self):
        self.nos = []
        self.nos_dict = {}
        self.json_nos = []
        self.json_arestas = []
        self.cidades_seguras = []
    
    def inicializar_estrutura(self, numero_cidades, numero_estradas , numero_membros):
        
        self.numero_cidades  = numero_cidades
        self.numero_estradas = numero_estradas
        self.numero_membros  = numero_membros
        
        for i in range(self.numero_cidades):
            no = No(i)
            self.nos.append(no)
            self.nos_dict[i] = no
            
    def adicionar_aresta(self, de, para, peso):
        aresta = Aresta(de, para, peso)
        self.nos[de].adicionar_aresta(aresta)
        self.nos[para].adicionar_aresta(aresta)
        self.json_arestas.append(aresta.get_json())
        
    def get_no(self,name):
        return self.nos_dict[name]
        
    def setar_no_com_presa(self, no):
        self.nos[no].setar_no_com_presa()
        
    def setar_no_com_cacador(self, no):
        self.nos[no].setar_no_com_cacador()
                
    def coletar_json_nos(self):
        for no in self.nos:
            self.json_nos.append(no.get_json())
            
    def printar_grafo(self, mensagem):
        
        self.coletar_json_nos()
        
        physics = 'true'
        if len (self.json_nos) >20:
            physics = 'false'
        
        
        
        html = '''
            <!DOCTYPE html>
            <html lang="pt-br">
              <head>
                <title>Grafo</title>

                <style type="text/css">

                  #mynetwork {
                    width: 100%;
                    height: 100%;
                    position: absolute; 
                    top: 0; left: 0;
                  }
                </style>

                <script
                  type="text/javascript"
                  src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"

                ></script>

                <script type="text/javascript">

                  var nos = '''+ json.dumps(self.json_nos) +''';
                  var arestas = '''+ json.dumps(self.json_arestas) +''';
                  var network = null;


                  function draw() {
                    nodes = '''+ json.dumps(self.json_nos) +''';

                    // Instantiate our network object.
                    var container = document.getElementById("mynetwork");
                    var data = {
                      nodes: nos,
                      edges: arestas,
                    };
                    var options = {
                      physics: { enabled: '''+physics+''' },
                      nodes: {
                        

                      },
                    };
                    network = new vis.Network(container, data, options);
                    
                    

                    var net = document.getElementById('mynetwork');


                  }
                </script>
              </head>
              <body onload="draw()">
                <h1 style="text-align: center;" >''' + mensagem + '''</h1>
                <br></br>
                <div id="mynetwork"></div>
              </body>
            </html>
        '''
        

        # salvando o grafo localmente
        filename = "grafo.html"
        f = open(filename, "w")
        f.write(html)
        f.close()
        # abrindo no navegador
        webbrowser.open('file://' + os.path.realpath(filename))