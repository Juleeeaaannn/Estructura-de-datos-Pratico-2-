import numpy as np
from nodo import Nodo
class Lista:
    __arreglo=None
    __tamano=3
    __cabeza=0#apunta siempre al primer elemento cabeza
    __puntero=0#apunta al primer elemento vacio
    __cantidad=0
    def __init__(self):
        self.__arreglo=np.full(self.__tamano,None)
        self.__puntero=0
        self.__cantidad=0
        self.__tamano=3
        self.__cabeza=0
        for i in range(0,self.__tamano):
            nodo1=Nodo()
            nodo1.setDato("A")
            nodo1.setSiguiente(i+1)
            self.__arreglo[i]=nodo1
    def vacia(self):
        return self.__cantidad==0
    def Insertar(self,pos,elemento):
        if self.__tamano > self.__cantidad and pos<self.__tamano:     
            i=0   
            while elemento < self.__arreglo[i].getDato():
                i=i+1
            if pos==0:
                self.__arreglo[self.__puntero].setDato(elemento)
                self.__arreglo[self.__puntero].setSiguiente(-1)
                self.__puntero=i+1
            elif i!=self.__cabeza:
                self.__arreglo[self.__puntero].setDato(elemento)
                self.__arreglo[self.__puntero].setSiguiente(-1)
                self.__arreglo[i-1].setSiguiente(self.__puntero)
                self.__puntero=i+1
                self.__cantidad+=1
            elif i == self.__cabeza:
                self.__arreglo[self.__puntero].setDato(elemento)
                self.__arreglo[self.__puntero].setSiguiente(self.__cabeza)
                self.__cabeza=self.__puntero
        else: raise IndexError
    def Suprimir(self,pos):
        if pos>0 and pos<self.__tamano:
            self.__arreglo[pos].setDato("A")
            self.__arreglo[pos].setSiguiente(self.__puntero)
            self.__puntero=pos
        else: raise ValueError
    def Max(self):
        i=0
        max=""
        while i != self.__tamano:
            if self.__arreglo[i].getDato()>max:
                max=self.__arreglo[i].getDato()
                pos=i
            i+=1
        return max

    def __str__(self):
        return str([[i.getDato(),i.getSiguiente()]for i in self.__arreglo])
if __name__=='__main__':
    lista=Lista()
    print(lista)
    lista.Insertar(0,'D')
    print(lista)
    lista.Insertar(1,"C")
    print(lista)
    lista.Insertar(2,"E")
    print(lista)
    lista.Suprimir(1)
