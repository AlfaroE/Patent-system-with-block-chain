from Objects.patent_physical import Patent_PhysicalPerson
from Objects.patent_moral import Patent_MoralPerson
from datetime import date

def create_patent():
    tipo_persona = int(input("Seleccione el tipo de persona 1) Persona Física, 2) Persona Moral \n$ "))
    patente = Patent_PhysicalPerson() if (tipo_persona == 1) else Patent_MoralPerson()
    patente.set_fecha_solicitud(date.today())
    return patente

