from os import system, name 
import sys
import time
pr = sys.stdout.write

class Cinta():
    listaCinta = []
    posicion = 0
    estado = '0'

    def __init__(self, cinta):
        cinta = cinta.replace(" ", "_")
        self.listaCinta = list(cinta)

    def moverDerecha(self, estado):
        self.estado = estado
        self.posicion = self.posicion + 1
        if(self.posicion==len(self.listaCinta)):
            #pr("dato ")
            #print(len(self.listaCinta))
            #print(self.posicion)
            self.agregarCampoDerecha()

    def moverIzquierda(self, estado):
        self.estado = estado
        if(self.posicion > 0):
            self.posicion = self.posicion - 1
        if(self.posicion == 0):
            #print("posicion:  %s " % (self.posicion))
            self.agregarCampoIzquierda()

    def obtenerCinta(self):
        self.clear()
        print("************ MOVIMIENTO MAQUINA TURING ***********")
        for i,k in enumerate(self.listaCinta):
            k = k.replace("_", " ")
            pr(k)
        pr("\n");pr(" "*self.posicion);print("^")
        print("estado: %s" % (self.estado))
        pr("\n")
        print("**************************************************")
        return self.listaCinta

    def agregarCampoIzquierda(self):
        auxArray = []
        auxArray.append("_")
        for i, k in enumerate(self.listaCinta):
            auxArray.append(k)
        self.listaCinta = auxArray
        #print("(agregarCampoIzquierda) posicion:  %s " % (self.posicion))
        #print(self.listaCinta)

    def agregarCampoDerecha(self):
        self.listaCinta.append("_")
        #print(self.listaCinta)

    def validarListavacia(self):
        if(len(self.listaCinta) < 1):
            self.agregarCampoIzquierda()
            self.posicion = 0

    def obtenerDato(self):
        #print(self.posicion)
        return self.listaCinta[self.posicion]
    
    def cambiarDato(self, dato):
        self.listaCinta[self.posicion] = dato
    
    def validarMovimiento(self, dir, est):
        if(dir == 'R'):
            self.moverDerecha(est)
        elif (dir == 'L'):
            self.moverIzquierda(est)

    def clear(self): 
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear') 

archivoEntrada = sys.argv[1]
archivoCinta = sys.argv[2]
fEntrada = open(archivoEntrada, "r")
fCinta = open(archivoCinta, "r")
cinta = ""
entrada = ""
existe = True
if (fEntrada.mode == "r" and fCinta.mode == "r"):
    cinta = fCinta.read()
    entrada = fEntrada.read()
entrada = entrada.splitlines()
cinta = Cinta(cinta)
cinta.obtenerCinta()
cinta.validarListavacia()
cinta.obtenerCinta()

while True:
    existe = True
    contador = 0
    while(True):
        orden = entrada[contador].split(" ")
        #print("mior %s %s " % (orden[1],contador))
        if(orden[0] == cinta.estado and orden[1] == cinta.obtenerDato()):
            cinta.cambiarDato(orden[2])
            cinta.validarMovimiento(orden[3], orden[4])
            cinta.obtenerCinta()
            time.sleep(0.1)
            break
        else: 
            contador = contador + 1
        
        if(contador == len(entrada)):
            existe = False
            break

    if(not existe):
        break
