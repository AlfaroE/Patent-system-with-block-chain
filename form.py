from Objects.patent_physical import Patent_PhysicalPerson
from Objects.patent_moral import Patent_MoralPerson
from datetime import date,datetime
from random import randint as rand
import json
from pdfdocument.document import PDFDocument
from io import BytesIO

def create_patent():
    folio = ''.join([str(rand(0,9)) for i in range(8)])
    tipo_persona = int(input("Seleccione el tipo de persona 1) Persona Física, 2) Persona Moral \n$ "))
    patente = Patent_PhysicalPerson() if (tipo_persona == 1) else Patent_MoralPerson()
    patente.set_fecha_solicitud(str(date.today()))

    if tipo_persona == 1:
        curp = input("Ingrese su curp\n$ ")
        nombre = input("Ingrese su Nombre\n$ ")
        apellido_paterno = input("Ingrese su Apellido Paterno\n$ ")
        apellido_materno = input("Ingrese su Apellido Materno\n$ ")
        nacionalidad = input("Ingrese su Nacionalidad\n$ ")
        numero = int(input("Ingrese su Número de teléfono\n$ "))
        patente.set_persona_fisica(curp,nombre,apellido_paterno,apellido_materno,nacionalidad,numero)

    else:
        rfc = input("Ingrese su razón rfc\n$ ")
        razon_social = input("Ingrese su razón social\n$ ")
        nacionalidad = input("Ingrese su nacionalidad")
        telefono = int(input("Ingrese su Número de teléfono\n$ "))
        patente.set_persona_moral(rfc,razon_social,nacionalidad,telefono)

    codigo_postal = int(input("Ingrese su código postal\n$ "))
    calle = input("Ingrese su dirección\n$ ")
    numero_ext = int(input("Ingrese su Número Exterior\n$ "))
    numero_int = int(input("Ingrese su Número Interior\n$ "))
    colonia = input("Ingrese su Colonia\n$ ")
    municipio = input("Ingrese su Municipio\n$ ")
    entidad_federativa = input("Ingrese su Entidad federativa\n$ ")
    pais = input("Ingrese su país de origen\n$ ")
    patente.set_domicilio(codigo_postal,calle,numero_ext,numero_int,colonia,municipio,entidad_federativa,pais)

    seleccion = False
    while not seleccion:
        signo = int(input("Seleccione su signo que solicita\n \t1=Publicación de Nombre Comercial\n \t2=Registro de Aviso Comercial\n \t3=Registro de Marca\n \t4=Registro de Marca Colectiva\n \t5=Registro de Marca de Certificación\n$ "))
        signo_text = ""
        if(signo in [i for i in range(1,6)]):
            if signo == 1:
                seleccion = True
                signo_text = "Publicación de Nombre Comercial"
            elif signo == 2:
                seleccion = True
                signo_text = "Registro de Aviso Comercial"
            elif signo == 3:
                seleccion = True
                signo_text = "Registro de Marca"
            elif signo == 4:
                seleccion = True
                signo_text = "Registro de Marca Colectiva"
            elif signo == 5:
                seleccion = True
                signo_text = "Registro de Marca de Certificación"
            else:
                print("Signo de razón ingresado no existe")
    patente.set_datos_de_signo(signo_text)

    fecha = input("Ingrese la fecha de primer uso en México con el siguiente formato DD/MM/YYY\n$ ")
    patente.set_fecha_primer_uso_mexico(fecha)

    patente.set_clase(''.join([str(rand(0,9)) for i in range(2)]))

    nombre = input("Ingrese el nombre de su producto\n$ ")
    patente.set_nombre_producto(nombre)

    descripcion = input("Ingrese una leve descripción del producto\n$ ")
    patente.set_descripcion_producto(descripcion)

    patente_json = json.dumps(patente.__dict__)
    jsonFile = open('./PatentFiles/'+nombre+'.json','w')
    jsonFile.write(patente_json)
    jsonFile.close()
    f = BytesIO()
    pdf = PDFDocument(f)
    pdf.init_report()
    pdf.h1(nombre)
    with open('./PatentFiles/'+nombre+'.json') as json_file:
        data = json.load(json_file)
        print(type(data))
        for i,j in data.items():
            pdf.p(str(i)+":"+str(j))
    pdf.generate()
    with open('./PatentFiles/'+nombre+'.pdf','wb') as file:
        file.write(f.getvalue())
    return './PatentFiles/'+nombre+'.pdf'

