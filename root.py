import tkinter as tk
from tkinter import ttk
from error import Error
from edit_box import Edit
import json

WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MACROS = ["Calories", "Protein", "Carbs", "Fat"]
UNITS = {"Calories" : "kj", "Protein" : "g", "Carbs" : "g", "Fat" : "g"}

class Main:
    def __init__(self, page, account_name):

        #setting the active day for display
        self.active_day = {"Monday" : ["active", "grey"], "Tuesday" : ["active", "grey"], "Wednesday" : ["active", "grey"], "Thursday" : ["active", "grey"], "Friday" : ["active", "grey"], "Saturday" : ["active", "grey"], "Sunday" : ["active", "grey"]}

        with open("acc_data.json", "r+") as f:
            self.data = json.load(f)
        #Initial designation of totals
        self.macro_goals = {"Calories" : 100.00, "Protein" : 100.00, "Carbs" : 100.00, "Fat" : 100.00}
        self.macro_totals = {"Calories" : 0, "Protein" : 0, "Carbs" : 0, "Fat" : 0}

        self.UI = page
        self.error_state = False
        self.window_status = False

        self.root = tk.Tk()
        self.root.geometry("800x480")
        self.root.iconbitmap("app.ico")
        self.root.resizable(0,0)

        self.c_goal = 100.00

        if self.UI == "Main":
            self.root.title("Sigma Fitness")
            self.acc_name = account_name
            self.win_bac = "#324450" # note to self, make dictionaries of all of the UI properties
            self.hdr_bg = "#469FD3"
            self.t_fg = "black"
        
        elif self.UI == "Sign In":
            self.root.title("Sigma Fitness - Sign In")
            self.acc_name = account_name
            self.win_bac = "#324450"
            self.hdr_bg = "#469FD3"
            self.t_fg = "black"


    def main_window(self, day, startup):
        self.window_status = True

        #exertion total string
        self.exertion_ts = tk.StringVar()
        #intake total string
        self.intake_ts = tk.StringVar()

        if startup == "Boot":
            self.day_btns = {}
            self.day_btn_set(startup, day)
        elif startup == "True":
            self.day_btn_set(startup, day)
        else:
            self.main_frame.destroy()
            self.btn_frame.destroy()
            self.header.destroy()
            self.acc_btn.destroy()
        
        MACROS
        for i in range(len(MACROS)):
            self.macro_goals[MACROS[i]] = (self.data[self.acc_name]["week_track"][day]["values"]["goals"][MACROS[i]])
            self.macro_totals[MACROS[i]] = (self.data[self.acc_name]["week_track"][day]["values"]["totals"][MACROS[i]])

        self.root.configure(bg=self.win_bac)

        self.root.columnconfigure((0,6), weight = 1)
        self.root.columnconfigure((1,2,4,5), weight = 2)
        self.root.columnconfigure(3, weight = 8)
        self.root.rowconfigure((0,2), weight = 1)
        self.root.rowconfigure((1,3,5,7), weight = 2)
        self.root.rowconfigure(4, weight = 6)
        self.root.rowconfigure(6, weight = 48)

        self.root.rowconfigure(1, minsize = 40)
        self.root.rowconfigure((0,2), minsize = 5)
        
        def btn_sign():
            self.sign()

        #Header frame
        self.header = tk.Frame(self.root, bg = self.hdr_bg)
        #self.header.grid_propagate(False)
        self.header.grid(column = 0, row = 0, columnspan = 7, rowspan = 3, sticky = "NESW")

        self.header.columnconfigure((0,1,3,4), weight = 1)
        self.header.columnconfigure(2, weight = 10)
        self.header.rowconfigure((0,1,2), weight = 1)
        
        self.app_img = tk.PhotoImage(file = 'app.png').subsample(20,20)
        self.acc_img = tk.PhotoImage(file = 'acc.png').subsample(13,13)
        self.app_ico = tk.Label(self.header, image = self.app_img, bg = self.hdr_bg)
        self.app_ico.grid(column = 0, row = 1, sticky = "NES")
        self.t_app = tk.Label(self.header, text = "Sigma Fitness", font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg)
        self.t_app.grid(column = 1, row = 1, sticky = "NSW")
        self.acc_btn = tk.Button(self.header, text = self.acc_name, font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg, activebackground = self.hdr_bg, image = self.acc_img, compound = "right", borderwidth = 0, relief = "sunken", command = btn_sign)
        self.acc_btn.grid(column = 3, row = 1, columnspan = 2, sticky = "NESW")
        #self.acc_btn.bind("<Button-1>", lambda event : btn_placeholder, add="+")
        #self.acc_btn.bind("<Button-1>", lambda _: "break", add="+")
        
        #Daily Buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.grid(column = 1, row = 4, columnspan = 5, sticky = "NESW")
        self.btn_frame.columnconfigure((0,2,4,6,8,10,12,14), weight = 1)
        self.btn_frame.columnconfigure((1,3,5,7,9,11,13), weight = 6)
        self.btn_frame.rowconfigure((0,1,2), weight = 1)

        self.btn_place()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(column = 1, row = 6, columnspan = 5, sticky = "NESW")
        self.main_frame.columnconfigure((0,2,4), weight = 1)
        self.main_frame.columnconfigure(1, weight = 34)
        self.main_frame.columnconfigure(3, weight = 20)
        self.main_frame.rowconfigure((0,2), weight = 1)
        self.main_frame.rowconfigure(1, weight = 24)

        self.daily_frame = tk.Frame(self.main_frame, borderwidth = 4, relief = "groove")
        #self.daily_frame.grid_propagate(False)
        self.daily_frame.grid(column = 1, row = 1, sticky = "NESW")

        self.daily_frame.columnconfigure((0,2,4), weight = 1)
        self.daily_frame.columnconfigure((1,3), weight = 24)
        self.daily_frame.rowconfigure((1), weight = 24)
        self.daily_frame.rowconfigure(0, weight = 1)
        self.daily_frame.rowconfigure(2, weight = 1)

        self.intake_t_frame = tk.Frame(self.daily_frame)
        self.intake_t_frame.grid(column = 1, row = 0, sticky = "NESW")
        self.intake_t_frame.columnconfigure(0, weight = 3)
        self.intake_t_frame.columnconfigure(1, weight = 1)
        self.intake_t_frame.rowconfigure(0, weight = 1)


        self.exertion_t_frame = tk.Frame(self.daily_frame)
        self.exertion_t_frame.grid(column = 3, row = 0, sticky = "NESW")
        self.exertion_t_frame.columnconfigure(0, weight = 3)
        self.exertion_t_frame.columnconfigure(1, weight = 1)
        self.exertion_t_frame.rowconfigure(0, weight = 1)


        self.t_intake = tk.Label(self.intake_t_frame, textvariable = self.intake_ts, font = 10, width = 5, anchor = "w")
        self.t_intake.grid(column = 0, row = 0, sticky = "NESW")
        self.t_intake = tk.Label(self.exertion_t_frame, textvariable = self.exertion_ts, font = 10, width = 5, anchor = "w")
        self.t_intake.grid(column = 0, row = 0, sticky = "NESW")
        self.intake_frame = tk.Frame(self.daily_frame, borderwidth = 2, bg = "red")
        self.intake_frame.grid_propagate(False)
        self.intake_frame.grid(column = 1, row = 1, sticky = "NESW")
        self.exertion_frame = tk.Frame(self.daily_frame, borderwidth = 2, bg = "red")
        self.exertion_frame.grid_propagate(False)
        self.exertion_frame.grid(column = 3, row = 1, sticky = "NESW")

        #Assigning the data from acc_data.json to a variable and setting the previous StringVars to these values (with some formatting)
        self.intake_t = (self.data[self.acc_name]["week_track"][day]["values"]["intake"]["Calories"])
        self.exertion_t = (self.data[self.acc_name]["week_track"][day]["values"]["exertion"]["Calories"])
        self.intake_ts.set(f"Intake: {self.intake_t}kj")
        self.exertion_ts.set(f"Exertion: {self.exertion_t}kj")

        self.totals_frame = tk.Frame(self.main_frame, borderwidth = 4, relief = "groove")
        self.totals_frame.grid_propagate(False)
        self.totals_frame.grid(column = 3, row = 1, sticky = "NESW")

        self.totals_frame.columnconfigure(0, weight = 1)
        self.totals_frame.rowconfigure(0, weight = 1)
        self.totals_frame.rowconfigure(1, weight = 19)

        self.pb_frame = tk.Frame(self.totals_frame)
        self.pb_frame.grid_propagate(False)
        self.pb_frame.grid(column = 0, row = 1, sticky = "NESW")

        self.pb_frame.columnconfigure(0, weight = 8)
        self.pb_frame.columnconfigure(1, weight = 2)
        self.pb_frame.rowconfigure((0,1,2,4,5,6,8,9,10,12,13,14), weight = 1)
        self.pb_frame.rowconfigure((3,7,11), weight = 2)

        #for loop for placing progress bars and data for intake
        under = ttk.Style()
        under.theme_use("default")
        under.configure("TProgressbar", thickness=3, background = self.hdr_bg)
        stat_attributes = {}
        for i in range(len(MACROS)):
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_pb"
            stat_attributes[MACROS[i]] = ttk.Progressbar(self.pb_frame, orient = tk.HORIZONTAL, style="TProgressbar", maximum = (self.macro_goals[MACROS[i]] + 0.1))
            stat_attributes[MACROS[i]].grid(column = 0, row = ((i*4) + 1), columnspan = 2, sticky = "NESW")

            if self.macro_totals[MACROS[i]] < self.macro_goals[MACROS[i]]:
                stat_attributes[MACROS[i]].step(self.macro_totals[MACROS[i]])
            else:
                stat_attributes[MACROS[i]].step(self.macro_goals[MACROS[i]])
                over = ttk.Style()
                over.theme_use("default")
                over.configure("TProgressbar", thickness=3, background = "red")
                stat_attributes[MACROS[i]].configure(style = "TProgressbar")
            
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_title"
            stat_attributes[MACROS[i]] = tk.Label(self.pb_frame, text = f"{MACROS[i]}:", font = ("Arial", 10)).grid(column = 0, row = ((i*4)), sticky = "SW")

            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_perc"
            current_percentage = round(((self.macro_totals[MACROS[i]]/self.macro_goals[MACROS[i]])*100))
            stat_attributes[MACROS[i]] = tk.Label(self.pb_frame, text = f"{current_percentage}%", font = ("Arial", 10)).grid(column = 1, row = ((i*4)), sticky = "ES")

            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_total"
            stat_attributes[MACROS[i]] = tk.Label(self.pb_frame, text = f"Total: {self.macro_totals[MACROS[i]]}{UNITS[MACROS[i]]}", font = ("Arial", 10)).grid(column = 0, row = ((i*4) + 2), sticky = "NW")

            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_btn"
            stat_attributes[MACROS[i]] = tk.Button(self.pb_frame, text = "edit", font = ("Arial", 10), height = 1, command = lambda : Edit("Calories").edit_popup()).grid(column = 1, row = ((i*4) + 2), sticky = "NE") 


        self.t_exertion = tk.Label(self.totals_frame, text = "Totals:", font = 10, width = 5, anchor = "w")
        self.t_exertion.grid(column = 0, row = 0, sticky = "NSW")
        self.exertion_frame = tk.Frame(self.totals_frame, borderwidth = 2)
        self.exertion_frame.grid_propagate(False)
        self.exertion_frame.grid(column = 3, row = 1, sticky = "NESW")

        #if self.error_state == True:
            #open error
        
        if startup == "Boot":
            self.sign()

        #open error window function
        self.root.mainloop()
        with open("acc_data.json", "w") as f:
            json.dump(self.data, f, indent = 4)

    def sign(self):
        self.window_status = True
        
        #self.root.configure(bg=self.win_bac)
        
        #could make function for clearing window in future, would have to add to main_window call
        self.main_frame.destroy()
        self.btn_frame.destroy()
        self.header.grid_forget()
        self.acc_btn.destroy()
        #self.totals_frame.destroy()
        #self.exertion_frame.destroy()
        #self.intake_frame.destroy()
        #self.daily_frame.destroy()


        self.root.columnconfigure((3,4,5,6), weight = 0)
        self.root.columnconfigure((0,2), weight = 23)
        self.root.columnconfigure(1, weight = 26)
        self.root.rowconfigure((6,7), weight = 0)
        self.root.rowconfigure((0,2), weight = 1)
        self.root.rowconfigure((1,3,5), weight = 2)
        self.root.rowconfigure(4, weight = 56)

        self.root.rowconfigure(1, minsize = 40)
        self.root.rowconfigure((0,2), minsize = 5)

        self.header.grid(column = 0, row = 0, columnspan = 3, rowspan = 3, sticky = "NESW")
        self.app_ico.grid(column = 0, row = 1, sticky = "NES")
        self.t_app.grid(column = 1, row = 1, sticky = "NSW")

        self.log = tk.Frame(self.root)
        self.log.grid_propagate(False)
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

        self.sign_in = tk.Button(self.options, text = "Sign In", bg = "white", height = 1, width = 1, command = self.sign_valid).grid(column = 2, row = 0, sticky = "NESW")
        self.sign_up = tk.Button(self.options, text = "Sign Up", bg = "white", height = 1, width = 1, command = self.sign_up_valid).grid(column = 0, row = 0, sticky = "NESW")
        self.root.bind("<Return>", lambda event : self.sign_valid())

        self.u_nam = tk.StringVar()
        self.u_pass = tk.StringVar()
        self.error_txt = tk.StringVar()
        self.t_user = tk.Label(self.log, text = "Username:", font = 10, height = 1).grid(column = 2, row = 3, sticky = "NSW")
        self.e_user = tk.Entry(self.log, textvariable = self.u_nam, bg = "white", font = 10, border = 1).grid(column = 2, row = 4, sticky = "NEW")
        self.t_pass = tk.Label(self.log, text = "Password:", font = 10, height = 1).grid(column = 2, row = 6, sticky = "NSW")
        self.e_pass = tk.Entry(self.log, textvariable = self.u_pass, bg = "white", font = 10, border = 1).grid(column = 2, row = 7, sticky = "NEW")
        self.t_error = tk.Label(self.log, textvariable = self.error_txt, width = 5, font = ("Arial", 7), fg = "red", height = 4).grid(column = 2, row = 8, sticky = "NEW")

        #self.root.mainloop()
    
    def sign_valid(self):
        try:
            if (self.data[self.u_nam.get()]["password"]) == self.u_pass.get():
                    self.acc_name = self.u_nam.get()
                    self.root.unbind("<Return>")
                    self.main_window("Monday", "True")
            else:
                self.error_txt.set("Key Error:\nplease try again,\nthe username or password you have entered is incorrect")
        except:
            self.error_txt.set("Key Error:\nplease try again,\nthe username or password you have entered is incorrect")

    def sign_up_valid(self):
        if self.u_nam.get() != "":
            if self.u_pass.get() != "":
                self.data[self.u_nam.get()] = dict(self.data["User_0"])
                self.data[self.u_nam.get()]["password"] = self.u_pass.get()
                with open("acc_data.json", "w") as f:
                    json.dump(self.data, f, indent = 4)
                with open("acc_data.json", "r+") as f:
                    self.data = json.load(f)
            else:
                self.error_txt.set("Key Error:\nplease try again,\nPlease enter a username and password\nin the respective entries")
        else:
            self.error_txt.set("Key Error:\nplease try again,\nPlease enter a username and password\nin the respective entries")

    def day_btn_set(self, startup, day = ""):
            for i in range(len(self.active_day)):
                self.active_day[WEEK_DAYS[i]] = ["normal", "green"]
            if day != "":
                self.day = day
            else:
                print("ruh roh")
            self.active_day[self.day] = ["disabled", "#d9d9d9"]
            if startup == "False":
                self.main_window(self.day, "False")

    def btn_place(self):
        for i in range(len(WEEK_DAYS)):
            #day_btns[WEEK_DAYS[i]] = f"{WEEK_DAYS[i]}_btn"
            #self.day_btns[WEEK_DAYS[i]].grid_forget()
            self.day_btns[WEEK_DAYS[i]] = tk.Button(self.btn_frame, text = WEEK_DAYS[i], bg = "green", relief = "solid", borderwidth = 1, activeforeground = self.hdr_bg, activebackground = "#d9d9d9", disabledforeground = self.hdr_bg, width = 1, command = lambda day = WEEK_DAYS[i]: self.day_btn_set("False", day))
            self.day_btns[WEEK_DAYS[i]].config(state = self.active_day[WEEK_DAYS[i]][0], bg = self.active_day[WEEK_DAYS[i]][1])
            self.day_btns[WEEK_DAYS[i]].grid(column = ((i * 2) + 1), row = 1, sticky = "NESW")

    def main_win_stat(self):
        return self.window_status
    
    def error_state_check(self, state):
        self.error_state = state