import tkinter as tk
from tkinter import ttk

class Error:
    def __init__(er_win, error):
        er_win.error = error
        if er_win.error == "fatal":
            er_win.win_bac = "dark red"
            er_win.win_title = "Fatal Error"
            er_win.er_msg = "I don't even know what you did"
            er_win.btn_brdr = "black"
            er_win.img_txt_bg = "dark red"
            er_win.btn_txt = "white"
            er_win.btn_fg = "black"
        
        else:
            er_win.win_bac = "white"
            er_win.win_title = "Unexpected Error"
            er_win.er_msg = "Unexpected error"
            er_win.btn_brdr = "light grey"
            er_win.img_txt_bg = "white"
            er_win.btn_txt = "black"
            er_win.btn_fg = "white"

        er_win.window_status = False

    def er_popup(er_win):
        er_win.window_status = True

        popup = tk.Toplevel()
        popup.grab_set()
        popup.geometry("350x125")
        popup.title(er_win.win_title)
        popup.iconbitmap("er_icon.ico")
        popup.resizable(0,0)
        popup.configure(bg=er_win.win_bac)

        def click_quit():
            popup.destroy()

        popup.columnconfigure((1,2,3,4), weight = 4)
        popup.columnconfigure((0,5), weight = 1)
        popup.rowconfigure((0,1,2,3), weight = 4)
        popup.rowconfigure((4,6), weight = 2)
        popup.rowconfigure(5, weight = 1)

        error_name = tk.PhotoImage(file = 'error.png').subsample(12,12)
        er_img_lbl = tk.Label(popup, image = error_name, bg = er_win.img_txt_bg).grid(column = 1, row = 1, sticky = "NESW")
        boarder_lbl = tk.Label(popup, bg = er_win.btn_brdr).grid(column = 0, row = 4, columnspan = 6, rowspan = 3, sticky = "NESW")
        er_txt = tk.Label(popup, text = er_win.er_msg, font = 1, bg = er_win.img_txt_bg, fg = er_win.btn_txt).grid(column = 2, row = 1, columnspan = 2, sticky = "NSW")
        ex_btn = tk.Button(popup, text = "OK", font = 1, command = click_quit, bg = er_win.btn_fg, fg = er_win.btn_txt).grid(column = 4, row = 5, sticky = "NESW")
        er_win.window_status = False

        popup.mainloop()

    # I don't recall the purpose of this function but do not want to remove it incase it does have a use
#    def er_type(er_win):
#        return er_win.error

    def er_win_stat(er_win):
        return er_win.window_status