class ListadoRespuestas():
    def __init__(self,usuario:str, lista_respuestas:int):
        self.usuario = usuario
        self.lista_respuestas = lista_respuestas

    @property
    def usuario(self) -> int:
        return self.usuario

    @property
    def lista_respuestas(self) -> int:
        return self.lista_respuestas
