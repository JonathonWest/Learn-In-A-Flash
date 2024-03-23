import tkinter as tk
import tkinter.font as tkf
from Logic import Logic

LARGE_FONT = ("Verdana", 20)
SMOL_FONT = ("Verdana", 10)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.logic = Logic()

        # Create and configure container
        container = tk.Frame(self, width=1280, height=720, background="black")
        # container.pack(side = "top", fill = "both", expand = True) 
        container.grid(sticky='nswe')
        container.grid_propagate(0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Set up frames dictionary
        self.frames = {}
        self.PAGES = (Title, Load)
        for page in self.PAGES:
            frame = page(container, self,logic=self.logic)
            frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            self.frames[page] = frame
        

        

        self.show_page(Title)
  
    def show_page(self, frame):
        
        self.frames[frame].tkraise()

class Title(tk.Frame):
    def __init__(self, parent, controller,logic):
        tk.Frame.__init__(self, parent, background="white")
        self.logic = logic
        self.err = False

        label = tk.Label(self, text="Learn in a Flash!", fg="purple4", bg="steelblue", font=LARGE_FONT, 
                              height=2, borderwidth="3", relief="groove")
        label.place(relx=0.5, rely=0.1, anchor="center")
        load = tk.Button(self, text="Load Flashcards", command=lambda: controller.show_page(Load), 
                              bd=10, bg="orange", activebackground="orangered")
        load.place(relx=0.25, rely=0.6, anchor="center")
        self.errl = tk.Label(self, text="", fg="purple4", bg="steelblue", font=SMOL_FONT, 
                                height=1, borderwidth="2", relief="groove")
        self.errl.place(relx=0.75, rely=0.4, anchor="center")
        start = tk.Button(self, text="Study Flashcards", command=self.test, 
                              bd=10, bg="tomato")
        start.place(relx=0.75, rely=0.6, anchor="center")
        
        


    def test(self):
        if (self.logic.DeckSize()) == 0:
            self.errl.configure(text="please enter flashcard data before studying")

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

        load = tk.Button(self, text="Return to Main", command=lambda: controller.show_page(Title), 
                              bd=10, bg="orange", activebackground="orangered")
        load.place(relx=0.25, rely=0.6, anchor="center")

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

if __name__ == "__main__":
    app = App()
    app.mainloop()