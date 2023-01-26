import tkinter as tk

class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculatrice")
        self.geometry("300x400")

        self.resultat = tk.StringVar()
        self.resultat.set("0")

        self.ecran = tk.Entry(self, textvariable=self.resultat, font=("Arial", 20))
        self.ecran.pack(padx=10, pady=10, fill=tk.X)

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.creer_boutons()

    def creer_boutons(self):
        chiffres = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "0", ".", "="
        ]

        operations = [
            "+", "-", "*", "/",
            "sqrt", "pow", "percent",
            "C", "<-"
        ]

        colonne = 0
        ligne = 0

        for chiffre in chiffres:
            bouton = tk.Button(self.frame, text=chiffre, width=5, height=2, command=lambda chiffre=chiffre: self.ajouter_chiffre(chiffre))
            bouton.grid(row=ligne, column=colonne)
            colonne += 1

            if colonne > 2:
                ligne += 1
                colonne = 0

        ligne = 0
        colonne = 3

        for operation in operations:
            bouton = tk.Button(self.frame, text=operation, width=5, height=2, command=lambda operation=operation: self.ajouter_operation(operation))
            bouton.grid(row=ligne, column=colonne)
            ligne += 1

    def ajouter_chiffre(self, chiffre):
        if chiffre == "=":
            try:
                resultat = eval(self.resultat.get())
                self.resultat.set(resultat)
            except:
                self.resultat.set("Error")
        elif chiffre == "C":
            self.resultat.set("0")
        elif chiffre == "<-":
            self.resultat.set(self.resultat.get()[:-1])
        else:
            if self.resultat.get() == "0":
                self.resultat.set(chiffre)
        else:
    def ajouter_operation(self, operation):
        if operation == "sqrt":
            self.resultat.set(self.resultat.get() + "**(1/2)")
        elif operation == "pow":
            self.resultat.set(self.resultat.get() + "**")
        elif operation == "percent":
            self.resultat.set(self.resultat.get() + "/100")
        else:
            if self.resultat.get()[-1] not in ["+", "-", "*", "/", "**"]:
                self.resultat.set(self.resultat.get() + operation)

calculatrice = Calculatrice()
calculatrice.mainloop()            self.resultat.set(self.resultat.get() + chiffre)
