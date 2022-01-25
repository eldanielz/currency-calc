from tkinter import *
from tkinter import messagebox


class AmountError(Exception):
    pass


class Converter(object):
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.title("KONWERTER Waluty PLN ")
        self.build()
        self.window.mainloop()

    def build(self):
        self.field1 = Label()
        self.field1["text"] = "Podaj kwote w zl:"
        self.field1.grid(row=0, column=0, sticky="w")

        self.description1 = Entry(width=10)
        self.description1.focus()
        self.description1.grid(row=0, column=1, sticky="w")

        self.button1 = Button(
            width=14,
            text="PRZELICZ",
            command=self.convert,
        )
        self.button1.grid(row=1, column=0, sticky="w")

        self.field2 = Label()
        self.field2["text"] = "Oto Kwota w USD:"
        self.field2.grid(row=2, column=0, sticky="w")

        self.description2 = Entry(width=10)
        self.description2.grid(row=2, column=1, sticky="w")

        self.field3 = Label()
        self.field3["text"] = "Oto Kwota w EUR:"
        self.field3.grid(row=4, column=0, sticky="w")

        self.description3 = Entry(width=10)
        self.description3.grid(row=4, column=1, sticky="w")

        self.field4 = Label()
        self.field4["text"] = "Oto Kwota w JPY:"
        self.field4.grid(row=6, column=0, sticky="w")

        self.description4 = Entry(width=10)
        self.description4.grid(row=6, column=1, sticky="w")

        self.field5 = Label()
        self.field5["text"] = "Oto Kwota w GBP:"
        self.field5.grid(row=8, column=0, sticky="w")

        self.description5 = Entry(width=10)
        self.description5.grid(row=8, column=1, sticky="w")

        self.field6 = Label()
        self.field6["text"] = "Oto Kwota w AUD:"
        self.field6.grid(row=10, column=0, sticky="w")

        self.description6 = Entry(width=10)
        self.description6.grid(row=10, column=1, sticky="w")

        self.field7 = Label()
        self.field7["text"] = "Oto Kwota w CAD:"
        self.field7.grid(row=12, column=0, sticky="w")

        self.description7 = Entry(width=10)
        self.description7.grid(row=12, column=1, sticky="w")

        self.field8 = Label()
        self.field8["text"] = "Oto Kwota w CHF:"
        self.field8.grid(row=14, column=0, sticky="w")

        self.description8 = Entry(width=10)
        self.description8.grid(row=14, column=1, sticky="w")

        self.field9 = Label()
        self.field9["text"] = "Oto Kwota w SEK:"
        self.field9.grid(row=16, column=0, sticky="w")

        self.description9 = Entry(width=10)
        self.description9.grid(row=16, column=1, sticky="w")

    def convert(self):
        try:
            t = float(self.description1.get())
            if t <= 0:
                raise AmountError
        except ValueError:
            messagebox.showerror("ValueError", "Nieprawidłowy format danych")
        except AmountError:
            messagebox.showerror("AmountError", "Kwota nieprawidłowa")
        else:
            descriptions = [
                self.description2,
                self.description3,
                self.description4,
                self.description5,
                self.description6,
                self.description7,
                self.description8,
                self.description9,
            ]

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

            for i in range(len(descriptions)):
                descriptions[i].delete(0, END)
                descriptions[i].insert(0, str(round(currency_rates[i], 2)))


k = Converter()
