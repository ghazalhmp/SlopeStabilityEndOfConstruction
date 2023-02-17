import math
from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometry import CharacteristicsOfSlopeGeometry
from SpencerLimitEquilibrium.SlipSurface import SlipSurface
class ImportantCoordinatesCircle:
    def __init__(self,slipSurface:SlipSurface,characteristicsOfSlopeGeometry:CharacteristicsOfSlopeGeometry):
        self.__slipSurface = slipSurface
        self.__characteristicsOfSlopeGeometry = characteristicsOfSlopeGeometry
        self.__Computing()

    def __Computing(self):
        intersectionHorizontalAxisAndSlipSurface = math.sqrt( self.__slipSurface.radius2 - self.__slipSurface.xCenterCircle2 ) + self.__slipSurface.yCenterCircle
        intersectionEmbankmentAndSlipSurface = math.sqrt( self.__slipSurface.radius2 - ( (self.__characteristicsOfSlopeGeometry.characteristicsOfSlopeGeometryAttribute.height - self.__slipSurface.xCenterCircle) **2) ) 

        self.__intersectionHorizontalAxisAndSlipSurfaceLeft  = -intersectionHorizontalAxisAndSlipSurface
        self.__intersectionHorizontalAxisAndSlipSurfaceRight = intersectionHorizontalAxisAndSlipSurface
       
        self.__intersectionEmbankmentAndSlipSurface1 = -intersectionEmbankmentAndSlipSurface + self.__slipSurface.yCenterCircle
        self.__intersectionEmbankmentAndSlipSurface2 = intersectionEmbankmentAndSlipSurface + self.__slipSurface.yCenterCircle

        self.__intersectionEmbankmentAndSlipSurface = 0

        if (self.__intersectionEmbankmentAndSlipSurface1 > self.__characteristicsOfSlopeGeometry.heightDivSlope) and (self.__intersectionEmbankmentAndSlipSurface1 < self.__characteristicsOfSlopeGeometry.sideSmallSumHeightDivSlope):
           self.__intersectionEmbankmentAndSlipSurface = self.__intersectionEmbankmentAndSlipSurface1
       
        if (self.__intersectionEmbankmentAndSlipSurface2 > self.__characteristicsOfSlopeGeometry.heightDivSlope) and (self.__intersectionEmbankmentAndSlipSurface2 < self.__characteristicsOfSlopeGeometry.sideSmallSumHeightDivSlope):
            self.__intersectionEmbankmentAndSlipSurface = self.__intersectionEmbankmentAndSlipSurface2

    @property
    def slipSurface(self):
        return self.__slipSurface
    
    @property
    def characteristicsOfSlopeGeometry(self):
        return self.__characteristicsOfSlopeGeometry


    @slipSurface.setter
    def slipSurface(self,value):
        self.__slipSurface = value
        self.__Computing()
    
    @characteristicsOfSlopeGeometry.setter
    def characteristicsOfSlopeGeometry(self,value):
        self.__characteristicsOfSlopeGeometry= value
        self.__Computing()
        


    @property
    def intersectionHorizontalAxisAndSipSurfaceLeft(self):
        return self.__intersectionHorizontalAxisAndSlipSurfaceLeft
    
    @property
    def intersectionHorizontalAxisAndSlipSurfaceRight(self):
        return self.__intersectionHorizontalAxisAndSlipSurfaceRight
    
    @property
    def intersectionEmbankmentAndSlipSurface(self):
        return self.__intersectionEmbankmentAndSlipSurface

        