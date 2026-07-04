import csv
import random 
import time 
from time import sleep
import os
from dropgen.RDSTable import RDSTable
from dropgen.RDSItem import RDSItem

jugadores = ["Cpu"]
#6-Clase Mapa
class Mapa_Bioma_Bosque:
    def __ini__(self):
        pass
class Base_estadisticas:
    def __init__(self, nombre):  #Clase a explotar (se usara para todas las demas clases las cuales seran hijo de esta clase padre
        self.nombre = nombre
        self.vida = 0
        self.ataque = 0
        self.defensa = 0
        self.defensa_añadida = 0
        self.estado = True #vivo
        self.barra = None
        self.Inventario = []
        self.Fabricacion = []
        
#5-Clase Personaje
class Personaje_humano(Base_estadisticas): 
    def __init__(self, nombre):  #Aqui se le asigna los valores a nuestra clase personaje, de la cual se apoya por el padre: Base_estadisticas
        super().__init__(nombre) 
        self.ataque = random.randint(2,6)
        self.vida = random.randint(20,35)
        self.vida_maxima = self.vida
        self.defensa = random.randint(0,5)
        self.velocidad = random.randint(1,10)
        self.barra = "[==========]"
        self.Inventario = []
    def perfil_humano(self,rival):
        if self.vida <= 0:
            self.barra = "[          ]"
            self.estado = False
            print(f"Jugador: {self.nombre} ha sido derrotado!")
            sleep(3)
            return
        elif self.vida <= self.vida_maxima/2:
            self.barra = "[=====     ]"
        elif self.vida == self.vida_maxima or self.vida > self.vida_maxima/2:
            self.barra = "[==========]" 
        print(f"-_-_-Humano de {self.nombre}-_-_-\nVida: {self.vida}->{self.barra}  Defensa añadida: {self.defensa_añadida}\nAtaque: {self.ataque}\nDefensa: {self.defensa}\nVelocidad: {self.velocidad}")
        try:
            Opcion_jugador = int(input(f"""{10*"="}Menu{10*"="}\n[1] Atacar\n[2] Inspeccionar\n[3] Defender\n[4] Inventario y Fabricar\nElige: """))
        except ValueError:
            print(f"{50*"="}\nFavor de ingresar valor numerico\n{50*"="}")
            sleep(2)
            os.system("cls")
        if Opcion_jugador == 1:
            if self.defensa_añadida <= 0:
                golpe_critico_o_debil = random.randint(int(-self.ataque/2),int(self.ataque/2))
                if golpe_critico_o_debil < 0:
                    daño_real = self.ataque+golpe_critico_o_debil
                    print(f"Daño de ataque: {daño_real}\nOh no, un golpe debil!!!")
                    vida_reciente = rival.vida
                    rival.vida -= daño_real
                    print(f"Su vida paso de {vida_reciente} pasó a {rival.vida}")
                    sleep(3)
                elif golpe_critico_o_debil > 0:
                    daño_real = self.ataque+golpe_critico_o_debil
                    print(f"Daño de ataque: {daño_real}\nWow, fue un golpe critico!!!")
                    vida_reciente = rival.vida
                    rival.vida -= daño_real
                    print(f"Su vida paso de {vida_reciente} pasó a {rival.vida}")
                    sleep(3)
                elif golpe_critico_o_debil == 0:
                    print(f"Daño de ataque: {self.ataque}")
                    rival.vida -= self.ataque
                    print(f"Su vida de {self.vida}")
                    sleep(3) 
                os.system("cls")
            elif self.defensa_añadida > 0:
                golpe_critico_o_debil = random.randint(int(-self.ataque/2),int(self.ataque/2))
                if golpe_critico_o_debil < 0:
                    daño_real = self.ataque+golpe_critico_o_debil
                    print(f"Daño de ataque: {daño_real}\nOh no, un golpe debil!!!")
                    defensa_acumulada = rival.defensa_añadida
                    rival.defensa_añadida -= daño_real
                    print(f"Su defensa de {defensa_acumulada} pasó a {rival.defensa_añadida}")
                    sleep(3)
                elif golpe_critico_o_debil > 0:
                    daño_real = self.ataque+golpe_critico_o_debil
                    print(f"Daño de ataque: {daño_real}\nWow, fue un golpe critico!!!")
                    defensa_acumulada = rival.defensa_añadida
                    rival.defensa_añadida -= daño_real 
                    print(f"Su defensa de {defensa_acumulada} pasó a {rival.defensa_añadida}") 
                    sleep(3)
                elif golpe_critico_o_debil == 0:
                    daño_real = self.ataque
                    print(f"Daño de ataque: {daño_real}")
                    defensa_acumulada = rival.defensa_añadida
                    rival.defensa_añadida -= daño_real
                    print(f"Su defensa de {self.defensa_añadida} paso a {rival.defensa_añadida}")
                    sleep(3)  
                os.system("cls")
        elif Opcion_jugador == 2:
            self.Inspeccion_humano()
        elif Opcion_jugador == 3:
            print(f"Humano se incremento la defensa!!!\nDefensa: {self.defensa}")
            sleep(1)
            self.defensa_añadida = self.defensa
        elif Opcion_jugador == 4:
            self.Inventario_y_Fabricar()            
        return
    
    def Inspeccion_humano(self):
        self.inspeccion = ["Rama de Madera", "Rama de Madera con Filo", 
        "piedra pequeña", "piedra mediana", "Tierra"]
        objeto_encontrado = random.choice(self.inspeccion)
        print(f"Ha encontrado: {objeto_encontrado}")
        self.Inventario.append(objeto_encontrado)
        sleep(2)
        os.system("cls")
        return 
    
    def Inventario_y_Fabricar(self): #En esta funcion de la clase humano, podras crear objetos y ver tu inventario
        while True:
            self.Fabricacion = {1:"1 rama, 1 piedra ",
                        2:"1 rama, 1 banda de soga",
                        3:"1 rama flexible, 2 hilos",
                        4:"2 ramas secas"}
            print(f"\n{6*"="}FABRICACION{6*"="}")
            print("1-Lanza\n2-Resortera\n3-Arco\n4-Rama en Llamas")
            print(f"{5*"_-"}Objetos en el inventario: {len(self.Inventario)} {5*"-_"}")
            contador_inventario = 0
            for elemento in self.Inventario:
                contador_inventario +=1
                print(f"{contador_inventario}- {elemento}x{len[elemento]}\n")
                sleep(1)
            try:
                opcion_fabricar = str(input("Opcion: "))
            except ValueError:
                os.system("cls")
                print(f"{50*"="}\nFavor de ingresar opcion existente [No simbolos o letras]\n{50*"="}")
                sleep(2)
                os.system("cls")
            if opcion_fabricar in self.Fabricacion:
                opcion_fabricar = int(opcion_fabricar)
                print(f"{self.Fabricacion[opcion_fabricar]}")
                if opcion_fabricar == self.Fabricacion[opcion_fabricar]:
                    print("Tienes los materiales suficientes para fabricarnFabricar?: [S/N]")
                    confirmar_fabricacion = input("Fabricar?: [S/N]").upper()
                    while True:
                        if confirmar_fabricacion == "S":
                            self.Inventario.append(opcion_fabricar)
                            self.Inventario.pop(self.Fabricacion[opcion_fabricar])
                            print("El objeto ha sido frabricado con exito")
                            break
                        elif confirmar_fabricacion == "N":
                            self.perfil_humano()
                            break
                        else:
                            print("Elige una opcion Existente")
                else:
                    pass
            elif opcion_fabricar == "B" or opcion_fabricar == "b":
                return
            else:
                print("Este objeto no existe...")
                sleep(2) 
    
#6-Funcion para la partida (ahora si gameplay)
def Jugar(jugador_1,jugador_2):
    jugador1 = Personaje_humano(jugador_1)
    jugador2 = Personaje_humano(jugador_2)
    while True:
        jugador1.perfil_humano(jugador2)
        if not jugador2.estado:
            print(f"Ganador: {jugador1.nombre}")
            break
        jugador2.perfil_humano(jugador1)
        if not jugador1.estado:
            print(f"Ganador: {jugador2.nombre}")
            break
        
#2-Opcion 1 (Jugar)
def Inicio_juego():
    while True:
        os.system("cls")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-\nBienvenidos jugadores\n_-_-_-_-_-_-_-_-_-_-_-_-")
        print(60*"=")
        mensaje = "[Favor de Ingresar los nombres de los jugadores registrados]\nIngrese [B] para volver al menu principal\n"
        for letra in mensaje:
            print(letra,end="", flush=True)
            sleep(0.01)
        else:
            pass
        if len(jugadores) == 1:
            print("\nNo hay registro alguno de jugadores")
            mensaje = "\nRegresando al menu principal..."
            for letra in mensaje:
                print(letra,end="", flush=True)
                sleep(0.1)
            print("")
            print(60*"=")
            sleep(2)
            return
        else:
            print(60*"=")
            nom_jugador = input("Nombre Jugador: ")
            if nom_jugador in jugadores:
                print(60*"=")
                print("[Si no hay jugador 2, ingresa [X] para omitir]")
                nom_jugador_2 = input("Nombre Jugador 2: ")
                if nom_jugador_2 == "X" or nom_jugador_2 == "x":
                    print(f"\nModo solitario: [{nom_jugador}] vs [Cpu]")
                    nom_jugador_2 = "Cpu"
                    sleep(2)
                    os.system("cls")
                    for count in range(3,0,-1):
                        print(count,end="", flush=True)
                        sleep(1)
                        os.system("cls")
                    jugador_1 = nom_jugador
                    jugador_2 = nom_jugador_2
                    Jugar(jugador_1, jugador_2)
                    return
                elif nom_jugador_2 == "B" or nom_jugador_2 == "b":
                    return
                elif nom_jugador_2 in jugadores:
                    print(f"\nJugadores encontrados: [{nom_jugador}] vs [{nom_jugador_2}]")
                    sleep(2)
                    os.system("cls")
                    for count in range(3,0,-1):
                        print(count,end="", flush=True)
                        sleep(1)
                        os.system("cls")
                    jugador_1 = nom_jugador
                    jugador_2 = nom_jugador_2
                    Jugar(jugador_1,jugador_2)
                    return
                else:
                    print("El jugador no se encuentra registrado")
                    sleep(3)
            elif nom_jugador == "B" or nom_jugador == "b":
                return
            else:
                print("El jugador no se encuentra registrado")
                sleep(3)
        
#3-Opcion 2 (Registrar nombre del jugador)
def Registro_jugador():
    os.system("cls")
    print("-_-_-_Ingresa tu nombre Jugador_-_-_-_\n[-En caso de querer cancelar el registro ingrese [B]-]\n") 
    nombre_jugador = input("Jugador 1 [Alias]: ")
    if nombre_jugador == "B" or nombre_jugador == "b":
        return     
    elif nombre_jugador not in jugadores:
        print("Registrando jugador...%")
        jugadores.append(nombre_jugador)
        sleep(1)
        os.system("cls")
        print(66*"=")
        print(f"Nombre del Jugador: [{nombre_jugador}]\nCantidad de Jugadores Registrados (globalmente, contando CPU): [{len(jugadores)}]")
        print(66*"=")
        pausa = input("...")
        return
    else:
        print(f"\n[El nombre/jugador: [{nombre_jugador}] a registrar se encuentra duplicado]\nPor lo cuál el registro se omitirá...")
        sleep(5)
        os.system("cls")
        
#4-Opcion 3 (Vista de todos los jugadores)
def Vista_jugadores():
    os.system("cls")
    jugadores_nom = len(jugadores)
    if jugadores_nom != 1:
        contador = 0 
        print("-_-_-_JUGADORES REGISTRADOS_-_-_-")
        for elemento in jugadores:
            print(32*"=")
            print(f"{contador}-- [{elemento}]")
            contador +=1
            sleep(0.4)
        else:
            continuar = input("\ningresa Enter para continuar")
    else:
        os.system("cls")
        print("No hay Jugadores registrados aún")
        sleep(2.5)
        return

#5- Opcion 4 (Editar o eliminar nombre del jugador)
def Editar_eliminar_nombre_jugador():
    cantidad_jugadores = len(jugadores)
    if cantidad_jugadores !=1:
        os.system("cls")
        print(25*"-_",end="")
        print(f"\n{50*"="}")
        solicitud_eliminar_o_editar = input(f"[1] Eliminar jugador\n[2] Editar nombre jugador\n{50*"="}\nIngresa [B] para regresar\nOpcion: ").upper()
        if solicitud_eliminar_o_editar == "1":
            os.system
            borrar_jugador = input(f"{50*"="}\nIngresa nombre del jugador a eliminar: ")
            if borrar_jugador in jugadores:
                jugadores.remove(borrar_jugador)
                print(50*"=")
                print("Jugador eliminado")
                pausa = input("...")
                return
            else:
                print(f"{50*"="}\nJugador no encontrado [Vuelve a Intentar]")
                sleep(2)
                Editar_eliminar_nombre_jugador()
        elif solicitud_eliminar_o_editar == "2":
            Editar_jugador = input("Escribe el nombre del jugador existente: ")
            if Editar_jugador in jugadores:
                print(50*"=")
                Contenedor_jugador = jugadores.index(Editar_jugador)
                Editar_jugador_confirmado = input("Elige el nuevo nombre: ")
                print(50*"=")
                jugadores[Contenedor_jugador] = Editar_jugador_confirmado
                mensaje = "Realizando cambios..."
                for letra in mensaje:
                    print(letra,end="",flush=True)
                    sleep(0.1)
                sleep(2)
                return
            else:
                print("El jugador no existe\nNo procede el cambio")
                pausa = input("...")
        elif solicitud_eliminar_o_editar == "B":
            return
        else:
            print("Elige una Opcion validad")
            sleep(2)
            Editar_eliminar_nombre_jugador()
    else:
        os.system("cls")
        print("No hay Jugadores registrados aún")
        sleep(2.5)
        return
#6- Opcion 5 (guarda los datos en un archivo csv)
def Guardado_csv():
    with open ("Video_Juego_Oficial.csv","w", encoding="latin1", newline="") as Archivo_Juego:
        escritor = csv.writer(Archivo_Juego)
        escritor.writerow(["jugadores"])
        for nombre_jugador in jugadores:
            escritor.writerow([nombre_jugador])
    mensaje = "Creando Archivo..."
    for letra in mensaje:
        print(letra,end="",flush=True)
        sleep(0.2)
    print("\nCreado con exito")
    sleep(1)
    return

#7- Opcion 6 (Carga los datos de un csv)
def Cargar_csv():
    try:
        with open("Video_Juego_Oficial.csv","r",encoding="latin1",newline="") as Archivo_juego:
            lector = csv.reader(Archivo_juego)
            next(lector)
            for fila in lector:
                nombre = fila[0]
                if nombre not in jugadores:
                    jugadores.append(nombre)
        mensaje = "Cargando datos..."
        for letra in mensaje:
            print(letra, end="", flush=True)
            sleep(0.2)
        print(f"\n{len(jugadores)-1} datos cargados")   
        sleep(2)

    except FileNotFoundError:
        print("No existe archivo guardado aún")
        sleep(2)
    return 
                
#1-Menu principal
def main():
    while True:
        os.system("cls")
        print("-_-_-_-_-Menu Principal-_-_-_-_-\n")
        print("[1] Jugar")
        print("[2] Registrar jugador")
        print("[3] Lista de jugadores")
        print("[4] Editar/Eliminar jugador")
        print("[5] Guardar Datos ")
        print("[6] Cargar Datos Guardados")
        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        try:
            opcion = int(input("\nIngresa Opcion numerica: ").strip())
        except ValueError:
            os.system("cls")
            print(f"{32*"="}\nFavor de ingresar valor numerico\n{32*"="}")
            sleep(2)
            os.system("cls")
        else:
            if opcion == 1:
                Inicio_juego()
            elif opcion == 2:
                Registro_jugador()
            elif opcion == 3:
                Vista_jugadores()
            elif opcion == 4:
                Editar_eliminar_nombre_jugador()
            elif opcion == 5:
                Guardado_csv()
            elif opcion == 6:
                Cargar_csv()
            else:
                os.system("cls")
                print(f"{32*"="}\nElige una opcion existente\n{32*"="}")
                sleep(2)
                os.system("cls")
        


#Comienzo del inicio del programa (no juego)
print(f"{17*"="}\n== FightingRol ==\n{17*"="}")
sleep(2)
os.system("cls")
if __name__ == "__main__":
    main()