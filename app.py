from tkinter import *
from tkinter import messagebox


class AmountError(Exception):
    pass


class CommaError(Exception):
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
        # PLN input label and entry field
        self.frame_pln = Frame()
        self.label_pln = Label(
            self.frame_pln, width=15, text="Podaj kwote w PLN:", anchor="w"
        )
        self.entry_pln = Entry(self.frame_pln)
        self.frame_pln.pack(side=TOP, fill=X, padx=5, pady=5)
        self.label_pln.pack(side=LEFT)
        self.entry_pln.pack(side=LEFT)

        self.entry_pln.focus()

        # Converting button
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

        # Creating labels and entries dynamically
        string = "Oto kwota w "
        currencies = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "SEK"]
        self.labels = []  # creates an empty list for labels
        self.entries = []  # creates an empty list for entries
        for x in currencies:  # iterates over currencies
            label_name = string + x + ":"
            row = Frame()
            label = Label(row, width=15, text=label_name, anchor="w")
            entry = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            label.pack(side=LEFT)
            entry.pack(side=LEFT)
            self.labels.append(label)  # appends the label to the list for further use
            self.entries.append(
                entry
            )  # appends the entries to the list for further use

    # Converting function
    def convert(self):
        try:
            input_value = self.entry_pln.get()

            if "," in input_value:
                raise CommaError

            input_value = float(input_value)

            if input_value <= 0:
                raise AmountError

        except ValueError:
            messagebox.showerror("ValueError", "Nieprawidlowy format danych")
        except AmountError:
            messagebox.showerror("AmountError", "Kwota nieprawidlowa")
        except CommaError:
            messagebox.showinfo(
                "CommaError",
                "Czesc dziesietna oddziel kropka(.) zamiast przecinkiem(,)",
            )
        else:
            currency_rates = [
                input_value / 4.06,  # USD
                input_value / 4.59,  # EUR
                input_value / 0.036,  # JPY
                input_value / 5.48,  # GBP
                input_value / 2.90,  # AUD
                input_value / 3.22,  # CAD
                input_value / 4.42,  # CHF
                input_value / 0.44,  # SEK
            ]

            for i in range(len(self.entries)):
                self.entries[i].delete(0, END)
                self.entries[i].insert(0, str(round(currency_rates[i], 2)))


converter = Converter()
