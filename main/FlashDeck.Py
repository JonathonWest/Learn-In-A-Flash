from FlashCard import Flashcard
import os
import csv

class Flashdeck:
    def __init__(self, link = None):
        self.deck = []
        if link != None:
            self.readIn(link)

        

    
    def readIn(self,link):
        link = link.strip("'\"")
        if("txt" in link.split(".")[1]):
            self.readTxt(link)
        else:
            self.readCsv(link)


    def AddCard(self,term,definition):
        newF = Flashcard(term,definition)
        self.deck.append(newF)

    def readTxt(self,link):
        with open(link, 'r') as file:   
            for line in file:
                card = line.split("||")
                self.deck.append(Flashcard(card[0],card[1]))
                
    def readCsv(self,link):
        with open(link, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.deck.append(Flashcard(row[0],row[1]))

    def getCardIndex(self,index):
        return self.deck[index]
    
    def getDeck(self):
        return self.deck
   


if __name__ == "__main__":
    fd = Flashdeck('data.csv')
    