from encuesta import Encuesta,EncuestaEdad,EncuestaRegion

class usuario():
    def __init__(self, correo_electronico:str, edad:int, region:int):
        self.__correo_electronico = correo_electronico
        self.__edad = edad
        self.__region = region
        self.lista_listado_respuestas =[]
        self.__respuesta:str

    @property
    def correo_electronico(self) -> int:
        return self.__correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, correo_electronico)->None:
        self.__correo_electronico = correo_electronico

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, edad)->None:
        self.__edad = edad

    @property
    def region(self) -> int:
        return self.__region

    @region.setter
    def region(self, region)->None:
        self.__region = region


    def responder_encuesta(self, edad_min, edad_max, edad, lista_listado_respuestas,list_region):
        respuesta = input("Respuesta: ")
        if EncuestaEdad.validar_edad(self, edad_min, edad_max, lista_listado_respuestas) == True:
            self.lista_listado_respuestas.append(self.edad, self.respuesta)
        elif EncuestaRegion.validar_region(self,list_region,lista_listado_respuestas) == True:
            self.lista_listado_respuestas.append(list_region, self.respuesta)
        else:
            self.lista_listado_respuestas.append(respuesta)
