import tkinter as tk
from tkinter import ttk

class Main:
    def __init__(self, page, account_name):
        self.UI = page
        self.ac_name = account_name
        self.win_bac = "white" # note to self, make dictionaries of all of the UI properties
        self.hdr_bg = "sky blue"
        self.t_fg = "white"
        self.error_state = False
        
        self.window_status = False

    def main_window(self):
        self.window_status = True

        root = tk.Tk()
        root.geometry("800x480")
        root.title("Sigma Fitness")
        root.iconbitmap("app.ico")
        root.resizable(1,1)
        root.configure(bg=self.win_bac)

        root.columnconfigure((0,6), weight = 1)
        root.columnconfigure((1,2,4,5), weight = 2)
        root.columnconfigure(3, weight = 8)
        root.rowconfigure((0,2,3,5), weight = 1)
        root.rowconfigure(1, weight = 2)
        root.rowconfigure(4, weight = 24)

        header = tk.Label(root, bg = "sky blue").grid(column = 0, row = 0, columnspan = 7, rowspan = 3, sticky = "NESW")
        
        app_img = tk.PhotoImage(file = 'app.png').subsample(15,15)
        acc_img = tk.PhotoImage(file = 'acc.png').subsample(10,10)
        app_ico = tk.Label(root, image = app_img, bg = self.hdr_bg).grid(column = 1, row = 1, sticky = "NESW")
        acc_ico = tk.Label(root, image = acc_img, bg = self.hdr_bg).grid(column = 5, row = 1, sticky = "NESW")
        t_app = tk.Label(root, text = "Sigma Fitness", font = ("bold", 20), fg = self.t_fg, bg = self.hdr_bg).grid(column = 2, row = 1, sticky = "NSW")
        t_acc = tk.Label(root, text = self.ac_name, font = ("bold", 20), fg = self.t_fg, bg = self.hdr_bg).grid(column = 4, row = 1, sticky = "NES")
        main_frame = tk.Frame(root).grid(column = 1, row = 4, columnspan = 5, sticky = "NESW")
        #if self.error_state == True:
            #open error
        
        #open error window function
        root.mainloop()
         
    def main_win_stat(self):
            return self.window_status
    
    def error_state_check(self, state):
        self.error_state = state