import math
from SpencerLimitEquilibrium.ImportantCoordinatesCircle import ImportantCoordinatesCircle
from SpencerLimitEquilibrium.NumberOfSlices import NumberOfSlices
from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometry import CharacteristicsOfSlopeGeometry

class WidthSlices:
    def __init__(self,importantCoordinatesCircle:ImportantCoordinatesCircle,numberOfSlices:NumberOfSlices,characteristicsOfSlopeGeometry:CharacteristicsOfSlopeGeometry):
        self.__importantCoordinatesCircle = importantCoordinatesCircle
        self.__numberOfSlices = numberOfSlices
        self.__characteristicsOfSlopeGeometry = characteristicsOfSlopeGeometry
        self.__Computing()

    def __Computing(self):
        numeratorFirstPiece = 0 - self.__importantCoordinatesCircle.intersectionHorizontalAxisAndSipSurfaceLeft
        numeratorSecendPiece= self.__characteristicsOfSlopeGeometry.characteristicsOfSlopeGeometryAttribute.height / math.tan(self.__characteristicsOfSlopeGeometry.beta)
        numeratorThirdPiece = self.__importantCoordinatesCircle.intersectionEmbankmentAndSlipSurface - numeratorSecendPiece
        self.__widthFirstPiece = numeratorFirstPiece / self.__numberOfSlices.numberSlicesFirstPiece
        self.__widthSecendPiece = numeratorSecendPiece / self.__numberOfSlices.numberSlicesSecendPiece
        self.__widthThirdPiece = numeratorThirdPiece / self.__numberOfSlices.numberSlicesThirdPiece

    @property
    def importantCoordinatesCircle(self):
        return self.__importantCoordinatesCircle        
    
    @property
    def numberOfSlices(self):
        return self.__numberOfSlices        

    @property
    def characteristicsOfSlopeGeometry(self):
        return self.__characteristicsOfSlopeGeometry        

    @importantCoordinatesCircle.setter
    def importantCoordinatesCircle(self,value):
        self.__importantCoordinatesCircle = value  
        self.__Computing()
    
    @numberOfSlices.setter
    def numberOfSlices(self,value):
        self.__numberOfSlices = value      
        self.__Computing()

    @characteristicsOfSlopeGeometry.setter
    def characteristicsOfSlopeGeometry(self,value):
        self.__characteristicsOfSlopeGeometry = value
        self.__Computing()



    @property
    def widthFirstPiece(self):
        return __widthFirstPiece        

    @property
    def widthSecendPiece (self):
        return __widthSecendPiece 

    @property
    def widthThirdPiece(self):
        return __widthThirdPiece 