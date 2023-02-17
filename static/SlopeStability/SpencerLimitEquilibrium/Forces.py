from SpencerLimitEquilibrium.WetSpecificWeight import WetSpecificWeight
from SpencerLimitEquilibrium.EndCoordinatesOfSlices import EndCoordinatesOfSlices

class Forces:
    def __init__(self,wetSpecificWeight:WetSpecificWeight,endCoordinatesOfSlices:EndCoordinatesOfSlices):
        self.__endCoordinatesOfSlices = endCoordinatesOfSlices
        self.__wetSpecificWeight = wetSpecificWeight
        
    def __Computing(self):
        self.__forceVertical =  self.__wetSpecificWeight.gammaWet * self.__endCoordinatesOfSlices.areaSlice
        self.__forceHorizontal = 0

    @property
    def wetSpecificWeight(self):
        return self.__wetSpecificWeight
    
    @wetSpecificWeight.setter
    def wetSpecificWeight(self,value):
        self.__wetSpecificWeight = value
        self.__Computing()

    @property
    def endCoordinatesOfSlices(self):
        return self.__endCoordinatesOfSlices
    
    @endCoordinatesOfSlices.setter
    def endCoordinatesOfSlices(self,value):
        self.__endCoordinatesOfSlices = value
        self.__Computing()

    @property
    def forceVertical(self):
        return self.__forceVertical
    
    @property
    def forceHorizontal(self):
        return self.__forceHorizontal