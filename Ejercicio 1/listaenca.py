import numpy as np
from nodo import Nodo
class Lista:
    __arreglo=None
    __puntero=0
    __tamano=3
    __cabeza=None
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
    def Insertar(self,elemento,pos=0):
        if pos==0:
            self.__arreglo[0].setDato(elemento)
            self.__arreglo[0].setSiguiente(-1)
        elif self.__tamano>self.__cantidad:
                ant=self.__arreglo[self.__cabeza]
                act=self.__arreglo[self.__cabeza]
                while(pos>0 and pos<=self.__tamano and pos!=act.getSiguiente()):
                    ant.setDato(act)
                    act=act.getSiguiente()
                if(pos>0):
                    act.setDato(elemento)
                    self.__puntero=self.__cantidad+1
                    if self.__tamano==self.__cantidad:
                        act.setSiguiente(-1)
                    self.__cantidad+=1

        else: raise IndexError
    def __str__(self) -> str:
        return str([[i.getDato(),i.getSiguiente()]for i in self.__arreglo])
if __name__=='__main__':
    lista=Lista()
    lista.Insertar('D',0)
    lista.Insertar("C",1)
    print(lista)


