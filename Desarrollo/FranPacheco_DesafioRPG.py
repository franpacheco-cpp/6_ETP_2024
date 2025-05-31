import random, json

personaje = {"STR": 3, "DEX": 3, "INT": 3, "NIV": 1, "NOM": "Nadie", "VIC": 0, "HER": 0}
enemigo = {"STR": 0, "DEX": 0, "INT": 0, "NOM": "Nadie"}
listaNombres = ["Darion el Grande", "Mit el debil", "Muler la dracónida", "S'eva el trompetista", "Julian la pastora", "Murag la bruja", "Qena el ardiente", "Principe Kriv", "Holos el buho", "Ethos el nigromante", "Jun el esqueletico", "Esteban", "Rodaja de pan consciente", "Trio de duendes", "Wolo el clérigo", "Xesphos el rey del Infierno", "Ghalimdann Gomez"]

def guardarPersonaje():
    with open(f'{personaje["NOM"]}.json', 'w') as archivoGuardar:
        archivoGuardar.write(json.dumps(personaje));
    return personaje;

def cargarPersonaje(nombre):
    with open(f'{nombre}.json', 'r') as archivo:
        personaje = json.load(archivo);
    return personaje;

def generarEncuentro():
    enemigo["NOM"] = listaNombres[random.randint(0, 16)];
    enemigo["STR"] = personaje["STR"] + random.randint(-3, 3);
    enemigo["DEX"] = personaje["DEX"] + random.randint(-3, 3);
    enemigo["INT"] = personaje["INT"] + random.randint(-3, 3);
    return enemigo;

def combatir():
    ventaja = 0
    if personaje["STR"] >= enemigo["STR"]:
        ventaja += 1
    if personaje["DEX"] >= enemigo["DEX"]:
        ventaja += 1
    if personaje["INT"] >= enemigo["INT"]:
        ventaja += 1
    if ventaja >= 2:
        personaje["VIC"] += 1
        personaje["STR"] += random.randint(0, 2)
        personaje["DEX"] += random.randint(0, 2)
        personaje["INT"] += random.randint(0, 2)
        if random.randint(1,5) >= 3:
            personaje["NIV"] +=1;
            return f'Ganaste la batalla contra {enemigo["NOM"]} y subiste al nivel {personaje["NIV"]}!\n--------------------------------------------------------'
        else:
            return f'¡Ganaste la batalla contra {enemigo["NOM"]}!\n--------------------------------------------------------'
    else:
        personaje["HER"] +=1;
        return f'Perdiste la batalla y escapaste por los pelos de {enemigo["NOM"]}...\n--------------------------------------------------------'
    
def verPersonaje():
    return f'- Datos de {personaje["NOM"]} -\n--------------------------------------------------------\nFuerza: {personaje["STR"]}\nDestreza: {personaje["DEX"]},\nInteligencia: {personaje["INT"]}\n--------------------------------------------------------\nNivel: {personaje["NIV"]}\nBatallas ganadas: {personaje["VIC"]}\nHeridas graves: {personaje["HER"]}\n--------------------------------------------------------'

def jugar():
    print(f'Hmm, "{personaje["NOM"]}" - interesante nombre por decir poco.')
    print(f'{personaje["NOM"]} deberá luchar por su vida en las catacumbas,\nenfrentandose a distintos enemigos con atributos variantes que deberá vencer.\nSi cree que no podrá vencer a uno, es mejor escapar antes que pelear.')
    print("Escribe 'Salir', 'terminar' o 'abandonar' para terminar la partida\nEscribe 'Huir', 'Escapar' o 'Irme' para evitar un combate\nEscribe 'Pelear', 'Atacar' o 'Combatir' para atacar a tu enemigo\nEscribe 'Ver', 'Inspeccionar' o 'Personaje' para averiguar sobre tus propios datos\n--------------------------------------------------------")
    print(verPersonaje());
    generarEncuentro();
    while True:
        if personaje["HER"] >=3:
            print(f'{personaje["NOM"]} está demasiado herid@, debe retirarse por siempre...')
            print("- Fin del juego -")
            break;
        if personaje["NIV"] <= 5:
            print("- Bosque Encantado -")
        elif personaje["NIV"] <= 8:
            print('- Entrada de Cueva -')
        elif personaje["NIV"] <= 12:
            print('- Catacumbas Oscuras -')
        elif personaje["NIV"] <=20:
            print('- Mazmorra Oculta -')
        elif personaje["NIV"] <=30:
            print('- Fortaleza Maligna -')
        elif personaje["NIV"] <50:
            print('- Puerta al Inframundo -')
        elif personaje["NIV"]>=50:
            print('- El reino del Mal -')
        print(f'Ves a {enemigo["NOM"]}.\nTiene {enemigo["STR"]} puntos de fuerza, {enemigo["DEX"]} puntos de destreza y {enemigo["INT"]} puntos de inteligencia...')
        eleccion = input("Qué haces? > ").lower();
        if eleccion in ["salir", "terminar", "abandonar"]:
            print("Gracias por jugar!\nDeseas guardar tu personaje para jugar después?")
            eleccionGuardado = input("> ").lower();
            if eleccionGuardado in ["si", "sí", "s", "ok", "okay", "okey"]:
                guardarPersonaje();
                break;
            else:
                break;
        elif eleccion in ["huir", "escapar", "irme", "irse", "me voy", "me escapo"]:
            print("Sales corriendo!")
            generarEncuentro();
        elif eleccion in ["pelear", "atacar", "combatir", "batir", "lo ataco", "la ataco", "le ataco"]:
            print("Empieza la batalla!")
            print(combatir());
            print(verPersonaje());
            generarEncuentro();
        elif eleccion in ["inspeccionar", "ver", "datos", "personaje"]:
            print(verPersonaje());


#Programa Principal
print("--------------------------------------------------------")
print("*********Dungeon  Quest***********")
print("--------------------------------------------------------")
cargarEleccion = input("Quieres cargar un personaje con el que jugaste previamente?\n> ").lower();
if cargarEleccion in ["si", "sí", "s"]:
    nombreCargado = input("Escribe el nombre exacto de tu personaje guardado: ");
    personaje = cargarPersonaje(nombreCargado);
    jugar();
else:
    personaje["NOM"] = input("Introduce el nombre de tu personaje > ")
    jugar()
