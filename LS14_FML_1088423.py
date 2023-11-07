class carro:
    def _init_(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = False
        self.CambioDolar = 0.0
        self.descApli = 0.0

    def Modelo(self, unModelo):
        self.modelo = unModelo
    def Precio(self, unPrecio):
        self.precio = unPrecio
    def Marca(self, unaMarca):
        self.marca = unaMarca
    def TipCamb(self, unTipoCambio):
        self.CambioDolar = unTipoCambio
    def Disponibilidad(self):
        self.disponible = not self.disponible
    def MostrarDispon(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInfo(self):
        precio_en_dolares = self.precio / self.CambioDolar
        disponibilidad = self.MostrarDispon()
        return (
            f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares ${precio_en_dolares}. {disponibilidad}"
        )

    def AplicarDescuento(self, miDescuento):
        self.descApli = miDescuento
        self.precio -= miDescuento
        self.Precio(self.precio)

car = carro()
car.Marca(input("Ingresa la marca del automóvil: "))
car.Modelo(int(input("Ingresa el modelo del automóvil: ")))
car.Precio(float(input("Ingresa el precio del automóvil: ")))
car.TipCamb(float(input("Ingresa el tipo de cambio a dólares: ")))

print("El automóvil ha sido registrado con los siguientes datos:")
print(car.MostrarInfo())

car.Disponibilidad()
print(f"Disponibilidad: {car.MostrarDispon()}")

descuento = float(input("Ingresa el descuento a aplicar (0 si no aplicar descuento): "))
if descuento > 0:
    car.AplicarDescuento(descuento)
    print(f"Descuento aplicado. Precio actualizado: Q{car.precio}")

print("Información actualizada del automóvil:")
print(car.MostrarInfo())