from FlashDeck import Flashdeck
from mnemonic import getMn
from hint import getHint
class Logic:
    

    def __init__(self):
        self.deck = Flashdeck()
        

    def setDeck(self,link = None):
        self.deck.readIn(link)
    def addCard (self, term, definition):
        self.deck.AddCard(term,definition)
    def DeckSize(self):
        return len(self.deck.getDeck())
    

    def getCard(self,indx):
        return self.deck.getCardIndex(indx)
    

    def getInfo(self,indx,side):
        card = self.getCard(indx)
        if side == True:
            return card.getTerm()
        if side == False:
            return card.getDef()
        
    def getmnem(self,indx):
        term = self.getInfo(indx,True)
        defin = self.getInfo(indx,False)
        if (len(term) < 3) or (len(defin) < 3):
            return "length of term or definition too short"
        else:
            prompt = "["+term+"] ["+defin+"]"
            return getMn(prompt)
    def gethint(self,indx):
        term = self.getInfo(indx,True)
        defin = self.getInfo(indx,False)
        if (len(term) < 3) or (len(defin) < 3):
            return "length of term or definition too short"
        else:
            prompt = "["+term+"] ["+defin+"]"
            return getHint(prompt)

    def testMnem(self,prompt):
        return getMn(prompt)
    
    def getStr(self):
        st= ""
        for card in self.deck.getDeck():
            st+= card.getTerm()
            st+=" || "
            st+= card.getDef()
            st+="\n"
        return st