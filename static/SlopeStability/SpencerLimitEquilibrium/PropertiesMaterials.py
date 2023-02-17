class PropertiesMaterials:
    def __init__(self,height,gammaSat,gs,drainedCohesion,drainedFrictioAngle,bedrockHeight):
        self.height=height
        self.gammaSat=gammaSat
        self.gs = gs
        self.drainedCohesion = drainedCohesion
        self.drainedFrictioAngle = drainedFrictioAngle
        self.bedrockHeight = bedrockHeight
        self.__gammaWatter = 9.81
        self.__gammaSatDivGammaWatter = self.gammaSat / self.__gammaWatter

    @property
    def gammaSatDivGammaWatter(self):
        return self.__gammaSatDivGammaWatter 


    @property
    def gammaWatter(self):
        return self.__gammaWatter    
    