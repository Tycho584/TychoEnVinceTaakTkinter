import tkinter as tk
import requests
from tkinter import ttk

root = tk.Tk()

baseURL = "https://api.frankfurter.app/2023-01-01..2023-11-22"

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
root.geometry("500x500")

tabBar = ttk.Notebook(root)
tabBar.grid(row=0,column=0)

tab1 = ttk.Frame(tabBar)
tab2 = ttk.Frame(tabBar)

tabBar.add(tab1, text="From - To")
tabBar.add(tab2, text="Specific date")


currencies = ["USD", "JPY", "BGN"]

fromValueInside = tk.StringVar(tab1)
toValueInside = tk.StringVar(tab1)

welcomeLabel = tk.Label(tab1, text="Welcome to the tkinter assignment of Tycho & Vince")
fromToWelcomeLabel = tk.Label(tab1, text="In this tab you can view the excange rate for diffrent currencies.")

fromCurrency = tk.OptionMenu(tab1,fromValueInside, *currencies)
toCurrency = tk.OptionMenu(tab1, toValueInside, *currencies)

fromCurrencyAmount = tk.Entry(tab1)
toCurrencyAmount = tk.Entry(tab1)

exchangeButton = tk.Button(tab1, text="Click here to exchange the currency", command=excangeCurrency)


welcomeLabel.grid(row=1, column=0, columnspan=6)
fromToWelcomeLabel.grid(row=2, column=0, columnspan=6)

fromCurrency.grid(row=3, column=0, columnspan=2)
toCurrency.grid(row=3, column=4, columnspan=2)

fromCurrencyAmount.grid(row=3, column=2)
toCurrencyAmount.grid(row=3, column=3)

exchangeButton.grid(row=4, column=2, columnspan=2)

test_label = tk.Label(tab2, text= "hoi")

test_label.grid(row= 0, column= 5)

root.mainloop()