class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
        self.picture = 'none'
        self.studyVal = 0
    
    #getters n setters
    def getTerm(self):
        return self.term
    def getDef(self):
        return self.definition
    def setTerm(self,Nterm):
        self.term = Nterm
    def setTerm(self,Ndef):
        self.definition = Ndef

    def setPicture(self,image):
        self.picture = image

    def getPicture(self):
        return self.picture
    
    def getStudyVal(self):
        return self.studyVal

    #dealing with values for study algorithm
    def addStudyVal(self):
        self.studyVal += 1

    def subtractStudyVal(self):
        if self.studyVal > 0:
            self.studyVal -= 1