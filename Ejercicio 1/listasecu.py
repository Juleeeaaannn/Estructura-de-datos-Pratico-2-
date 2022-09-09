# Ejercicio Nº 1
#     a) Construya el T.A.D Lista. Representación secuencial y encadenada por posición.
#     b) A partir del inciso a, realice las modificaciones necesarias para disponer del T.A.D lista por contenido.
# Insertar(X,L,p)
# Suprimir(X,L,p)
# Recuperar(L,p,X)
# Buscar(X,L,p)
# Primer_elemento (L,X)
# Ultimo_elemento (L,X)
# Siguiente(L,p,p1)
# Anterior(L,p,p1)
# Recorrer(L)
# Vacia()
import numpy as np
class ListaSecu:
    __lista=None
    __cantidad=0
    __tamano=0
    def __init__(self,tamano):
        self.__lista=np.full(tamano,None)
        self.__tamano=tamano
        self.__cantidad=0
    def Insertar(self,elemento,pos=0):
        j=0
        if self.Vacia():
            self.__lista[0]=elemento
            self.__cantidad+=1
        elif pos>=0 and pos<self.__tamano and self.__cantidad<self.__tamano:
            j=self.__tamano-1
            for i in range(pos,self.__tamano):
                self.__lista[j]=self.__lista[j-1]
                j-=1
            self.__lista[pos]=elemento
            self.__cantidad+=1
        else:
            print("La lista esta llena!")
    def Suprimir(self,pos):
        if pos>=0 and pos<self.__tamano-1:
            j=pos
            for i in range(pos,self.__tamano):
                if j<self.__tamano-1:
                    self.__lista[j]=self.__lista[j+1]
                else:
                    self.__lista[self.__tamano-1]=None
                    self.__cantidad-=1
                j+=1
    def Recuperar(self,pos):
        retorna=None
        if pos>=0 and pos<self.__tamano-1:
            retorna=self.__lista[pos]
        return retorna
    def Buscar(self,elemento):
        for i in range(0,self.__cantidad-1):
            if self.__lista[i]==elemento:
                print(f"se encuentra en la posicion {i}")
    def PrimerElemento(self):
        return self.__lista[0]
    def UltimoElemento(self):
        return self.__lista[self.__cantidad-1]
    def PosicionSig(self,pos):
        if pos>=0 and pos<self.__tamano-1:
            retorna=self.__lista[pos+1]
        return retorna
    def PosicionAnt(self,pos):
        if pos>=0 and pos<self.__tamano-1:
            retorna=self.__lista[pos-1]
        return retorna
    def Recorrer(self,pos):
        for i in self.__lista :
            print(i)
    def Vacia(self):
        return self.__cantidad==0
if __name__=='__main__':
    lista=ListaSecu(5)
    lista.Insertar(1)
    lista.Insertar(2,1)
    lista.Insertar(3,2)
    lista.Insertar(4,3)
    lista.Insertar(5,4)
    lista.Mostrar()
    lista.Suprimir(2)
    lista.Mostrar()
    lista.Insertar(2,1)
    lista.Mostrar()
    