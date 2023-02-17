import math
from SpencerLimitEquilibrium.EndCoordinatesOfSlices import EndCoordinatesOfSlices
from SpencerLimitEquilibrium.CharacteristicsOfSlopeGeometryAttribute import CharacteristicsOfSlopeGeometryAttribute

class AngleFloorRelativeHorizon:
    def __init__(self,numberOfSlices:NumberOfSlices,coordinatesOfSlices:EndCoordinatesOfSlices):
        for index in range (1,numberOfSlices.numberSlices):
            self.__alphaIndex=math.atan((coordinatesOfSlices.y[index]+ coordinatesOfSlices.y[index-1])/( coordinatesOfSlices.x[index]+ coordinatesOfSlices.x[index-1]))
