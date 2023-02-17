class NumberOfSlices:
    def __init__(self,numberSlicesFirstPiece,numberSlicesSecendPiece,numberSlicesThirdPiece):
        self.__numberSlicesFirstPiece = numberSlicesFirstPiece
        self.__numberSlicesSecendPiece = numberSlicesSecendPiece
        self.__numberSlicesThirdPiece = numberSlicesThirdPiece
        self.__Computing()

    def __Computing(self):
        self.__numberOfSlices = self.__numberSlicesFirstPiece + self.__numberSlicesSecendPiece + self.__numberSlicesThirdPiece

    @property    
    def numberOfSlices(self):
        return self.__numberOfSlices

    @property    
    def numberSlicesFirstPiece(self):
        return self.__numberSlicesFirstPiece

    @numberSlicesFirstPiece.setter    
    def numberSlicesFirstPiece(self,value):
        self.__numberSlicesFirstPiece = value
        self.__Computing()

    @property
    def numberSlicesSecendPiece(self):
        return self.__numberSlicesSecendPiece

    @numberSlicesSecendPiece.setter
    def numberSlicesSecendPiece(self,value):
        self.__numberSlicesSecendPiece = value
        self.__Computing()

    @property
    def numberSlicesThirdPiece(self):
        return self.__numberSlicesThirdPiece

    @numberSlicesThirdPiece.setter
    def numberSlicesThirdPiece(self,value):
        self.__numberSlicesThirdPiece = value
        self.__Computing()

