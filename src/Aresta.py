class Aresta:
    
    def __init__(self, de, para, peso):
        self.de = de
        self.para = para
        self.peso = peso
        
    def get_json(self):
        return {"from": self.de, "to": self.para, "label": str(self.peso), "arrows": {"to": {"enabled": True}}}