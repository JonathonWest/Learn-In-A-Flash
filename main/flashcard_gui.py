import tkinter as tk
import tkinter.font as tkf
from Logic import Logic

FONT = ("Verdana", 20)

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

        label = tk.Label(self, text="Learn in a Flash!", fg="purple4", bg="steelblue", font=FONT, 
                              height=2, borderwidth="3", relief="groove")
        label.place(relx=0.5, rely=0.1, anchor="center")
        load = tk.Button(self, text="Load Flashcards", command=lambda: controller.show_page(Load), 
                              bd=10, bg="orange", activebackground="orangered")
        load.place(relx=0.25, rely=0.6, anchor="center")
        start = tk.Button(self, text="Study Flashcards", command=self.test, 
                              bd=10, bg="tomato")
        start.place(relx=0.75, rely=0.6, anchor="center")
        if self.err:
            errl = tk.Label(self, text="Enter Flashcard Data Before Studying", fg="purple4", bg="steelblue", font=FONT, 
                              height=1, borderwidth="2", relief="groove")
            errl.place(relx=0.75, rely=0.6, anchor="center")


    def test(self):
        if (self.logic.DeckSize()) == 0:
            self.err = True

class Load(tk.Frame):
    def __init__(self, parent, controller,logic):
        tk.Frame.__init__(self, parent)
        self.logic = logic

        label = tk.Label(self, text="Load File", fg="purple4", bg="steelblue", font=FONT, 
                              height=2, borderwidth="3", relief="groove")
        label.place(relx=0.5, rely=0.1, anchor="center")

if __name__ == "__main__":
    app = App()
    app.mainloop()