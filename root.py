import tkinter as tk
from tkinter import ttk
from error import Error
from edit_box import Edit
import json

#declaration of all constants
WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MACROS = ["Calories", "Protein", "Carbs", "Fat"]
UNITS = {"Calories" : "kj", "Protein" : "g", "Carbs" : "g", "Fat" : "g"}

class Main:
    def __init__(self, page, account_name):
        #Declaring page as a variable across the whole class
        self.UI = page
        
        #Setting the active day for display
        self.active_day = {"Monday" : ["active", "grey"], "Tuesday" : ["active", "grey"], "Wednesday" : ["active", "grey"], "Thursday" : ["active", "grey"], "Friday" : ["active", "grey"], "Saturday" : ["active", "grey"], "Sunday" : ["active", "grey"]}

        #Opening json file
        with open("acc_data.json", "r+") as f:
            self.data = json.load(f)

        #Initial designation of totals
        self.macro_goals = {"Calories" : 100.00, "Protein" : 100.00, "Carbs" : 100.00, "Fat" : 100.00}
        self.macro_totals = {"Calories" : 0, "Protein" : 0, "Carbs" : 0, "Fat" : 0}

        #Setting basic window properties
        self.root = tk.Tk()
        self.root.geometry("800x480")
        self.root.iconbitmap("app.ico")
        self.root.resizable(0,0)

        #Dictating which properties the window will have dependant on the active page
        #(currently not overly utilized but could be in future with the addition of more pages)
        if self.UI == "Main":
            self.root.title("Sigma Fitness")
            self.acc_name = account_name
            self.win_bac = "#324450"
            self.hdr_bg = "#469FD3"
            self.t_fg = "black"
        elif self.UI == "Sign In":
            self.root.title("Sigma Fitness - Sign In")
            self.acc_name = account_name
            self.win_bac = "#324450"
            self.hdr_bg = "#469FD3"
            self.t_fg = "black"

    def main_window(self, day, startup):
        #Unbinding enter so there is not a paradoxical call of main window
        self.root.unbind("<Enter>")

        with open("acc_data.json", "r+") as f:
            self.data = json.load(f)

        self.menu = list(self.data[self.acc_name]["week_track"][day]["menu"])
        self.exercise = list(self.data[self.acc_name]["week_track"][day]["exertion"])

        #exertion total string
        self.exertion_ts = tk.StringVar()
        #intake total string
        self.intake_ts = tk.StringVar()

        #Dictating the behaviour of the page dependant on what has triggered this method
        #"Boot" referring to the initial startup of the application  
        if startup == "Boot":
            self.current_menu_item = 0
            self.current_e_menu_item = 0
            self.day_btns = {}
            self.day_btn_set(startup, day)
        #"True" while not "Boot" refers to the page being opened freshly but not for the first instance of the application
        elif startup == "True":
            self.current_menu_item = 0
            self.current_e_menu_item = 0
            self.day_btn_set(startup, day)
        #This is to delete the assets of the sign in page to proceed to the main screen
        else:
            self.main_frame.destroy()
            self.btn_frame.destroy()
            self.header.destroy()
            self.acc_btn.destroy()

        #Pulling all goal and totals data from the json file
        for i in range(len(MACROS)):
            self.macro_goals[MACROS[i]] = (self.data[self.acc_name]["week_track"][day]["values"]["goals"][MACROS[i]])
            active_macro_total = 0
            for item in self.data[self.acc_name]["week_track"][day]["menu"]:
                active_macro_total = (active_macro_total + int(self.data[self.acc_name]["week_track"][day]["menu"][item][MACROS[i]]))
            if MACROS[i] == "Calories":
                for item in self.data[self.acc_name]["week_track"][day]["exertion"]:
                    active_macro_total = (active_macro_total - int(self.data[self.acc_name]["week_track"][day]["exertion"][item]))
            self.data[self.acc_name]["week_track"][day]["values"]["totals"][MACROS[i]] = active_macro_total
            self.macro_totals[MACROS[i]] = (self.data[self.acc_name]["week_track"][day]["values"]["totals"][MACROS[i]])

        #Setting the window to the main pages window background
        #This is not overly useful in the programs current version but would be useful if later verions include other pages with different window colours
        self.root.configure(bg=self.win_bac)

        #Configuring the window's grid for the main page
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
        self.header.grid(column = 0, row = 0, columnspan = 7, rowspan = 3, sticky = "NESW")

        #Header frame grid configuration
        self.header.columnconfigure((0,1,3,4), weight = 1)
        self.header.columnconfigure(2, weight = 10)
        self.header.rowconfigure((0,1,2), weight = 1)
        
        #Importing the application logo png and account icon png to the program
        self.app_img = tk.PhotoImage(file = 'app.png').subsample(20,20)
        self.acc_img = tk.PhotoImage(file = 'acc.png').subsample(13,13)

        #Defining and placing the header widgets
        self.app_ico = tk.Label(self.header, image = self.app_img, bg = self.hdr_bg)
        self.t_app = tk.Label(self.header, text = "Sigma Fitness", font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg)
        self.acc_btn = tk.Button(self.header, text = self.acc_name, font = ("bold", 15), fg = self.t_fg, bg = self.hdr_bg, activebackground = self.hdr_bg, image = self.acc_img, compound = "right", borderwidth = 0, relief = "sunken", command = btn_sign)
        self.app_ico.grid(column = 0, row = 1, sticky = "NES")
        self.t_app.grid(column = 1, row = 1, sticky = "NSW")
        self.acc_btn.grid(column = 3, row = 1, columnspan = 2, sticky = "NESW")
        
        #A frame for placing the daily buttons
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.grid(column = 1, row = 4, columnspan = 5, sticky = "NESW")

        #Configuring the frame's grids
        self.btn_frame.columnconfigure((0,2,4,6,8,10,12,14), weight = 1)
        self.btn_frame.columnconfigure((1,3,5,7,9,11,13), weight = 6)
        self.btn_frame.rowconfigure((0,1,2), weight = 1)

        #Calling the function for placing all week day buttons
        self.btn_place()

        #Declaring the main elements frame; containing the intake, exertion, and totals
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(column = 1, row = 6, columnspan = 5, sticky = "NESW")
        
        #Configuring the frame's grids
        self.main_frame.columnconfigure((0,2,4), weight = 1)
        self.main_frame.columnconfigure(1, weight = 34)
        self.main_frame.columnconfigure(3, weight = 20)
        self.main_frame.rowconfigure((0,2), weight = 1)
        self.main_frame.rowconfigure(1, weight = 24)

        #Declaring the "daily frame" which contains (and frames) the intake and exertion
        self.daily_frame = tk.Frame(self.main_frame, borderwidth = 4, relief = "groove")
        self.daily_frame.grid(column = 1, row = 1, sticky = "NESW")

        #Configuring the frame's grids
        self.daily_frame.columnconfigure((0,2,4), weight = 1)
        self.daily_frame.columnconfigure((1,3), weight = 24)
        self.daily_frame.rowconfigure((1), weight = 24)
        self.daily_frame.rowconfigure(0, weight = 1)
        self.daily_frame.rowconfigure(2, weight = 1)

        #Declaring the intake frame to display food items and their corresponding data (and options for editing)
        self.intake_t_frame = tk.Frame(self.daily_frame)
        self.intake_t_frame.grid(column = 1, row = 0, sticky = "NESW")
        
        #Configuring the frame's grids
        self.intake_t_frame.columnconfigure(0, weight = 3)
        self.intake_t_frame.columnconfigure(1, weight = 1)
        self.intake_t_frame.rowconfigure(0, weight = 1)

        #Declaring the intake frame to display exercise and the corresponding caloric expendature data (and options for editing)
        self.exertion_t_frame = tk.Frame(self.daily_frame)
        self.exertion_t_frame.grid(column = 3, row = 0, sticky = "NESW")
        
        #Configuring the frame's grids
        self.exertion_t_frame.columnconfigure(0, weight = 3)
        self.exertion_t_frame.columnconfigure(1, weight = 1)
        self.exertion_t_frame.rowconfigure(0, weight = 1)

        #Declaring and placing all widgets withing the frames nested in the main frame
        self.t_intake = tk.Label(self.intake_t_frame, textvariable = self.intake_ts, font = 10, width = 5, anchor = "w")
        self.exertion = tk.Label(self.exertion_t_frame, textvariable = self.exertion_ts, font = 10, width = 5, anchor = "w")
        self.intake_frame = tk.Frame(self.daily_frame, borderwidth = 2, relief = "solid")
        self.exertion_frame = tk.Frame(self.daily_frame, borderwidth = 2, relief = "solid")
        self.t_intake.grid(column = 0, row = 0, sticky = "NESW")
        self.exertion.grid(column = 0, row = 0, sticky = "NESW")
        self.intake_frame.grid(column = 1, row = 1, sticky = "NESW")
        self.exertion_frame.grid(column = 3, row = 1, sticky = "NESW")
        self.intake_frame.grid_propagate(False)
        self.exertion_frame.grid_propagate(False)

        #Configuring the grid properties of the intake frame
        self.intake_frame.columnconfigure((0,4), weight = 1)
        self.intake_frame.columnconfigure(2, weight = 5)
        self.intake_frame.columnconfigure((1,3), weight = 4)
        self.intake_frame.rowconfigure(0, weight = 2)
        self.intake_frame.rowconfigure((1,3,5,7,9), weight = 1)
        self.intake_frame.rowconfigure(2, weight = 8)
        self.intake_frame.rowconfigure((4,6), weight = 6)
        self.intake_frame.rowconfigure(8, weight = 3)

        self.item_select = tk.StringVar()
        self.item_select.set(str(int(self.current_menu_item) + 1))
        item_selection = tk.Spinbox(self.intake_frame, textvariable = self.item_select, exportselection = True, increment = 1, state = "readonly", wrap = True, justify = "center", bg = "white", command = self.update_item)
        item_selection.grid(column = 0, row = 0, columnspan = 5, sticky = "NESW")
        try:
            item_selection.configure(from_ = 1, to = len(self.menu), state = "readonly")
        except:
            item_selection.configure(state = "disabled")

        food_item = tk.StringVar()
        current_cal = tk.StringVar()
        current_pro = tk.StringVar()
        current_carb = tk.StringVar()
        current_fat = tk.StringVar()
        try:
            food_item.set(self.menu[self.current_menu_item])
            i_current_cal = self.data[self.acc_name]["week_track"][day]["menu"][self.menu[self.current_menu_item]]["Calories"]
            i_current_pro = self.data[self.acc_name]["week_track"][day]["menu"][self.menu[self.current_menu_item]]["Protein"]
            i_current_carb = self.data[self.acc_name]["week_track"][day]["menu"][self.menu[self.current_menu_item]]["Carbs"]
            i_current_fat = self.data[self.acc_name]["week_track"][day]["menu"][self.menu[self.current_menu_item]]["Fat"]
            current_cal.set(f"Calories: {i_current_cal}kj")
            current_pro.set(f"Protein: {i_current_pro}g")
            current_carb.set(f"Carbs: {i_current_carb}g")
            current_fat.set(f"Fat: {i_current_fat}g")
        except:
            food_item.set("No Food Items Given")
        t_food_item = tk.Label(self.intake_frame, textvariable = food_item, font = ("Arial", 12, "bold")).grid(column = 1, row = 2, columnspan = 3, sticky = "NESW")
        t_cal = tk.Label(self.intake_frame, textvariable = current_cal, font = ("Arial", 10), width = 10, anchor = "w").grid(column = 1, row = 4, sticky = "NESW")
        t_pro = tk.Label(self.intake_frame, textvariable = current_pro, font = ("Arial", 10), width = 10, anchor = "w").grid(column = 3, row = 4, sticky = "NESW")
        t_carb = tk.Label(self.intake_frame, textvariable = current_carb, font = ("Arial", 10), width = 10, anchor = "w").grid(column = 1, row = 6, sticky = "NESW")
        t_fat = tk.Label(self.intake_frame, textvariable = current_fat, font = ("Arial", 10), width = 10, anchor = "w").grid(column = 3, row = 6, sticky = "NESW")

        #Buttons to add/remove meal
        intake_add_btn = tk.Button(self.intake_frame, text = "Add", bg = "white", relief = "solid", borderwidth = 1, activeforeground = self.hdr_bg, activebackground = "#d9d9d9", width = 10, command = lambda type = "Add Meal" : self.edit_box(type)).grid(column = 3, row = 8, sticky = "NESW")
        intake_add_btn = tk.Button(self.intake_frame, text = "Delete", bg = "white", relief = "solid", borderwidth = 1, activeforeground = self.hdr_bg, activebackground = "#d9d9d9", width = 10, command = lambda type = "menu" : self.remove_item(type)).grid(column = 1, row = 8, sticky = "NESW")

        #Configuring the grid properties of the exertion frame
        self.exertion_frame.columnconfigure((0,4), weight = 1)
        self.exertion_frame.columnconfigure(2, weight = 5)
        self.exertion_frame.columnconfigure((1,3), weight = 4)
        self.exertion_frame.rowconfigure(0, weight = 2)
        self.exertion_frame.rowconfigure((1,3,5,7,9), weight = 1)
        self.exertion_frame.rowconfigure(2, weight = 8)
        self.exertion_frame.rowconfigure((4,6), weight = 6)
        self.exertion_frame.rowconfigure(8, weight = 3)

        self.item_e_select = tk.StringVar()
        self.item_e_select.set(str(int(self.current_e_menu_item) + 1))
        item_e_selection = tk.Spinbox(self.exertion_frame, textvariable = self.item_e_select, exportselection = True, increment = 1, state = "readonly", wrap = True, justify = "center", bg = "white", command = self.update_exercise)
        item_e_selection.grid(column = 0, row = 0, columnspan = 5, sticky = "NESW")
        try:
            item_e_selection.configure(from_ = 1, to = len(self.exercise), state = "readonly")
        except:
            item_e_selection.configure(state = "disabled")

        exercise_item = tk.StringVar()
        current_e_cal = tk.StringVar()
        try:
            exercise_item.set(self.exercise[self.current_e_menu_item])
            i_current_e_cal = self.data[self.acc_name]["week_track"][day]["exertion"][self.exercise[self.current_e_menu_item]]
            current_e_cal.set(f"Calories: {i_current_e_cal}kj")
        except:
            exercise_item.set("No Exercises Given")
        t_exercise = tk.Label(self.exertion_frame, textvariable = exercise_item, font = ("Arial", 12, "bold")).grid(column = 1, row = 2, columnspan = 3, sticky = "NESW")
        t_e_cal = tk.Label(self.exertion_frame, textvariable = current_e_cal, font = ("Arial", 10), width = 10, anchor = "w").grid(column = 1, row = 4, sticky = "NESW")

        #Buttons to add/remove exercise
        exertion_add_btn = tk.Button(self.exertion_frame, text = "Add", bg = "white", relief = "solid", borderwidth = 1, activeforeground = self.hdr_bg, activebackground = "#d9d9d9", width = 10, command = lambda type = "Add Exercise" : self.edit_box(type)).grid(column = 3, row = 8, sticky = "NESW")
        exertion_add_btn = tk.Button(self.exertion_frame, text = "Delete", bg = "white", relief = "solid", borderwidth = 1, activeforeground = self.hdr_bg, activebackground = "#d9d9d9", width = 10, command = lambda type = "exercise" : self.remove_item(type)).grid(column = 1, row = 8, sticky = "NESW")

        #Assigning the data from acc_data.json to a variable and setting the previous StringVars to these values (with some formatting)
        try:
            self.exertion_t = 0
            for item in self.data[self.acc_name]["week_track"][day]["exertion"]:
                    self.exertion_t = (self.exertion_t + int(self.data[self.acc_name]["week_track"][day]["exertion"][item]))
        except:
            self.exertion_t = 0
        try:
            self.intake_t = (self.data[self.acc_name]["week_track"][day]["values"]["totals"]["Calories"] + self.exertion_t)
        except:
            self.intake_t = 0
        self.intake_ts.set(f"Intake: {self.intake_t}kj")
        self.exertion_ts.set(f"Exertion: {self.exertion_t}kj")

        #Declaring the frame that houses the total label and the frame containing the progress bars
        self.totals_frame = tk.Frame(self.main_frame, borderwidth = 4, relief = "groove")
        self.totals_frame.grid(column = 3, row = 1, sticky = "NESW")
        self.totals_frame.grid_propagate(False)

        #Configuring the grid properties
        self.totals_frame.columnconfigure(0, weight = 1)
        self.totals_frame.rowconfigure(0, weight = 1)
        self.totals_frame.rowconfigure(1, weight = 19)
        
        #Declaring and placing the title label for totals above the progress bars
        self.t_totals = tk.Label(self.totals_frame, text = "Totals:", font = 10, width = 5, anchor = "w")
        self.t_totals.grid(column = 0, row = 0, sticky = "NSW")

        #Declaring and placing the frame to house the progress bars
        self.pb_frame = tk.Frame(self.totals_frame)
        self.pb_frame.grid(column = 0, row = 1, sticky = "NESW")
        self.pb_frame.grid_propagate(False)

        #Configuring the grids of the progress bar frame
        self.pb_frame.columnconfigure(0, weight = 8)
        self.pb_frame.columnconfigure(1, weight = 2)
        self.pb_frame.rowconfigure((0,1,2,4,5,6,8,9,10,12,13,14), weight = 1)
        self.pb_frame.rowconfigure((3,7,11), weight = 2)

        #Creating a blue progressbar style
        blue = ttk.Style()
        blue.theme_use("default")
        blue.configure("blue.Horizontal.TProgressbar", thickness=3, background = self.hdr_bg)

        #Creating a red progressbar style
        red = ttk.Style()
        red.theme_use("default")
        red.configure("red.Horizontal.TProgressbar", thickness=3, background = "red")

        #Creating a green progressbar style
        green = ttk.Style()
        green.theme_use("default")
        green.configure("green.Horizontal.TProgressbar", thickness=3, background = "green")

        #For loop for placing progress bars, corresponding data for intake sum and buttons for editing macro goals
        stat_attributes = {}
        for i in range(len(MACROS)):
            #Calcuating the percentage of the current total against the goal of the current macro
            current_percentage = round(((self.macro_totals[MACROS[i]]/self.macro_goals[MACROS[i]])*100))
            
            #Declaring and placing progress bar
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_pb"
            stat_attributes[MACROS[i]] = ttk.Progressbar(self.pb_frame, orient = tk.HORIZONTAL, style="blue.Horizontal.TProgressbar", maximum = (self.macro_goals[MACROS[i]] + 0.1))
            stat_attributes[MACROS[i]].grid(column = 0, row = ((i*4) + 1), columnspan = 2, sticky = "NESW")

            #Checking if the current macro is below the acceptable threshold (below 35)
            if current_percentage <= 35:
                stat_attributes[MACROS[i]].step(self.macro_totals[MACROS[i]])
                stat_attributes[MACROS[i]].configure(style = "red.Horizontal.TProgressbar")

            #Checking if the current macro is above the acceptable threshold (above 85) and still below the maximum (below 100)
            elif current_percentage >= 85 and current_percentage <= 100:
                stat_attributes[MACROS[i]].step(self.macro_totals[MACROS[i]])
                stat_attributes[MACROS[i]].configure(style = "green.Horizontal.TProgressbar")

            #If the totals are under the maximum, step the bar it's corresponding amount
            elif self.macro_totals[MACROS[i]] < self.macro_goals[MACROS[i]]:
                stat_attributes[MACROS[i]].step(self.macro_totals[MACROS[i]])
                stat_attributes[MACROS[i]].configure(style = "blue.Horizontal.TProgressbar")

            #Otherwise the total must be higher than the goal, in this case the UI will have to display a full bar in red colour to represent overshooting the goal
            else:
                stat_attributes[MACROS[i]].step(self.macro_goals[MACROS[i]])
                stat_attributes[MACROS[i]].configure(style = "red.Horizontal.TProgressbar")
            
            #Declaring and placing the title of the bar graph
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_title"
            stat_attributes[MACROS[i]] = tk.Label(self.pb_frame, text = f"{MACROS[i]}:", font = ("Arial", 10)).grid(column = 0, row = ((i*4)), sticky = "SW")

            #Declaring and placing a widget to display the percentage (calculated earlier) of the goal the user has consumed
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_perc"
            stat_attributes[MACROS[i]] = tk.Label(self.pb_frame, text = f"{current_percentage}%", font = ("Arial", 10)).grid(column = 1, row = ((i*4)), sticky = "ES")

            #Declaring and placing a label to display the total in respective units of each bar
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_total"
            stat_attributes[MACROS[i]] = tk.Label(self.pb_frame, text = f"Total: {self.macro_totals[MACROS[i]]}{UNITS[MACROS[i]]}", font = ("Arial", 10)).grid(column = 0, row = ((i*4) + 2), sticky = "NW")

            #Placing a button to give the user the option of editing their macro goals
            stat_attributes[MACROS[i]] = f"self.{MACROS[i]}_btn"
            stat_attributes[MACROS[i]] = tk.Button(self.pb_frame, text = "edit", font = ("Arial", 10), height = 1, command = lambda type = MACROS[i] : self.edit_box(type)).grid(column = 1, row = ((i*4) + 2), sticky = "NE") 
        
        #Checking if the program is running it's initial boot in order to prompt the user with a sign in
        #"Boot" referring to the initial startup of the application
        if startup == "Boot":
            self.sign()

        self.root.mainloop()

    def sign(self):
        #Destroying widgets that are not utilized by the sign in page but have been placed by the main page
        self.main_frame.destroy()
        self.btn_frame.destroy()
        self.header.grid_forget()
        self.acc_btn.destroy()

        #(Re-)Configuring grid properties of the window
        self.root.columnconfigure((3,4,5,6), weight = 0)
        self.root.columnconfigure((0,2), weight = 23)
        self.root.columnconfigure(1, weight = 26)
        self.root.rowconfigure((6,7), weight = 0)
        self.root.rowconfigure((0,2), weight = 1)
        self.root.rowconfigure((1,3,5), weight = 2)
        self.root.rowconfigure(4, weight = 56)

        self.root.rowconfigure(1, minsize = 40)
        self.root.rowconfigure((0,2), minsize = 5)

        #(Re-)Placing the header in the correct position
        self.header.grid(column = 0, row = 0, columnspan = 3, rowspan = 3, sticky = "NESW")
        self.app_ico.grid(column = 0, row = 1, sticky = "NES")
        self.t_app.grid(column = 1, row = 1, sticky = "NSW")

        #Declaring and placing a new frame to house the sign in elements
        self.log = tk.Frame(self.root)
        self.log.grid(column = 1, row = 4, sticky = "NESW")
        self.log.grid_propagate(False)

        #Configuring the grid properties of this frame
        self.log.columnconfigure((0,4), weight = 3)
        self.log.columnconfigure((1,3), weight = 2)
        self.log.columnconfigure(2, weight = 18)
        self.log.rowconfigure((0,2,3,5,6,9,10), weight = 1)
        self.log.rowconfigure((1,4,7), weight = 3)
        self.log.rowconfigure(8, weight = 8)

        #Declaring and placing a frame to house the "Sign in" title and icon
        self.acc_logo = tk.Frame(self.log)
        self.acc_logo.grid(column = 1, row = 1, columnspan = 3, sticky = "NESW")
        self.acc_logo.columnconfigure(1, weight = 1)
        self.acc_logo.columnconfigure((0,2), weight = 2)
        
        #Placing the account icon and "Sign in" text in the aforementioned frame
        self.acc_ico = tk.Label(self.acc_logo, image = self.acc_img).grid(column = 0, row = 0, sticky = "NES")
        self.acc_title = tk.Label(self.acc_logo, text = "Sign in", font = ("bold", 15), width = 1).grid(column = 1, row = 0, sticky = "NESW")

        #Declaring, placing and configuring a frame to house the sign-in/sign-out buttons
        self.options = tk.Frame(self.log)
        self.options.grid(column = 1, row = 9, columnspan = 3, sticky = "NESW")
        self.options.columnconfigure((0,2), weight = 2)
        self.options.columnconfigure((1), weight = 1)
        self.options.rowconfigure(0, weight = 1)

        #Declaring and placing the aforementioned buttons
        self.sign_in = tk.Button(self.options, text = "Sign In", bg = "white", height = 1, width = 1, command = self.sign_valid).grid(column = 2, row = 0, sticky = "NESW")
        self.sign_up = tk.Button(self.options, text = "Sign Up", bg = "white", height = 1, width = 1, command = self.sign_up_valid).grid(column = 0, row = 0, sticky = "NESW")
        self.root.bind("<Return>", lambda event : self.sign_valid())

        #Declaring stringvars for the username and password entries
        self.u_nam = tk.StringVar()
        self.u_pass = tk.StringVar()
        
        #Declaring a stringvar for the error display allowing a variety of errors to be displayed (not currently explored)
        self.error_txt = tk.StringVar()
        
        #Declaring and placing all entried and labels present in the sign in frame
        self.t_user = tk.Label(self.log, text = "Username:", font = 10, height = 1).grid(column = 2, row = 3, sticky = "NSW")
        self.e_user = tk.Entry(self.log, textvariable = self.u_nam, bg = "white", font = 10, border = 1).grid(column = 2, row = 4, sticky = "NEW")
        self.t_pass = tk.Label(self.log, text = "Password:", font = 10, height = 1).grid(column = 2, row = 6, sticky = "NSW")
        self.e_pass = tk.Entry(self.log, textvariable = self.u_pass, bg = "white", font = 10, border = 1).grid(column = 2, row = 7, sticky = "NEW")
        self.t_error = tk.Label(self.log, textvariable = self.error_txt, width = 5, font = ("Arial", 7), fg = "red", height = 4).grid(column = 2, row = 8, sticky = "NEW")
    
    #Sign in validation
    def sign_valid(self):
        #A try statement is used for easy validation
        #This is utilized as the if statment will throw a key error if the username inputted does not exist as a key
        #This means that the user must enter a real and present username
        try:
            #Checks that the password entered is the correct password for the associated username
            if (self.data[self.u_nam.get()]["password"]) == self.u_pass.get():
                    #Sets the active user to the username entered
                    self.acc_name = self.u_nam.get()
                    #Unbinds return from signing in the user as they have already(/are currently) being signed in
                    self.root.unbind("<Return>")
                    #Opens the main page under their account and corresponding data
                    self.main_window("Monday", "True")
            #If the password is entered incorrectly the program will display an error
            else:
                self.error_txt.set("Key Error:\nplease try again,\nthe username or password you have entered is incorrect")
        #If a username that does not exist is entered, the program will display an error
        except:
            self.error_txt.set("Key Error:\nplease try again,\nthe username or password you have entered is incorrect")

    #Sign up validation
    def sign_up_valid(self):
        #Checks that the user has enetered a username
        if self.u_nam.get() != "":
            #Checks that the user has enetered a password
            if self.u_pass.get() != "":
                #Opens a new dictionary under there name using the developer account (User_0) as a blueprint
                self.data[self.u_nam.get()] = dict(self.data["User_0"])
                #Sets the password of this new account to the password entered
                self.data[self.u_nam.get()]["password"] = self.u_pass.get()
                #json dump so that the user cannot lose the new account by accidentally terminating or alt+f4 the program
                with open("acc_data.json", "w") as f:
                    json.dump(self.data, f, indent = 4)
                #Reopen the json file
                with open("acc_data.json", "r+") as f:
                    self.data = json.load(f)
                #Setting the active user to the username given
                self.acc_name = self.u_nam.get()
                #Opens the main page under their account and corresponding data 
                self.main_window("Monday", "True")
            #Displays an error if there is no password given
            else:
                self.error_txt.set("Key Error:\nplease try again,\nPlease enter a username and password\nin the respective entries")
        #Displays an error if there is no username given
        else:
            self.error_txt.set("Key Error:\nplease try again,\nPlease enter a username and password\nin the respective entries")

    #Method for setting the properties of buttons based upon the active day
    #This means the active day's corresponding button will be unreactive, unusable and greyed
    #And all other buttons will be reactivated
    def day_btn_set(self, startup, day = ""):
            for i in range(len(self.active_day)):
                self.active_day[WEEK_DAYS[i]] = ["normal", "white"]
            if day != "":
                self.day = day
            self.active_day[self.day] = ["disabled", "#d9d9d9"]
            if startup == "False":
                self.main_window(self.day, "False")

    #Method for placing daily buttons
    def btn_place(self):
        for i in range(len(WEEK_DAYS)):
            self.day_btns[WEEK_DAYS[i]] = tk.Button(self.btn_frame, text = WEEK_DAYS[i], bg = "white", relief = "solid", borderwidth = 1, activeforeground = self.hdr_bg, activebackground = "#d9d9d9", disabledforeground = self.hdr_bg, width = 1, command = lambda day = WEEK_DAYS[i]: self.day_btn_set("False", day))
            self.day_btns[WEEK_DAYS[i]].config(state = self.active_day[WEEK_DAYS[i]][0], bg = self.active_day[WEEK_DAYS[i]][1])
            self.day_btns[WEEK_DAYS[i]].grid(column = ((i * 2) + 1), row = 1, sticky = "NESW")

    #Method for opening the value editor pop-up
    def edit_box(self, type):
        self.root.bind("<Enter>", lambda event : self.main_window(self.day, "False"))
        Edit(type).edit_popup(self.acc_name, self.day)

    #Command for removing an item from either the menu or exercise list
    def remove_item(self, type):
        if type == "menu":
            self.data[self.acc_name]["week_track"][self.day]["menu"].pop(self.menu[self.current_menu_item])
            with open("acc_data.json", "w") as f:
                json.dump(self.data, f, indent = 4)
            self.current_menu_item = (int(self.item_select.get()) - 2)
            self.main_window(self.day, "False")
        elif type == "exercise":
            self.data[self.acc_name]["week_track"][self.day]["exertion"].pop(self.exercise[self.current_e_menu_item])
            with open("acc_data.json", "w") as f:
                json.dump(self.data, f, indent = 4)
            self.current_e_menu_item = (int(self.item_e_select.get()) - 2)
            self.main_window(self.day, "False")

    def update_item(self):
        self.current_menu_item = (int(self.item_select.get()) - 1)
        self.main_window(self.day, "False")
    
    def update_exercise(self):
        self.current_e_menu_item = (int(self.item_e_select.get()) - 1)
        self.main_window(self.day, "False")