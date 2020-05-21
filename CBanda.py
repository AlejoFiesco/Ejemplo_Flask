import abc
from abc import ABC
import random

class Instrumento ( ABC ):
    def __init__(self):
        __metaclass__ = ABCMeta

    @abc.abstractmethod
    def Preparar(self):
        pass

    @abc.abstractmethod
    def Tocar(self):
        pass

class Guitarra (Instrumento):
    def __init__(self):
        pass

    def Preparar(self):
        return 'Preparando Guitarra'

    def Tocar(self):
        return 'Tocando Guitarra'

class Flauta (Instrumento):
    def __init__(self):
        pass

    def Preparar(self):
        return 'Preparando Flauta'

    def Tocar(self):
        return 'Tocando Flauta'

class Organeta (Instrumento):
    def __init__(self):
        pass

    def Preparar(self):
        return 'Preparando Organeta'

    def Tocar(self):
        return 'Tocando Organeta'

class Tambor (Instrumento):
    def __init__(self):
        pass

    def Preparar(self):
        return 'Preparando Tambor'

    def Tocar(self):
        return 'Tocando Tambor'

class Trompeta (Instrumento):
    def __init__(self):
        pass

    def Preparar(self):
        return 'Preparando Trompeta'

    def Tocar(self):
        return 'Tocando Trompeta'

class Musico ():
    def __init__(self,inst):
        self.inst = inst

    def Prepararinstr(self):
        return self.inst.Preparar()
    
    def Tocarinstr(self):
        return self.inst.Tocar()

class Banda ():

    musico = list()

    def __init__(self):    
        pass    

    def AsignarInst(self):
        self.cmusicos = random.randint(5,10)
        for i in range(self.cmusicos):
            inst = random.randint(1, 5)
            if inst == 1:
                instru1 = Guitarra()
                self.musico.append(Musico(instru1))
            if inst == 2:
                instru2 = Flauta()
                self.musico.append(Musico(instru2))
            if inst == 3:
                instru3 = Tambor()
                self.musico.append(Musico(instru3))
            if inst == 4:
                instru4 = Trompeta()
                self.musico.append(Musico(instru4))
            if inst == 5:
                instru5 = Organeta()
                self.musico.append(Musico(instru5))        





        
