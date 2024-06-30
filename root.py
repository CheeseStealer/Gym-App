import tkinter as tk
from tkinter import ttk

WEEK_DAYS = ["Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class Main:
    def __init__(self, page, account_name):
        self.UI = page
        self.ac_name = account_name
        self.win_bac = "#324450" # note to self, make dictionaries of all of the UI properties
        self.hdr_bg = "#469FD3"
        self.t_fg = "black"
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
        root.rowconfigure((0,2), weight = 0)
        root.rowconfigure((3,5,7), weight = 1)
        root.rowconfigure((1,7), weight = 1)
        root.rowconfigure(4, weight = 3)
        root.rowconfigure(6, weight = 24)

        #Header frame
        header = tk.Frame(root, bg = self.hdr_bg)
        header.grid(column = 0, row = 0, columnspan = 7, rowspan = 3, sticky = "NESW")

        header.columnconfigure((0,1,3,4), weight = 1)
        header.columnconfigure(2, weight = 10)
        header.rowconfigure((0,1,2), weight = 1)
        
        app_img = tk.PhotoImage(file = 'app.png').subsample(20,20)
        acc_img = tk.PhotoImage(file = 'acc.png').subsample(13,13)
        app_ico = tk.Label(header, image = app_img, bg = self.hdr_bg).grid(column = 0, row = 1, sticky = "NES")
        t_app = tk.Label(header, text = "Sigma Fitness", font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg).grid(column = 1, row = 1, sticky = "NSW")
        acc_btn = tk.Button(header, text = self.ac_name, font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg, image = acc_img, compound = "right", borderwidth = 0).grid(column = 3, row = 1, columnspan = 2, sticky = "NESW")
        
        #Daily Buttons
        btn_frame = tk.Frame(root)
        btn_frame.grid(column = 1, row = 4, columnspan = 5, sticky = "NESW")
        btn_frame.columnconfigure((0,2,4,6,8,10,12,14), weight = 1)
        btn_frame.columnconfigure((1,3,5,7,9,11,13), weight = 6)
        btn_frame.rowconfigure((0,1,2), weight = 1)

        day_btns = {}
        for i in range(len(WEEK_DAYS)):
            day_btns[WEEK_DAYS[i]] = f"{WEEK_DAYS[i]}_btn"
            day_btns[WEEK_DAYS[i]] = tk.Button(btn_frame, text = WEEK_DAYS[i], relief = "solid", borderwidth = 1, bg = "green").grid(column = ((i * 2) + 1), row = 1, sticky = "NESW")
        
        main_frame = tk.Frame(root)
        main_frame.grid(column = 1, row = 6, columnspan = 5, sticky = "NESW")
        main_frame.columnconfigure((0,2,4), weight = 1)
        main_frame.columnconfigure(1, weight = 34)
        main_frame.columnconfigure(3, weight = 20)
        main_frame.rowconfigure((0,2), weight = 1)
        main_frame.rowconfigure(1, weight = 24)
        daily_frame = tk.Frame(main_frame, bg = "red").grid(column = 1, row = 1, sticky = "NESW")
        total_frame = tk.Frame(main_frame, bg = "blue").grid(column = 3, row = 1, sticky = "NESW")
        #if self.error_state == True:
            #open error
        
        #open error window function
        root.mainloop()
         
    def main_win_stat(self):
            return self.window_status
    
    def error_state_check(self, state):
        self.error_state = state