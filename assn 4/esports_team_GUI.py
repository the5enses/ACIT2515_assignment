import tkinter as tk
from tkinter import messagebox as tkMessageBox
import re
from add_player_popup import AddPlayerPopup
import requests


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="\nPlayer Roster\n").grid(row=1, column=2, columnspan=2)

        self._players_listbox = tk.Listbox(self, width=55, height=10)
        self._players_listbox.grid(row=2, column=1, columnspan=4)

        tk.Button(self, text="Add Player", command=self._add_player()).grid(row=3, column=1)

    def _add_player(self):
        """ Add Player Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddPlayerPopup(self._popup_win, self._close_player_callback())

    def _close_player_callback(self):
        self._popup_win.destroy()

    def _quit_callback(self):
        self.quit()


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

