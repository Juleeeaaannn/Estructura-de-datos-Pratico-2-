class Nodo:
    __elemento=None
    __siguiente=None
    def __init__(self, personal):
        self.elemento=personal
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.elemento