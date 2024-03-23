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
    
    



if __name__ == "__main__":
    log = Logic()
    print('Hello World')