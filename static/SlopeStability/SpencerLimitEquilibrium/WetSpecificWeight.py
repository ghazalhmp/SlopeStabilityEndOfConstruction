from SpencerLimitEquilibrium.PropertiesMaterials import PropertiesMaterials

class WetSpecificWeight:
    def __init__(self,propertiesMaterials:PropertiesMaterials):
        self.__propertiesMaterials = propertiesMaterials
        self.__Computing()

    def __Computing(self):
        self.__porosityRatioNumerator = self.__propertiesMaterials.gs - self.__propertiesMaterials.gammaSatDivGammaWatter
        self.__porosityRatioDenominator = self.__propertiesMaterials.gammaSatDivGammaWatter - 1
        self.__porosityRatio = self.__porosityRatioNumerator / self.__porosityRatioDenominator
        self.__moistureSoil = self.__porosityRatio / self.__propertiesMaterials.gs
        self.__gammaWet = ( self.__propertiesMaterials.gs * ( 1 + self.__moistureSoil ) / ( 1 + self.__porosityRatio ) ) * ( self.__propertiesMaterials.gammaWatter )

    
    @property
    def propertiesMaterials(self):
        return self.__propertiesMaterials

    @propertiesMaterials.setter
    def propertiesMaterials(self,value):
        self.__propertiesMaterials = value
        self.__Computing()

    @property
    def porosityRatioNumerator(self):
        return self.__porosityRatioNumerator

    @property
    def porosityRatioDenominator(self):
        return self.__porosityRatioDenominator

    @property
    def porosityRatio(self):
        return self.__porosityRatio

    @property
    def moistureSoil(self):
        return self.__moistureSoil

    @property
    def gammaWet(self):
        return self.__gammaWet
 