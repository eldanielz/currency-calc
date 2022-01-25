from tkinter import *
from tkinter import messagebox


class AmountError(Exception):
    pass


class Converter(object):
    def __init__(self):
        self.window = Tk()
        self.window.geometry("250x350")
        self.window.eval("tk::PlaceWindow . center")
        self.window.title("KONWERTER Waluty PLN ")
        self.build()
        self.window.mainloop()

    def build(self):
        # PLN currency label and entry field
        self.frame_pln = Frame()
        self.label_pln = Label(
            self.frame_pln, width=15, text="Podaj kwote w PLN:", anchor="w"
        )
        self.entry_pln = Entry(self.frame_pln)
        self.frame_pln.pack(side=TOP, fill=X, padx=5, pady=5)
        self.label_pln.pack(side=LEFT)
        self.entry_pln.pack(side=LEFT)

        self.entry_pln.focus()

        self.frame_btn = Frame()
        self.button = Button(
            self.frame_btn,
            activebackground="grey",
            activeforeground="white",
            relief="groove",
            height=2,
            width=25,
            text="PRZELICZ",
            command=self.convert,
        )
        self.frame_btn.pack(side=TOP, fill=X, padx=30, pady=5)
        self.button.pack(side=LEFT)

        string = "Oto kwota w "
        currencies = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "SEK"]
        self.labels = []  # creates an empty list for labels
        self.entries = []  # creates an empty list for entries
        for x in currencies:  # iterates over currencies
            label_name = string + x + ":"
            row = Frame()
            label = Label(row, width=15, text=label_name, anchor="w")
            entry = Entry(row, justify="right")
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            label.pack(side=LEFT)
            entry.pack(side=LEFT)
            self.labels.append(label)  # appends the label to the list for further use
            self.entries.append(
                entry
            )  # appends the entries to the list for further use

    def convert(self):
        try:
            t = float(self.entry_pln.get())
            if t <= 0:
                raise AmountError
        except ValueError:
            messagebox.showerror("ValueError", "Nieprawidłowy format danych")
        except AmountError:
            messagebox.showerror("AmountError", "Kwota nieprawidłowa")
        else:
            currency_rates = [
                t / 4.06,
                t / 4.59,
                t / 0.036,
                t / 5.48,
                t / 2.90,
                t / 3.22,
                t / 4.42,
                t / 0.44,
            ]

            for i in range(len(self.entries)):
                self.entries[i].delete(0, END)
                self.entries[i].insert(0, str(round(currency_rates[i], 2)))


converter = Converter()
