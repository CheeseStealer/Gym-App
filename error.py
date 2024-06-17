import tkinter as tk
from tkinter import ttk

class Error:
    def __init__(self, error):
        self.error = error
        if self.error == "fatal":
            self.win_bac = "dark red"
            self.win_title = "Fatal Error"
            self.er_msg = "I don't even know what you did"
            self.btn_brdr = "black"
            self.img_txt_bg = "dark red"
            self.btn_txt = "white"
            self.btn_fg = "black"
        
        else:
            self.win_bac = "white"
            self.win_title = "Unexpected Error"
            self.er_msg = "Unexpected error"
            self.btn_brdr = "light grey"
            self.img_txt_bg = "white"
            self.btn_txt = "black"
            self.btn_fg = "white"

        self.window_status = False

    def er_popup(self):
        self.window_status = True

        popup = tk.Tk()
        popup.geometry("350x125")
        popup.title(self.win_title)
        popup.iconbitmap("er_icon.ico")
        popup.resizable(0,0)
        popup.configure(bg=self.win_bac)

        def click_quit():
            popup.destroy()

        popup.columnconfigure((1,2,3,4), weight = 4)
        popup.columnconfigure((0,5), weight = 1)
        popup.rowconfigure((0,1,2,3), weight = 4)
        popup.rowconfigure((4,6), weight = 2)
        popup.rowconfigure(5, weight = 1)

        error_name = tk.PhotoImage(file = 'error.png').subsample(12,12)
        er_img_lbl = tk.Label(popup, image = error_name, bg = self.img_txt_bg).grid(column = 1, row = 1, sticky = "NESW")
        boarder_lbl = tk.Label(popup, bg = self.btn_brdr).grid(column = 0, row = 4, columnspan = 6, rowspan = 3, sticky = "NESW")
        er_txt = tk.Label(popup, text = self.er_msg, font = 1, bg = self.img_txt_bg, fg = self.btn_txt).grid(column = 2, row = 1, columnspan = 2, sticky = "NSW")
        ex_btn = tk.Button(popup, text = "OK", font = 1, command = click_quit, bg = self.btn_fg, fg = self.btn_txt).grid(column = 4, row = 5, sticky = "NESW")
        self.window_status = False

        popup.mainloop()

    # I don't recall the purpose of this function but do not want to remove it incase it does have a use
#    def er_type(self):
#        return self.error

    def er_win_stat(self):
        return self.window_status