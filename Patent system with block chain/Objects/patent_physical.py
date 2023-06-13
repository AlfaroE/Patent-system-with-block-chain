from .patent import Patent

class Patent_PhysicalPerson(Patent):
    
    def set_persona_fisica(self,curp,nombre,apellido_paterno,apellido_materno,nacionalidad,numero):
        self.curp = curp
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nacionalidad = nacionalidad
        self.numero = numero


    def set_fecha_solicitud(self, fecha):
        super(Patent_PhysicalPerson,self).set_fecha_solicitud(fecha)
    
    def set_domicilio(self,codigo_postal,calle,numero_ext,numero_int,colonia,municipio,entidad_federativa,pais):
        super(Patent_PhysicalPerson,self).set_domicilio(codigo_postal,calle,numero_ext,numero_int,colonia,municipio,entidad_federativa,pais)

    def set_datos_de_signo(self,dato_de_signo):
        super(Patent_PhysicalPerson,self).set_datos_de_signo(dato_de_signo)
    
    def set_fecha_primer_uso_mexico(self,fecha_primer_uso_mexico):
        super(Patent_PhysicalPerson,self).set_fecha_primer_uso_mexico(fecha_primer_uso_mexico)
    
    def set_clase(self,clase):
        super(Patent_PhysicalPerson,self).set_clase(clase)

    def set_nombre_producto(self,nombre_producto):
        super(Patent_PhysicalPerson,self).set_nombre_producto(nombre_producto)

    def set_descripcion_producto(self,descripcion_producto):
        super(Patent_PhysicalPerson,self).set_descripcion_producto(descripcion_producto)
