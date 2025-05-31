class vehiculo:
    def __init__(self, marca, modelo, patente, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.kilometraje = kilometraje
    def __str__(self):
        return f'Es un {self.marca} {self.modelo}, patente {self.patente} con {self.kilometraje}km'

#Programa principal

print("----------------------------------------------------")
print("--------Procesamiento de autos---------")
print("----------------------------------------------------")
print("\nPor Francisco Pacheco\n")
while True:
    eleccion = input("Quieres (A)ñadir un auto nuevo o (R)evisar un auto en stock?\n> ").lower()
    if eleccion in ["a", "añadir", "añadir un auto nuevo", "añadir un auto", "añadir auto"]:
        marcaNueva = input("Qué marca es? > ").lower()
        modeloNuevo = input("Qué modelo es? > ").lower()
        patenteNueva = input("Qué patente tiene? > ").lower()
        kilometrajeNuevo = input("Qué kilometraje tiene? > ").lower()
        auto = vehiculo(marcaNueva, modeloNuevo, patenteNueva, kilometrajeNuevo)
    elif eleccion in ["r", "revisar", "revisar un auto", "revisar un auto en stock", "revisar auto", "revisar stock"]:
        print(f'{str(auto)}')
    else:
        print("Respuesta inválida!")
