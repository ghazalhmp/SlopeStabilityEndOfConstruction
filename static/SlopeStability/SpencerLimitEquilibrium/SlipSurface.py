import random 

class SlipSurface:
    def __init__(self,sizeX,sizeY):
        self.__xCenterCircle=random.randint(0,sizeX)
        self.__yCenterCircle=random.randint(0,sizeY)
        self.__radius=random.randint(0,sizeY - self.__yCenterCircle)
        self.__radius2=self.__radius**2
        self.__xCenterCircle2=self.__xCenterCircle**2
        self.__yCenterCircle2=self.__yCenterCircle**2

    @property
    def xCenterCircle(self):
        return self.__xCenterCircle

    @property
    def yCenterCircle(self):
        return self.__yCenterCircle

    @property
    def xCenterCircle2(self):
        return self.__xCenterCircle2

    @property
    def yCenterCircle2(self):
        return self.__yCenterCircle2

    @property
    def radius(self):
        return self.__radius

    @property
    def radius2(self):
        return self.__radius ** 2