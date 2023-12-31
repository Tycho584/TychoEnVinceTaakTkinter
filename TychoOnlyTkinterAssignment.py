import tkinter as tk
from tkinter import ttk
import requests

root = tk.Tk()

baseURL = "https://api.frankfurter.app/2023-01-01..2023-11-22"

def specificDate():
    baseURL = "https://api.frankfurter.app/"

    date = "Enter your start date here"

    URL = baseURL + f"{date}"

    getFileContentSpecificDate = requests.get(URL)
    getFileContentSpecificDateJson = getFileContentSpecificDate.json()

def specificTimePeriod():
    baseURL = "https://api.frankfurter.app/"

    startDate = "Enter your start date here"
    endDate = "Enter your end date here"

    URL = baseURL + f"{startDate}..{endDate}"

    getFileContentSpecificTimePeriod = requests.get(URL)
    getFileContentSpecificTimePeriodJson = getFileContentSpecificTimePeriod.json()

def excangeCurrency():
    baseURL = "https://api.frankfurter.app/"

    comingFromCurrency = fromValueInside.get()
    goingToCurrency = toValueInside.get()

    comingFromCurrencyAmount = fromCurrencyAmount.get()

    URL = baseURL+f"latest?from={comingFromCurrency}&to={goingToCurrency}&amount={comingFromCurrencyAmount}"

    getFileContent = requests.get(URL)
    getFileContentJson = getFileContent.json()
    print(URL)
    print(getFileContentJson)

    toCurrencyAmount.insert(0,str(getFileContentJson["rates"][goingToCurrency]))

def latestInformation():
    URL = "https://api.frankfurter.app/latest"

    getFileContentLatestInformation = requests.get(URL)
    getFileContentLatestInformationJson = getFileContentLatestInformation.json()

    print(getFileContentLatestInformationJson)

def showAvailableCurrencies():
    URL = "https://api.frankfurter.app/currencies"

    getFileContentAvailableCurrencies = requests.get(URL)
    getFileContentAvailableCurrenciesJson = getFileContentAvailableCurrencies.json()

    print(getFileContentAvailableCurrenciesJson)

root.title("Currency Excanger")
root.geometry("1000x650")

tabBar = ttk.Notebook(root)
tabBar.grid(row=0,column=0)

tab1 = ttk.Frame(tabBar)
tab2 = ttk.Frame(tabBar)
tab3 = ttk.Frame(tabBar)
tab4 = ttk.Frame(tabBar)

tabBar.add(tab1, text="From - To")
tabBar.add(tab2, text="Specific date")
tabBar.add(tab3, text="Specific time period")
tabBar.add(tab4, text="Latest information")



currencies = ['AUD','BGN','BRL','CAD','CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

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

root.mainloop()