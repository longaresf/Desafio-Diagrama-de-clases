from alternativa import Alternativa
from listado_respuestas import ListadoRespuestas

class Encuesta():
    Alternativa.alternativas
    ListadoRespuestas.lista_respuestas
    def __init__(self, nombre:str, lista_preguntas:list, lista_listado_respuestas:list):
        self.__nombre = nombre
        self.lista_preguntas = lista_preguntas
        self.lista_listado_respuestas = lista_listado_respuestas
        self.respuesta:str = None
        self.ayuda = None

    @property
    def respuestas(self)->str:
        return self.respuestas
    
    @property
    def ayuda(self)->str:
        return self.ayuda
    
    @property
    def nombre(self)->str:
        return self.nombre

    @nombre.setter
    def nombre(self, nombre)->None:
        self.__nombre = nombre

    @property
    def lista_preguntas(self)->str:
        return self.lista_preguntas
    
    @property
    def lista_listado_respuestas(self)->str:
        return self.lista_listado_respuestas

    def mostrar_encuesta(self, nombre, lista_preguntas, lista_listado_respuestas, ayuda, respuesta)->None:
        print(f"Encuesta: {self.nombre}")
        for i in range(len(zip(self.lista_preguntas,ayuda,Alternativa.mostrar_alternativas()))):
            print(f"\nPregunta {i+1}:")
            print(f"{self.lista_preguntas[i]}, Ayuda: {self.ayuda[i]}, Alternativa: {self.alternativa[i]}, Ayuda: {self.ayuda_alt[i]}")


class EncuestaEdad(Encuesta):
    def __init__(self, edad_min:int, edad_max:int):
        self.__edad_min = edad_min
        self.__edad_max = edad_max
        self.edad:int = None
        self.lista_listado_respuestas =[]
        super().__init__()
        
    @property
    def edad_min(self) -> int:
        return self.__edad_min

    @property
    def edad_max(self) -> int:
        return self.__edad_max

    @edad_min.setter
    def edad_min(self, edad_min)->None:
        self.__edad_min = edad_min

    @edad_max.setter
    def edad_max(self, edad_max)->None:
        self.__edad_max = edad_max

    def validar_edad(self, edad_min, edad_max, lista_listado_respuestas):
        if self.edad_min < self.edad or self.edad < self.edad_max :
            print('Pertenece a Encuesta por edad')
        else:
            print('No pertenece a Encuesta por edad')


class EncuestaRegion(Encuesta):
    def __init__(self, list_region:int):
        self.__list_region = list_region
        self.lista_listado_respuestas =[]
        super().__init__()
        
    @property
    def list_region(self) -> int:
        return self.__list_region

    @list_region.setter
    def list_region(self, list_region)->None:
        self.__list_region = list_region

    def validar_region(self,list_region,lista_listado_respuestas):
        if isinstance(list_region, list):
            for i in range (len(list_region)):
                if not isinstance(list_region[i], int):
                    raise ValueError("El valor ingresado no es un número entero")
                else:
                    print("Pertenece a Encuesta por Regiones")
        else:
            print("No pertenece a Encuesta por Regiones")

