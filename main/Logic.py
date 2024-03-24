from FlashDeck import Flashdeck
from mnemonic import getMn
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
        prompt = "["+term+"] ["+defin+"]"
        return getMn(prompt)

    def testMnem(self,prompt):
        return getMn(prompt)
    
    



if __name__ == "__main__":
    log = Logic()
    print(log.testMnem("[abrir] [to open]"))