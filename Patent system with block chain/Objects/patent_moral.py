from .patent import Patent

class Patent_MoralPerson(Patent):
    def set_persona_moral(self,rfc,razon_social,nacionalidad,telefono):
        self.rfc = rfc
        self.razon_social = razon_social
        self.nacionalidad = nacionalidad
        self.telefono = telefono
