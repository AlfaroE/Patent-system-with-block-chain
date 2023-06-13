
class Patent:
    def set_fecha_solicitud(self, fecha):
        self.fecha = fecha
    
    def set_domicilio(self,codigo_postal,calle,numero_ext,numero_int,colonia,municipio,entidad_federativa,pais):
        self.codigo_postal = codigo_postal
        self.calle = calle
        self.numero_ext = numero_ext
        self.numero_int = numero_int
        self.colonia = colonia
        self.municipio = municipio
        self.entidad_federativa = entidad_federativa
        self.pais = pais

    def set_datos_de_signo(self,dato_de_signo):
        self.datos_de_signo = dato_de_signo
    
    def set_fecha_primer_uso_mexico(self,fecha_primer_uso_mexico):
        self.fecha_primer_uso_mexico = fecha_primer_uso_mexico
    
    def set_clase(self,clase):
        self.clase = clase

    def set_nombre_producto(self,nombre_producto):
        self.nombre_producto = nombre_producto

    def set_descripcion_producto(self,descripcion_producto):
        self.descripcion_producto = descripcion_producto