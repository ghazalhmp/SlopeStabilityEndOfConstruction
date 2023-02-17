import math 
from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometryAttribute import CharacteristicsOfSlopeGeometryAttribute

class CharacteristicsOfSlopeGeometry:
    def __init__(self,characteristicsOfSlopeGeometryAttribute:CharacteristicsOfSlopeGeometryAttribute):
        self.__characteristicsOfSlopeGeometryAttribute = characteristicsOfSlopeGeometryAttribute
        self.__Computing()

    def __Computing(self):
        self.__slope = 1 / 2.6
        self.__sideSmall = (0.2 * self.__characteristicsOfSlopeGeometryAttribute.height) + 3
        self.__sideBig = self.__sideSmall + ((2 * self.__characteristicsOfSlopeGeometryAttribute.height) / self.__slope)
        self.__beta = math.atan(self.__slope)
        self.__maxRange = self.__characteristicsOfSlopeGeometryAttribute.height / math.tan(self.__beta)
        self.__heightDivSlope = self.__characteristicsOfSlopeGeometryAttribute.height / self.__slope
        self.__sideSmallSumHeightDivSlope =  self.__sideSmall + self.__heightDivSlope

    @property
    def sideSmallSumHeightDivSlope(self):
        return self.__sideSmallSumHeightDivSlope

    @property
    def heightDivSlope(self):
        return self.__heightDivSlope


    @property
    def slope(self):
        return self.__slope

    @property
    def sideSmall(self):
        return self.__sideSmall
        
    @property
    def sideBig(self):
        return self.__sideBig

    @property
    def beta(self):
        return self.__beta

    @property
    def maxRange(self):
        return self.__maxRange

    @property
    def characteristicsOfSlopeGeometryAttribute(self):
        return self.__characteristicsOfSlopeGeometryAttribute

    @characteristicsOfSlopeGeometryAttribute.setter
    def characteristicsOfSlopeGeometryAttribute(self,value):
        self.__characteristicsOfSlopeGeometryAttribute = value
        self.__Computing()