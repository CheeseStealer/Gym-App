import tkinter as tk
from tkinter import ttk
import json

MACROS = ["Calories", "Protein", "Carbs", "Fat"]

class Edit:
    def __init__(win, edit_type):
        win.edit = edit_type
        if win.edit in MACROS:
            win.win_bac = "#d9d9d9"
            win.win_title = f"{win.edit} Goal Editor"
            f"Current {win.edit} Goal:"
            win.btn_brdr = "black"
            win.img_txt_bg = "dark red"
            win.btn_txt = "white"
            win.btn_fg = "black"
            win.edit_assets = 1
        
        else:
            win.win_bac = "white"
            win.win_title = "Unexpected Error"
            win.er_msg = "Unexpected error"
            win.btn_brdr = "light grey"
            win.img_txt_bg = "white"
            win.btn_txt = "black"
            win.btn_fg = "white"

        win.window_status = False

    def edit_popup(win):
        win.window_status = True

        popup = tk.Toplevel()
        popup.grab_set()
        popup.geometry("350x125")
        popup.title(win.win_title)
        popup.iconbitmap("er_icon.ico")
        popup.resizable(0,0)
        popup.configure(bg=win.win_bac)

        def click_quit():
            popup.destroy()

        popup.columnconfigure((1,2,3,4), weight = 4)
        popup.columnconfigure((0,5), weight = 1)
        popup.rowconfigure((0,1,2,3), weight = 4)
        popup.rowconfigure((4,6), weight = 2)
        popup.rowconfigure(5, weight = 1)

        error_name = tk.PhotoImage(file = 'error.png').subsample(12,12)
        er_img_lbl = tk.Label(popup, image = error_name, bg = win.img_txt_bg).grid(column = 1, row = 1, sticky = "NESW")
        boarder_lbl = tk.Label(popup, bg = win.btn_brdr).grid(column = 0, row = 4, columnspan = 6, rowspan = 3, sticky = "NESW")
        er_txt = tk.Label(popup, text = win.er_msg, font = 1, bg = win.img_txt_bg, fg = win.btn_txt).grid(column = 2, row = 1, columnspan = 2, sticky = "NSW")
        ex_btn = tk.Button(popup, text = "Confirm", font = 1, command = click_quit, bg = win.btn_fg, fg = win.btn_txt).grid(column = 4, row = 5, sticky = "NESW")
        win.window_status = False

        popup.mainloop()