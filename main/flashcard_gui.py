import tkinter as tk
import tkinter.font as tkf
from Logic import Logic
import pyttsx3
from tkinter import PhotoImage
from imageGet import getTitle,getloadanstufFlash
import random


LARGE_FONT = ("Verdana", 30)
SMOL_FONT = ("Verdana", 10)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        

        self.logic = Logic()

        # Create and configure container
        container = tk.Frame(self, width=1280, height=720, background="medium blue")
        # container.pack(side = "top", fill = "both", expand = True) 
        container.grid(sticky='nswe')
        container.grid_propagate(0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Set up frames dictionary
        self.frames = {}
        self.PAGES = (Title, Load, Select, Learn, Test)
        for page in self.PAGES:
            frame = page(container, self, logic=self.logic)
            frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            self.frames[page] = frame
        

        

        self.show_page(Title)
  
    def show_page(self, frame):
        self.frames[frame].tkraise()

class Title(tk.Frame):
    def __init__(self, parent, controller,logic):
        tk.Frame.__init__(self, parent, background="medium blue")
        
        self.logic = logic
        self.err = False
        self.controller = controller
        self.ima = getTitle()
        self.loaf,self.studf = getloadanstufFlash()
        
        label = tk.Label(self,image=self.ima,bg='medium blue')
        label.place(relx=0.5, rely=0.3, anchor="center")
        load = tk.Button(self, image=self.loaf, command=lambda: controller.show_page(Load),bg='medium blue',bd=0,activebackground="medium blue")
        load.place(relx=0.25, rely=0.62, anchor="center")

        self.errl = tk.Label(self, text="",fg="red" , font=SMOL_FONT, bg='medium blue',height=1, borderwidth="2")
        self.errl.place(relx=0.75, rely=0.4, anchor="center")
        start = tk.Button(self, text="Study Flashcards", command=self.test, 
                              bd=10, bg="tomato")
        
  
        start.place(relx=0.75, rely=0.62, anchor="center")
        
        


    def test(self):
        if (self.logic.DeckSize()) == 0:
            self.errl.configure(text="please enter flashcard data before studying")
        else:
            self.controller.show_page(Select)


class Load(tk.Frame):
    def __init__(self, parent, controller,logic):
        tk.Frame.__init__(self, parent)
        
        self.logic = logic

        self.file_name = ""


        file_label = tk.Label(self, text="Input file name here:", fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=2, borderwidth="3", relief="groove")
        file_label.place(relx=0.5, rely=0.05, anchor="center")
        self.file_input = tk.Text(self, width=75, height=3)
        self.file_input.place(relx=0.4, rely=0.1, anchor="center")
        enter = tk.Button(self, text="Enter  Flashcard File Path", command=self.get_input,
                          bd=10, bg="orange", activebackground="orangered")
        enter.place(relx=0.7, rely=0.1, anchor="center")

        ret = tk.Button(self, text="Return to Main", command=lambda: controller.show_page(Title), 
                              bd=10, bg="orange", activebackground="orangered")
        ret.place(relx=0.25, rely=0.6, anchor="center")

        manual_label = tk.Label(self, text="Input Flashcards Manually", fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=2, borderwidth="3", relief="groove")
        manual_label.place(relx=0.5, rely=0.4, anchor="center")

        term_label = tk.Label(self, text="Term here", fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=2, borderwidth="3", relief="groove")
        term_label.place(relx=0.4, rely=0.5, anchor="center")

        defi_label = tk.Label(self, text="Definition here", fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=2, borderwidth="3", relief="groove")
        defi_label.place(relx=0.6, rely=0.5, anchor="center")

        self.term = tk.Text(self, width=30, height=3)
        self.term.place(relx=0.4, rely=0.6, anchor="center")
        self.defin = tk.Text(self, width=30, height=3)
        self.defin.place(relx=0.6, rely=0.6, anchor="center")
        done = tk.Button(self, text="Submit Flashcard", command=self.get_term,
                         bd=10, bg="royalblue", activebackground="mediumblue")
        done.place(relx=0.48, rely=0.65)

    def get_input(self):
        self.file_name = self.file_input.get(1.0, "end-1c")
        self.file_input.delete(1.0, "end-1c")
        self.logic.setDeck(self.file_name)
        


    def get_term(self):
        new_term = self.term.get(1.0, "end-1c")
        new_def = self.defin.get(1.0, "end-1c")
        if len(new_term) != 0 and len(new_def) !=0:
            new_term = self.term.get(1.0, "end-1c")
            self.term.delete(1.0, tk.END)
            new_def = self.defin.get(1.0, "end-1c")
            self.defin.delete(1.0, tk.END)
            self.logic.addCard(new_term,new_def)

class Select(tk.Frame):
    def __init__(self, parent, controller, logic):
        tk.Frame.__init__(self, parent)
        

        learn = tk.Button(self, text="Learn", command=lambda: controller.show_page(Learn),
                          bd=20, bg="orange", activebackground="orangered")
        learn.place(relx=0.5, rely=0.3, anchor="center")
        test = tk.Button(self, text="Test", command=lambda: controller.show_page(Test),
                          bd=20, bg="orange", activebackground="orangered")
        test.place(relx=0.5, rely=0.7, anchor="center")

class Learn(tk.Frame):
    def __init__(self, parent, controller, logic):
        tk.Frame.__init__(self, parent)
        
        self.logic = logic
        self.side = True #t for term d for def (flip)
        self.deckIndx = 0
        self.text = 'Flip to Begin'
        self.mnem = ""

        self.card = tk.Label(self, text=self.text, fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=15, width=60, borderwidth="3", relief="groove")
        self.card.place(relx=0.5, rely=0.2, anchor="center")

        self.mnemo = tk.Label(self, text=self.mnem, fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=15, width=90, borderwidth="3", relief="groove",wraplength=400)
        self.mnemo.place(relx=0.5, rely=0.8, anchor="center")

        getmnem = tk.Button(self, text="Get Mnemonic", command=self.fillmnem,
                              bd=10, width=20, bg="blue", activebackground="navy")
        getmnem.place(relx=0.5, rely=0.9, anchor="center")


        flip = tk.Button(self, text="Flip Button", command=self.flip,
                              bd=10, width=20, bg="blue", activebackground="navy")
        flip.place(relx=0.5, rely=0.4, anchor="center")
        next_card = tk.Button(self, text="Next", command=self.next,
                              bd=10, bg="orange", activebackground="orangered")
        next_card.place(relx=0.6, rely=0.5, anchor="center")
        back = tk.Button(self, text="Back", command=self.back,
                              bd=10, bg="orange", activebackground="orangered")

        back.place(relx=0.4, rely=0.5, anchor="center")

        Hear = tk.Button(self, text="Hear the Term", command=self.sound,
                              bd=10, bg="orange", activebackground="orangered")
        Hear.place(relx=0.5, rely=0.7, anchor="center")

        load = tk.Button(self, text="Return to Main", command=lambda: controller.show_page(Title), 
                              bd=10, bg="orange", activebackground="orangered")
        load.place(relx=0.25, rely=0.6, anchor="center")


    def fillmnem(self):
        self.mnem = self.logic.getmnem(self.deckIndx)
        self.mnemo.configure(text=self.mnem)


    def flip(self):

        if self.side:
            self.side =  False
        elif self.side == False:
            self.side = True
        
        self.update()
        # Flip flashcard self.errl.configure(text="please enter flashcard data before studying")
    
    def next(self):
        self.deckIndx+=1
        if self.deckIndx >= self.logic.DeckSize():
            self.deckIndx = 0
        self.update()
    
    def back(self):
        self.deckIndx-=1
        if self.deckIndx < 0:
            self.deckIndx = self.logic.DeckSize() -1
        self.update()

    def update(self):
        self.mnem = ""
        self.mnemo.configure(text=self.mnem)
        self.text = self.logic.getInfo(self.deckIndx,self.side)
        self.card.configure(text=self.text)
    
    def sound(self):
        engine = pyttsx3.init()
        engine.say(self.text)
        engine.runAndWait()


class Test(tk.Frame):
    def __init__(self, parent, controller, logic):
        tk.Frame.__init__(self, parent)
        
        self.logic = logic
        self.side = True #t for term d for def (flip)
        self.deckIndx = 0
        self.text = 'Flip to Begin'
        

        self.card = tk.Label(self, text=self.text, fg="purple4", bg="steelblue", font=SMOL_FONT, 
                              height=15, width=60, borderwidth="3", relief="groove")
        self.card.place(relx=0.5, rely=0.2, anchor="center")

        flip = tk.Button(self, text="Flip Button", command=self.flip,
                              bd=10, width=20, bg="blue", activebackground="navy")
        flip.place(relx=0.5, rely=0.4, anchor="center")
        Correct_card = tk.Button(self, text="Correct", command=self.correct,
                              bd=10, bg="orange", activebackground="orangered")
        Correct_card.place(relx=0.6, rely=0.5, anchor="center")
        Incorrect = tk.Button(self, text="Incorrect", command=self.wrong,
                              bd=10, bg="orange", activebackground="orangered")
        Incorrect.place(relx=0.4, rely=0.5, anchor="center")

        load = tk.Button(self, text="Return to Main", command=lambda: controller.show_page(Title), 
                              bd=10, bg="orange", activebackground="orangered")
        load.place(relx=0.25, rely=0.6, anchor="center")

    

    def flip(self):

        if self.side:
            self.side =  False
        elif self.side == False:
            self.side = True
        
        self.update()
        # Flip flashcard self.errl.configure(text="please enter flashcard data before studying")
    
    def nextCard(self):
        self.deckIndx = random.randint(0, self.logic.DeckSize()) % (self.logic.DeckSize() - 1)
        #while the study value is too low
        while self.logic.getCard(self.deckIndx).getStudyVal() > 3:
            self.deckIndx += 1
            if self.deckIndx >= self.logic.DeckSize():
                self.deckIndx = 0
            #chance that it will give you the card again even if you already studied it
            rand = random.randint(1,4)
            if rand == 1:
                break


    def correct(self):
        card = self.logic.getCard(self.deckIndx)
        card.addStudyVal()
        
        self.nextCard()
        self.update()
    
    def wrong(self):
        card = self.logic.getCard(self.deckIndx)
        card.subtractStudyVal()

        self.nextCard()
        self.update()

    def update(self):
        self.text = self.logic.getInfo(self.deckIndx,self.side)
        self.card.configure(text=self.text)
        self.side = True

        

    

if __name__ == "__main__":
    app = App()
    app.mainloop()