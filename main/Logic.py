from FlashDeck import Flashdeck

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
        



    
    



if __name__ == "__main__":
    log = Logic()
    print('Hello World')