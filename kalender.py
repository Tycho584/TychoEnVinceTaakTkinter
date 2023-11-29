from tkcalendar import Calendar, DateEntry
import tkinter as tk
import datetime

root = tk.Tk()

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

# Toevoegen van DateEntry zelf
tekiezen_einddatum_label = tk.Label(root, text="Voltooiingsdatum")
tekiezen_einddatum_label.grid(row=0, column=0)
einddatum_dateentry = CustomDateEntry(root, width= 16, background= "black", foreground= "white",bd=2)
einddatum_dateentry.set_date(datetime.datetime.now().strftime("%d-%m-%Y"))
einddatum_dateentry.grid(row=1, column=0)

root.mainloop()