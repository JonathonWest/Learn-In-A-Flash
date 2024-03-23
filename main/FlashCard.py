class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
        self
    
    #getters n setters
    def getTerm(self):
        return self.term
    def getDef(self):
        return self.definition
    def setTerm(self,Nterm):
        self.term = Nterm
    def setTerm(self,Ndef):
        self.definition = Ndef