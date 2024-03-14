class Alternativa():
    def __init__(self, contenido:str):
        self.__contenido = contenido
        self.ayuda:str = None

    def mostrar_alternativas(self,contenido,ayuda):
        for a in list(zip(self.contenido,self.ayuda)):
            return f"Alternativa: {a.contenido}, Ayuda: {a.ayuda}"
    
    @property
    def ayuda(self)->str:
        return self.ayuda

    @property
    def contenido(self)->str:
        return self.contenido

    @ayuda.setter
    def contenido(self, contenido)->None:
        self.__contenido = contenido

    @ayuda.setter
    def ayuda(self, ayuda:str)->None:
        self.ayuda = ayuda
