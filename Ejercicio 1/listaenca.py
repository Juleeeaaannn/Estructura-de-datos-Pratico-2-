import numpy as np
from nodo import Nodo
class Lista:
    __arreglo=None
    __puntero=0
    __tamano=3
    __cabeza=0#apunta siempre a la cabeza
    __puntero=0#apunta al ultimo dato agregado 
    __cantidad=0
    def __init__(self):
        self.__arreglo=np.full(self.__tamano,None)
        self.__puntero=0
        self.__cantidad=0
        self.__tamano=3
        self.__cabeza=0
        for i in range(0,self.__tamano):
            nodo1=Nodo()
            nodo1.setSiguiente(i+1)
            self.__arreglo[i]=nodo1
    def vacia(self):
        return self.__cantidad==0
    def Insertar(self,elemento,pos=0):
        if self.__tamano>self.__cantidad:
            if pos==0:
                self.__arreglo[0].setSiguiente(-1)
                self.__arreglo[self.__puntero].setSiguiente(0)
                self.__arreglo[0].setDato(elemento)
                self.__cantidad+=1
                self.__puntero=0
            else:
                i=0
                while(pos>0 and pos<=self.__tamano and pos!=i):
                    i+=1
                if(pos>0):
                    self.__arreglo[self.__puntero].setSiguiente(i) #al anterior, en la pos sig se le agrega este enlace al nuevo
                    self.__arreglo[i].setDato(elemento)
                    self.__puntero=i
                    self.__cantidad+=1
                    self.__arreglo[i].setSiguiente(-1)
        else: raise IndexError
    def suprimir(self,pos):
        if pos>0 and pos<=self.__tamano:
            i=0
            while(pos!=i):
                i+=1
            if pos!=i:
                if pos == self.__cabeza:
                    self.__cabeza+=1
                self.__arreglo[i]=None
        else: raise ValueError
        
        
    def __str__(self):
        return str([[i.getDato(),i.getSiguiente()]for i in self.__arreglo])
if __name__=='__main__':
    lista=Lista()
    lista.Insertar('D',0)
    lista.Insertar("C",1)
    lista.Insertar("E",2)
    print(lista)
    lista.suprimir(1)
    print(lista)