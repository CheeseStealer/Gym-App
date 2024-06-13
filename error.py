import tkinter as tk
#from tkinter import ttk

window_status = True

popup = tk.Tk()
popup.geometry("350x125")
popup.title("popup")
popup.resizable(0,0)

def click_quit():
    popup.destroy()

popup.columnconfigure((1,2,3,4), weight = 4)
popup.columnconfigure((0,5), weight = 1)
popup.rowconfigure((0,1,2,3), weight = 4)
popup.rowconfigure((4,6), weight = 2)
popup.rowconfigure(5, weight = 1)

error_name = tk.PhotoImage(file = 'error.png').subsample(12,12)
er_img_lbl = tk.Label(popup, image = error_name).grid(column = 1, row = 1, sticky = "NESW")
boarder_lbl = tk.Label(popup, bg = "light grey").grid(column = 0, row = 4, columnspan = 6, rowspan = 3, sticky = "NESW")
er_txt = tk.Label(popup, text = "Invalid input, please try again", font = 1).grid(column = 2, row = 1, columnspan = 2, sticky = "NSW")
ex_btn = tk.Button(popup, text = "OK", font = 1, command = click_quit).grid(column = 4, row = 5, sticky = "NESW")

popup.mainloop()
window_status = False

class Error:
    def __init__(self, error):
        self.error = error

    def win_stat(self):
        return window_status

error1 = Error("integer")