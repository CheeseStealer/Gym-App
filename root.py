import tkinter as tk
from tkinter import ttk
from error import Error

WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class Main:
    def __init__(self, page, account_name):
        self.UI = page
        self.error_state = False
        self.window_status = False

        self.root = tk.Tk()
        self.root.geometry("800x480")
        self.root.iconbitmap("app.ico")
        self.root.resizable(0,0)

        if self.UI == "Main":
            self.root.title("Sigma Fitness")
            self.ac_name = account_name
            self.win_bac = "#324450" # note to self, make dictionaries of all of the UI properties
            self.hdr_bg = "#469FD3"
            self.t_fg = "black"
        
        elif self.UI == "Sign In":
            self.root.title("Sigma Fitness - Sign In")
            self.ac_name = account_name
            self.win_bac = "#324450"
            self.hdr_bg = "#469FD3"
            self.t_fg = "black"


    def main_window(self):
        self.window_status = True
        
        self.root.configure(bg=self.win_bac)

        self.root.columnconfigure((0,6), weight = 1)
        self.root.columnconfigure((1,2,4,5), weight = 2)
        self.root.columnconfigure(3, weight = 8)
        self.root.rowconfigure((0,2), weight = 1)
        self.root.rowconfigure((1,3,5,7), weight = 2)
        self.root.rowconfigure(4, weight = 6)
        self.root.rowconfigure(6, weight = 48)

        def btn_placeholder():
            #error1 = Error("integer")
            #error1.er_popup()
            self.sign()

        #Header frame
        self.header = tk.Frame(self.root, bg = self.hdr_bg)
        self.header.grid(column = 0, row = 0, columnspan = 7, rowspan = 3, sticky = "NESW")

        self.header.columnconfigure((0,1,3,4), weight = 1)
        self.header.columnconfigure(2, weight = 10)
        self.header.rowconfigure((0,1,2), weight = 1)
        
        self.app_img = tk.PhotoImage(file = 'app.png').subsample(20,20)
        self.acc_img = tk.PhotoImage(file = 'acc.png').subsample(13,13)
        self.app_ico = tk.Label(self.header, image = self.app_img, bg = self.hdr_bg).grid(column = 0, row = 1, sticky = "NES")
        self.t_app = tk.Label(self.header, text = "Sigma Fitness", font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg).grid(column = 1, row = 1, sticky = "NSW")
        self.acc_btn = tk.Button(self.header, text = self.ac_name, font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg, image = self.acc_img, compound = "right", borderwidth = 0, command = btn_placeholder)
        self.acc_btn.grid(column = 3, row = 1, columnspan = 2, sticky = "NESW")
        
        #Daily Buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.grid(column = 1, row = 4, columnspan = 5, sticky = "NESW")
        self.btn_frame.columnconfigure((0,2,4,6,8,10,12,14), weight = 1)
        self.btn_frame.columnconfigure((1,3,5,7,9,11,13), weight = 6)
        self.btn_frame.rowconfigure((0,1,2), weight = 1)

        day_btns = {}
        for i in range(len(WEEK_DAYS)):
            day_btns[WEEK_DAYS[i]] = f"{WEEK_DAYS[i]}_btn"
            day_btns[WEEK_DAYS[i]] = tk.Button(self.btn_frame, text = WEEK_DAYS[i], relief = "solid", borderwidth = 1, bg = "green", width = 1, command = btn_placeholder).grid(column = ((i * 2) + 1), row = 1, sticky = "NESW")
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(column = 1, row = 6, columnspan = 5, sticky = "NESW")
        self.main_frame.columnconfigure((0,2,4), weight = 1)
        self.main_frame.columnconfigure(1, weight = 34)
        self.main_frame.columnconfigure(3, weight = 20)
        self.main_frame.rowconfigure((0,2), weight = 1)
        self.main_frame.rowconfigure(1, weight = 24)
        daily_frame = tk.Frame(self.main_frame, bg = "red").grid(column = 1, row = 1, sticky = "NESW")
        total_frame = tk.Frame(self.main_frame, bg = "blue").grid(column = 3, row = 1, sticky = "NESW")
        #if self.error_state == True:
            #open error
        
        #open error window function
        self.root.mainloop()

    def sign (self):
        self.window_status = True
        
        #self.root.configure(bg=self.win_bac)
        
        #could make function for clearing window in future, would have to add to main_window call
        self.main_frame.destroy()
        self.btn_frame.destroy()
        self.acc_btn.destroy()

        self.root.columnconfigure((3,4,5,6), weight = 0)
        self.root.columnconfigure((0,2), weight = 8)
        self.root.columnconfigure(1, weight = 6)
        self.root.rowconfigure((6,7), weight = 0)
        self.root.rowconfigure((0,2), weight = 1)
        self.root.rowconfigure((1,3,5), weight = 2)
        self.root.rowconfigure(4, weight = 56)

        self.header.grid(column = 0, row = 0, columnspan = 3, rowspan = 3, sticky = "NESW")

        self.log = tk.Frame(self.root)
        self.log.grid(column = 1, row = 4, sticky = "NESW")

        self.log.columnconfigure((0,4), weight = 3)
        self.log.columnconfigure((1,3), weight = 2)
        self.log.columnconfigure(2, weight = 18)
        self.log.rowconfigure((0,2,3,5,6,9,10), weight = 1)
        self.log.rowconfigure((1,4,7), weight = 3)
        self.log.rowconfigure(8, weight = 8)

        self.acc_logo = tk.Frame(self.log)
        self.acc_logo.grid(column = 1, row = 1, columnspan = 3, sticky = "NESW")
        self.acc_logo.columnconfigure(1, weight = 1)
        self.acc_logo.columnconfigure((0,2), weight = 2)
        
        self.acc_ico = tk.Label(self.acc_logo, image = self.acc_img).grid(column = 0, row = 0, sticky = "NES")
        #make the sign in text variable for sign in screen and log out screen
        self.acc_title = tk.Label(self.acc_logo, text = "Sign in", font = ("bold", 15), width = 1).grid(column = 1, row = 0, sticky = "NESW")

        self.options = tk.Frame(self.log)
        self.options.grid(column = 1, row = 9, columnspan = 3, sticky = "NESW")
        self.options.columnconfigure((0,2), weight = 2)
        self.options.columnconfigure((1), weight = 1)
        self.options.rowconfigure(0, weight = 1)

        self.sign_in = tk.Button(self.options, text = "Sign In", bg = "white", height = 1, width = 1).grid(column = 2, row = 0, sticky = "NESW")
        self.sign_up = tk.Button(self.options, text = "Sign Up", bg = "white", height = 1, width = 1).grid(column = 0, row = 0, sticky = "NESW")

        self.t_user = tk.Label(self.log, text = "Username:", font = 10, height = 1).grid(column = 2, row = 3, sticky = "NSW")
        self.e_user = tk.Entry(self.log, bg = "white", font = 10, border = 1).grid(column = 2, row = 4, sticky = "NEW")
        self.t_pass = tk.Label(self.log, text = "Password:", font = 10, height = 1).grid(column = 2, row = 6, sticky = "NSW")
        self.e_pass = tk.Entry(self.log, bg = "white", font = 10, border = 1).grid(column = 2, row = 7, sticky = "NEW")
        self.t_error = tk.Label(self.log, text = "Error test display", fg = "red", height = 4).grid(column = 2, row = 8, sticky = "NEW")

        #self.root.mainloop()

    def main_win_stat(self):
        return self.window_status
    
    def error_state_check(self, state):
        self.error_state = state