from datetime import datetime

class Persona:
    def _init_(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = None

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        if self.apellido_casada:
            return f"{self.apellidos} de casada: {self.apellido_casada}"
        else:
            return self.apellidos

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def obtener_nombre_completo(self):
        return f"{self.nombres} {self.obtener_apellidos()}"

    def obtener_edad(self):
        if self.fecha_nacimiento:
            hoy = datetime.now()
            edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
            return edad
        else:
            return "Fecha de nacimiento desconocida"

persona = Persona()
persona.insertar_nombres(input("Ingrese su nombre"))
persona.insertar_apellidos(input("Ingrese su apellido"))
persona.insertar_apellido_casada(input("Ingrese su apellido de casada"))
persona.insertar_fecha_nacimiento(datetime(2004, 5, 20))

print(persona.obtener_nombre_completo())  
print("El tiene", persona.obtener_edad())  