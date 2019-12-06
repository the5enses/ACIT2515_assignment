import tkinter as tk
from tkinter import messagebox
import requests
import re


class AddPlayerPopup(tk.Frame):
    """ Popup Frame to Add a player """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="First name:").grid(row=1, column=1)
        self._first_name = tk.Entry(self)
        self._first_name.grid(row=1, column=2)

        tk.Label(self, text="Last name:").grid(row=2, column=1)
        self._last_name = tk.Entry(self)
        self._last_name.grid(row=2, column=2)

        tk.Label(self, text="player name:").grid(row=3, column=1)
        self._player_name = tk.Entry(self)
        self._player_name.grid(row=3, column=2)

        tk.Label(self, text="age:").grid(row=4, column=1)
        self._age = tk.Entry(self)
        self._age.grid(row=4, column=2)

        tk.Label(self, text="num of towers:").grid(row=5, column=1)
        self._num_towers = tk.Entry(self)
        self._num_towers.grid(row=5, column=2)

        tk.Label(self, text="num of objectives:").grid(row=6, column=1)
        self._num_objectives = tk.Entry(self)
        self._num_objectives.grid(row=6, column=2)

        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=9, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=9, column=2)

    def _submit_cb(self):
        """ Submit the Add player """

        # Validate the non-string data values

        if re.match("^\d+$", self._age.get()) is None:
            messagebox.showerror("Error", "age must be a valid integer")
            return

        if re.match("^\d+$", self._num_towers.get()) is None:
            messagebox.showerror("Error", "nuber of towers must be a valid integer")
            return

        if re.match("^\d+$", self._num_objectives.get()) is None:
            messagebox.showerror("Error", "number of objectives must be a valid integer")
            return

        # Create the dictionary for the JSON request body
        data = {}
        data['first_name'] = self._first_name.get()
        data['last_name'] = self._last_name.get()
        data['player_name'] = self._player_name.get()
        data['age'] = int(self._age.get())
        data['num_towers'] = int(self._num_towers.get())
        data['num_objectives'] = int(self._num_objectives.get())
        data['type'] = "league player"

        # Implement your code here
        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/esports_team/players",
                                 json=data,
                                 headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Add player request failed\n\n" + response.text)

