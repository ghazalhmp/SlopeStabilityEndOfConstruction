import math
import Forces
import AngleFloorRelativeHorizon
import PropertiesMaterials
import EndCoordinatesOfSlices    

class QFormulation:
    def __init__(self,forces:Forces,angleFloorRelativeHorizon:AngleFloorRelativeHorizon,propertiesMaterials:PropertiesMaterials,endCoordinatesOfSlices:EndCoordinatesOfSlices):
        alpha = angleFloorRelativeHorizon.alphaIndex
        
        fVertical   = forces.forceVertical
        FHorizontal = forces.forceHorizontal
        
        cPrime=propertiesMaterials.drainedCohesion
        phiPrime=propertiesMaterials.drainedFrictioAngle
        
        sin(alpha)=math.sin(alpha)
        cos(alpha)=math.cos(alpha)
        tan(phiPrime)=math.tan(phiPrime)
        deltaL = endCoordinatesOfSlices.deltaLIndex
        u = 0
        
        
        