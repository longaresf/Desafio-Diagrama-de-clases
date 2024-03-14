class Pregunta():
    def __init__(self, enunciado:str, requerida:bool, lista_alternativas:list) -> None:
        self.__enunciado = enunciado
        self.__requerida = requerida
        self.__lista_alternativas = lista_alternativas
        self.ayuda = None

    @property
    def ayuda(self)->str:
        return self.ayuda

    @property
    def enunciado(self)->str:
        return self.enunciado

    @enunciado.setter
    def enunciado(self, enunciado)->None:
        self.__enunciado = enunciado

    @property
    def requerida(self)->str:
        return self.requerida

    @requerida.setter
    def requerida(self, requerida)->None:
        self.__requerida = requerida

    def mostrar_pregunta(self,enunciado, ayuda,lista_alternativas):
        for p in list(zip(enunciado,ayuda,lista_alternativas)):
            print(f"Pregunta: {p.enunciado}, lista_alternativas: {p.lista_alternativas}, Ayuda: {p.ayuda}")

