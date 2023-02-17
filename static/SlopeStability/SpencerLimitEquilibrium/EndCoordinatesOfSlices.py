import math
import array as arr
from SpencerLimitEquilibrium.ImportantCoordinatesCircle import ImportantCoordinatesCircle
from SpencerLimitEquilibrium.NumberOfSlices import NumberOfSlices
from SpencerLimitEquilibrium.Widthslices import Widthslices
from SpencerLimitEquilibrium.PropertiesMaterials import PropertiesMaterials
from SpencerLimitEquilibrium.SlipSurface import SlipSurface
from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometry import CharacteristicsOfSlopeGeometry
from SpencerLimitEquilibrium.AngleFloorRelativeHorizon import AngleFloorRelativeHorizon

class CoordinatesOfSlice:
    def __init__(self,x,y1,y2,areaSlices,data):
        self.__x = x 
        self.__y1 = y1
        self.__y2 = y2
        self.__areaSlices = areaSlices
        self.__data = data
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y1(self):
        return self.__y1

    @property
    def y2(self):
        return self.__y2

    @property
    def areaSlices(self):
        return self.__areaSlices

class EndCoordinatesOfSlices:
    def __init__(self,angleFloorRelativeHorizon:AngleFloorRelativeHorizon,importantCoordinatesCircle:ImportantCoordinatesCircle,numberOfSlices:NumberOfSlices,widthslices:WidthSlices,propertiesMaterials:PropertiesMaterials,slipSurface:SlipSurface,characteristicsOfSlopeGeometry:CharacteristicsOfSlopeGeometry):
        self.__importantCoordinatesCircle = importantCoordinatesCircle
        self.__numberOfSlices = numberOfSlices
        self.__widthslices = widthslices
        self.__propertiesMaterials = propertiesMaterials
        self.__slipSurface = slipSurface
        self.__characteristicsOfSlopeGeometry = characteristicsOfSlopeGeometry
        self.__angleFloorRelativeHorizon = AngleFloorRelativeHorizon
        self.__x = []
     
     
                
    def __Computing(self):
        for indexSlice in range (1,self.numberOfSlices.numberSlicesFirstPiece):
            for index in range (self.__importantCoordinatesCircle.intersectionHorizontalAxisAndSlipsurfaceLeft,0):
                xIndex = self.__importantCoordinatesCircle.intersectionHorizontalAxisAndSlipsurfaceLeft + ( indexSlice * self.__widthslices.widthFirstPiece)
                
                sqr = (self.__slipSurface.radius2) - ((xIndex-self.__slipSurface.xCenterCircle)**2)
                
                y11Index=  math.sqrt(sqr) + self.__slipSurface.yCenterCircle
                y12Index= -math.sqrt(sqr) + self.__slipSurface.yCenterCircle

                y1Index = y11Index
                if (y11Index < 0) and (y12Index < 0):
                    raise  ("Invalid Y", 0) 
                elif (y11Index >= 0) and (y12Index >= 0) :
                    if y11Index < y12Index :
                        y1Index = y11Index
                    else :
                        y1Index = y12Index
                else :
                    if y11Index < 0:
                        y1Index = y11Index
                    else :
                        y1Index = y12Index

                y2 = self.__characteristicsOfSlopeGeometry.slope * xIndex

                if (index == 0):
                    areaSlice = ( 0 + y2 ) / 2
                    
                    deltaLIndex=(self.__widthslices.widthFirstPiece) / math.cos(self.__angleFloorRelativeHorizon)
                    CoordinatesOfSlice coordinatesOfSlice(xIndex,y1Index,y2,areaSlice,deltaLIndex)

                    self.__x.append(coordinatesOfSlice)

                else :
                    yLast = self.__x[len(self.__x)]

                    areaSlice = ( yLast.y1 + y2 ) / 2
                    
                    deltaLIndex=(self.__widthslices.widthFirstPiece)/math.cos(self.__angleFloorRelativeHorizon)
                    CoordinatesOfSlice coordinatesOfSlice(xIndex,y1Index,y2,areaSlice,deltaLIndex)

                    self.__x.append(coordinatesOfSlice)
                
        for indexSlice in range (1, self.numberOfSlices.numberSlicesSecendPiece):
            for index in range (0, self.__characteristicsOfSlopeGeometry.heightDivSlope ):
                xIndex= indexSlice * self.__widthslices.widthSecendPiece

                sqr = (self.__slipSurface.radius2) - ((xIndex-self.__slipSurface.xCenterCircle)**2)

                y11Index =  math.sqrt(sqr) + self.__slipSurface.yCenterCircle
                y12Index = -math.sqrt(sqr) + self.__slipSurface.yCenterCircle

                y1Index = y11Index
                if (y11Index < 0) and (y12Index < 0):
                    raise  ("Invalid Y", 0) 
                elif (y11Index >= 0) and (y12Index >= 0) :
                    if y11Index < y12Index:
                        y1Index = y11Index
                    else :
                        y1Index = y12Index
                else :
                    if y11Index < 0:
                        y1Index = y11Index
                    else :
                        y1Index = y12Index
                
                y2Index = self.__characteristicsOfSlopeGeometry.slope * xIndex
                y1Index = y1Index + y2Index

                yLast = self.__x[len(self.__x)]

                areaSlice=( ( yLast.y1 + y1Index) / 2 ) * self.__widthslices.widthSecendPiece + ( ( yLast.y2 + y2Index) / 2 ) * self.__widthslices.widthSecendPiece
                deltaLIndex=(self.__widthslices.widthSecendPiece)/math.cos(self.__angleFloorRelativeHorizon)

                CoordinatesOfSlice coordinatesOfSlice(xIndex,y1Index,y2Index,areaSlice,deltaLIndex)
                self.__x.append(coordinatesOfSlice)


        for indexSlice in range (1,self.__numberOfSlices.numberSlicesThirdPiece):
            for index in range ( self.__heightDivSlope,ImportantCoordinatesCircle, self.__intersectionEmbankmentAndSlipSurface ):
                xIndex = self.__characteristicsOfSlopeGeometry.heightDivSlope + indexSlice * self.__widthslices.widthThirdPiece

                sqr = (self.__slipSurface.radius2) - ((xIndex-self.__slipSurface.xCenterCircle)**2)

                y11Index = math.sqrt(sqr) + self.__slipSurface.yCenterCircle
                y12Index = -math.sqrt(sqr) + self.__slipSurface.yCenterCircle

                y1Index = y11Index
                if (y11Index < 0) and (y12Index < 0):
                    raise  ("Invalid Y", 0) 
                elif (y11Index >= 0) and (y12Index >= 0) :
                    if y11Index < y12Index :
                        y1Index = y11Index
                    else :
                        y1Index = y12Index
                else :
                    if y11Index < 0:
                        y1Index = y11Index
                    else :
                        y1Index = y12Index

                y2Index = self.__characteristicsOfSlopeGeometry.slope * xIndex
                yIndex = y1Index + y2Index

                yLast = self.__x[len(self.__x)]
                
                areaSlice = ( ( yLast.y1 + y1Index ) / 2 ) * self.__widthslices.widthThirdPiece + ( ( yLast.y2 + y2Index ) / 2 ) * self.__widthslices.widthThirdPiece
                deltaLIndex = (self.__widthslices.widthThirdPiece)/math.cos(self.__angleFloorRelativeHorizon)
                CoordinatesOfSlice coordinatesOfSlice(xIndex,y1Index,y2Index,areaSlice,deltaLIndex)

                self.__x.append(coordinatesOfSlice)