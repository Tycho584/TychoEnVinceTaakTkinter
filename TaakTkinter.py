import tkinter as tk
from tkinter import ttk
import requests, datetime
from tkcalendar import Calendar, DateEntry

root = tk.Tk()

root.iconbitmap("Afbeeldingen\pay_cash_payment_money_dollar_bill_icon_143267.ico")

###############################################################################################################################################################################################

def specificDate():
    baseURL = "https://api.frankfurter.app/"

    date = einddatum_dateentry.get_date()

    fromCurrency = fromValueInsideSpecificDate.get()
    toCurrency = toValueInsideSpecificDate.get()

    URL = baseURL + f"{date}"

    getFileContentSpecificDate = requests.get(URL)
    getFileContentSpecificDateJson = getFileContentSpecificDate.json()

    print(getFileContentSpecificDateJson)
    
    fromCurrencyAmountSpecificDate.delete(0,tk.END)
    fromCurrencyAmountSpecificDate.insert(0,str(getFileContentSpecificDateJson['rates'][fromCurrency]))

    toCurrencyAmountSpecificDate.delete(0,tk.END)
    toCurrencyAmountSpecificDate.insert(0,str(getFileContentSpecificDateJson['rates'][toCurrency]))

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

    print(comingFromCurrencyAmount)

    if comingFromCurrencyAmount.isnumeric() == False or comingFromCurrencyAmount == "":
        noNumbersGivvenInAmountLabel.config(text="Give in a number in the entry!!", bg="yellow", fg="red")

    else:
        print(fromCurrencyAmount.get())
        comingFromCurrencyAmount = fromCurrencyAmount.get()

        URL = baseURL+f"latest?from={comingFromCurrency}&to={goingToCurrency}&amount={comingFromCurrencyAmount}"

        getFileContent = requests.get(URL)
        getFileContentJson = getFileContent.json()
        print(URL)
        print(getFileContentJson)

        toCurrencyAmount.delete(0,tk.END)
        toCurrencyAmount.insert(0,str(getFileContentJson["rates"][goingToCurrency]))

        noNumbersGivvenInAmountLabel.config(text="", bg="white")


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

class CustomDateEntry(DateEntry):
    def _select(self, event=None):
        date = self._calendar.selection_get()
        if date is not None:
            self._set_text(date.strftime('%d-%m-%Y'))
            self.event_generate('<<DateEntrySelected>>')
        self._top_cal.withdraw()
        if 'readonly' not in self.state():
            self.focus_set()

###################################################################################################################################################################################################

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
# tabBar.add(tab3, text="Specific time period")
# tabBar.add(tab4, text="Latest information")



currencies = ['AUD','BGN','BRL','CAD','CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']

###################################################################################################################################################################################################################

fromValueInside = tk.StringVar(tab1)
toValueInside = tk.StringVar(tab1)

welcomeLabel = tk.Label(tab1, text="Welcome to the tkinter assignment of Tycho & Vince")
fromToWelcomeLabel = tk.Label(tab1, text="In this tab you can view the excange rate for diffrent currencies.")

fromFullCurrencyNameLabel = tk.Label(tab1, text="",)
toFullCurrencyNameLabel = tk.Label(tab1, text="")

fromCurrency = tk.OptionMenu(tab1,fromValueInside, *currencies)
toCurrency = tk.OptionMenu(tab1, toValueInside, *currencies)

fromCurrencyAmount = tk.Entry(tab1)
EqualsSignLabel = tk.Label(tab1, text="=")
toCurrencyAmount = tk.Entry(tab1)

noNumbersGivvenInAmountLabel = tk.Label(tab1,text="")

exchangeButton = tk.Button(tab1, text="Click here to exchange the currency", command=excangeCurrency)


welcomeLabel.grid(row=0, column=0, columnspan=6)
fromToWelcomeLabel.grid(row=1, column=0, columnspan=6)

fromFullCurrencyNameLabel.grid(row=3, column=0, columnspan=2)
toFullCurrencyNameLabel.grid(row=3, column=2,columnspan=2)

fromCurrency.grid(row=2, column=0, columnspan=2)
toCurrency.grid(row=2, column=5, columnspan=2)

fromCurrencyAmount.grid(row=2, column=2)
EqualsSignLabel.grid(row=2,column=3)
toCurrencyAmount.grid(row=2, column=4)

exchangeButton.grid(row=4, column=2, columnspan=3)

noNumbersGivvenInAmountLabel.grid(row=5,column=0,columnspan=6)

###################################################################################################################################################################################################################

fromValueInsideSpecificDate = tk.StringVar(tab2)
toValueInsideSpecificDate = tk.StringVar(tab2)

welcomeLabelSpecificDate = tk.Label(tab2, text="Welcome to the tkinter assignment of Tycho & Vince")
fromToWelcomeLabelSpecificDate = tk.Label(tab2, text="In this tab you can view the excange rate for diffrent currencies at a specific date. (The base currency is EUR: You cannot change this)")

tekiezen_einddatum_label = tk.Label(tab2, text="Voltooiingsdatum")
einddatum_dateentry = CustomDateEntry(tab2, width= 16, background= "black", foreground= "white",bd=2)
einddatum_dateentry.set_date(datetime.datetime.now().strftime("%d-%m-%Y"))

fromCurrencySpecificDate = tk.OptionMenu(tab2,fromValueInsideSpecificDate, *currencies)
MidTextSpecificDate = tk.Label(tab2, text= "=")
toCurrencySpecificDate = tk.OptionMenu(tab2, toValueInsideSpecificDate, *currencies)

fromCurrencyAmountSpecificDate = tk.Entry(tab2)
toCurrencyAmountSpecificDate = tk.Entry(tab2)

exchangeButtonSpecificDate = tk.Button(tab2, text="Click here to exchange the currency", command=specificDate)

welcomeLabelSpecificDate.grid(row=1, column=0, columnspan=6)
fromToWelcomeLabelSpecificDate.grid(row=2, column=0, columnspan=6)

tekiezen_einddatum_label.grid(row=3, column=3, pady=(10, 0))
einddatum_dateentry.grid(row=4, column=3, pady=(0, 10))


fromCurrencySpecificDate.grid(row=5, column=0, columnspan=2)
fromCurrencyAmountSpecificDate.grid(row=5, column=2)
MidTextSpecificDate.grid(row=5, column=3)
toCurrencyAmountSpecificDate.grid(row=5, column=4)
toCurrencySpecificDate.grid(row=5, column=5, columnspan=2)

exchangeButtonSpecificDate.grid(row=6, column=0, columnspan=6)

root.mainloop()