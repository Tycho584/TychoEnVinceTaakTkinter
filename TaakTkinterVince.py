from tkcalendar import Calendar, DateEntry
import tkinter as tk
import requests
from tkinter import ttk
import datetime

root = tk.Tk()

baseURL = "https://api.frankfurter.app/2023-01-01..2023-11-22"

""" Widgets voor ingeven voltooiingsdatum"""
# Custom DateEntry om datum op de (correcte) europese manier weer te geven.
class CustomDateEntry(DateEntry):
    def _select(self, event=None):
        date = self._calendar.selection_get()
        if date is not None:
            self._set_text(date.strftime('%d-%m-%Y'))
            self.event_generate('<<DateEntrySelected>>')
        self._top_cal.withdraw()
        if 'readonly' not in self.state():
            self.focus_set()


def specificDate():
    pass

def specificTimePeriod():
    pass

def excangeCurrency():
    baseURL = "https://api.frankfurter.app/"

    comingFromCurrency = fromCurrency
    goingToCurrency = toCurrency

    comingFromCurrencyAmount = fromCurrencyAmount.get()

    URL = f"{baseURL}latest?from={comingFromCurrency}&to={goingToCurrency}&amount={comingFromCurrencyAmount}"



def latestInformation():
    pass

def showAvailableCurrencies():
    pass

root.title("Currency Excanger")
# root.geometry("500x500")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

tabBar = ttk.Notebook(root)
tabBar.grid(row=0,column=0)

tab1 = ttk.Frame(tabBar)
subtab1 = ttk.Frame(tab1)
subtab1.pack()
tab2 = ttk.Frame(tabBar)
subtab2 = ttk.Frame(tab2)
subtab2.pack()

tabBar.add(tab1, text="From - To")
tabBar.add(tab2, text="Specific date")


currencies = ["USD", "JPY", "BGN"]

fromValueInside = tk.StringVar(subtab1)
toValueInside = tk.StringVar(subtab1)

welcomeLabel = tk.Label(subtab1, text="Welcome to the tkinter assignment of Tycho & Vince")
fromToWelcomeLabel = tk.Label(subtab1, text="In this tab you can view the excange rate for diffrent currencies.")

fromCurrency = tk.OptionMenu(subtab1,fromValueInside, *currencies)
toCurrency = tk.OptionMenu(subtab1, toValueInside, *currencies)
MidText = tk.Label(subtab1, text= "=")
fromCurrencyAmount = tk.Entry(subtab1)
toCurrencyAmount = tk.Entry(subtab1)

exchangeButton = tk.Button(subtab1, text="Click here to exchange the currency", command=excangeCurrency)


welcomeLabel.grid(row=1, column=0, columnspan=6)
fromToWelcomeLabel.grid(row=2, column=0, columnspan=6)

fromCurrency.grid(row=5, column=0, columnspan=2)
fromCurrencyAmount.grid(row=5, column=2)
MidText.grid(row=5, column=3)
toCurrencyAmount.grid(row=5, column=4)
toCurrency.grid(row=5, column=5, columnspan=2)

exchangeButton.grid(row=6, column=0, columnspan=6)

tabBar.add(tab1, text="From - To")
tabBar.add(tab2, text="Specific date")


currencies = ["USD", "JPY", "BGN"]

fromValueInside = tk.StringVar(subtab2)
toValueInside = tk.StringVar(subtab2)

welcomeLabel = tk.Label(subtab2, text="Welcome to the tkinter assignment of Tycho & Vince")
fromToWelcomeLabel = tk.Label(subtab2, text="In this tab you can view the excange rate for diffrent currencies at a specific date.")

tekiezen_einddatum_label = tk.Label(subtab2, text="Voltooiingsdatum")
einddatum_dateentry = CustomDateEntry(subtab2, width= 16, background= "black", foreground= "white",bd=2)
einddatum_dateentry.set_date(datetime.datetime.now().strftime("%d-%m-%Y"))

fromCurrency = tk.OptionMenu(subtab2,fromValueInside, *currencies)
MidText = tk.Label(subtab2, text= "=")
toCurrency = tk.OptionMenu(subtab2, toValueInside, *currencies)

fromCurrencyAmount = tk.Entry(subtab2)
toCurrencyAmount = tk.Entry(subtab2)

exchangeButton = tk.Button(subtab2, text="Click here to exchange the currency", command=excangeCurrency)

welcomeLabel.grid(row=1, column=0, columnspan=6)
fromToWelcomeLabel.grid(row=2, column=0, columnspan=6)

tekiezen_einddatum_label.grid(row=3, column=3, pady=(10, 0))
einddatum_dateentry.grid(row=4, column=3, pady=(0, 10))


fromCurrency.grid(row=5, column=0, columnspan=2)
fromCurrencyAmount.grid(row=5, column=2)
MidText.grid(row=5, column=3)
toCurrencyAmount.grid(row=5, column=4)
toCurrency.grid(row=5, column=5, columnspan=2)

exchangeButton.grid(row=6, column=0, columnspan=6)

# Toevoegen van DateEntry zelf

root.mainloop()