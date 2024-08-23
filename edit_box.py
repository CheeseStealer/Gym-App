import tkinter as tk
from tkinter import ttk
import json

#Declaring all macros in a dictionary as a constant
MACROS = ["Calories", "Protein", "Carbs", "Fat"]

class Edit:
    def __init__(win, edit_type):
        #Making the edit type acceccable to the whole class
        win.edit = edit_type

        #Opening the json file
        with open("acc_data.json", "r+") as f:
            win.data = json.load(f)
        
        #Setting some basic window colours and properties for easy theme trialing
        #and the addition of varying window styles
        win.win_bac = "white"
        if win.edit in MACROS:
            win.win_title = f"{win.edit} Goal - Editor"
        else:
            win.win_title = f"{win.edit} - Editor"
        win.er_msg = "Unexpected error"
        win.btn_brdr = "light grey"
        win.img_txt_bg = "white"
        win.btn_txt = "black"
        win.btn_fg = "white"
        
        #s prefix - string
        #i prefix - integer
        #setting the number of entry box assets
        if win.edit in MACROS:
            win.s_edit_assets = 0
            win.i_edit_assets = 1
        elif win.edit == "Add Meal":
            win.s_edit_assets = 1
            win.i_edit_assets = 4
        elif win.edit == "Edit Meal":
            win.s_edit_assets = 1
            win.i_edit_assets = 4
        elif win.edit == "Add Exercise":
            win.s_edit_assets = 1
            win.i_edit_assets = 1
        elif win.edit == "Edit Exercise":
            win.s_edit_assets = 1
            win.i_edit_assets = 1

    def edit_popup(win, acc_name, day):
        #Declaring basic window properties
        popup = tk.Toplevel()
        #Using grab_set here so the user cannot interact with the main window during the alteration
        popup.grab_set()
        popup.title(win.win_title)
        popup.iconbitmap("wrench.ico")
        popup.resizable(0,0)
        popup.configure(bg = win.win_bac)

        #Setting the window size dependant on the ammount of assets being edited
        if (win.s_edit_assets + win.i_edit_assets) == 1:
            popup.geometry("350x150")
        elif (win.s_edit_assets + win.i_edit_assets) == 2:
            popup.geometry("350x250")
        elif (win.s_edit_assets + win.i_edit_assets) == 5:
            popup.geometry("350x400")

        #Function for confirm button
        def click_conf():
            #Checks if the data being taken is a macro by checking if only one attribute is being edited
            if (win.s_edit_assets + win.i_edit_assets) == 1:
                #A try except statement is used as the program will throw an error in the case the given input is not an integer
                #This happens as the new_data string we are getting is attempting to be turned into a string and then integer
                #At any point this could throw an error for either being NAN or a alphabetic character or special character
                #This covers all cases
                try:
                    #Checking if the input is a positive integer
                    if int(str(new_data.get())) >= 0:
                        #Checking if the input is an integer above 0
                        if int(str(new_data.get())) > 0:
                            #Setting the selected goal to the new integer inputted
                            win.data[acc_name]["week_track"][day]["values"]["goals"][win.edit] = int(str(new_data.get()))
                            #Update the json with this new alteration
                            with open("acc_data.json", "w") as f:
                                json.dump(win.data, f, indent = 4)
                            #Close the pop-up
                            popup.destroy()
                        else:
                            #Displaying an error to inform the user they must enter a number higher than zero
                            error_str.set("Invalid input,\nplease enter a number higher than zero")
                    else:
                        #Displaying an error to inform the user they must enter a number that is positive
                        error_str.set("Invalid input,\nplease enter a positive integer")
                except:
                    #Displaying an error to inform the user they must enter an integer
                    error_str.set("Invalid input,\nplease enter an integer")
            #Checks if the data being taken is a new meal
            elif win.edit == "Add Meal":
                if str(food_item.get()) != "":
                    #Using a try/except statment to validate integer inputs
                    #This will throw an error if an alpha or special character is input
                    try:
                        #Declaring the data taken in a dictionary
                        new_item_dict = {"Calories" : int(str(cal.get())), "Protein" : int(str(pro.get())), "Carbs" : int(str(carb.get())), "Fat" : int(str(fat.get()))}
                        #Checking that all entered data is a positive number
                        if int(str(cal.get())) >= 0 and int(str(pro.get())) >= 0 and int(str(carb.get())) >= 0 and int(str(carb.get())) >= 0:
                            #Checking that the calories entered is not 0 as this would be impossible
                            if int(str(cal.get())) > 0:
                                #Creating a new food dictionary in the json dictionary path and assigning the new dictionary declared above to it
                                win.data[acc_name]["week_track"][day]["menu"][str(food_item.get())] = new_item_dict
                                #Writing this addition to the json
                                with open("acc_data.json", "w") as f:
                                    json.dump(win.data, f, indent = 4)
                                #Close the pop-up
                                popup.destroy()
                            #Display error to inform user they have entered an invalid calorie value of 0
                            else:
                                error_str.set("Invalid input,\nplease enter a calorie value above zero")
                        #Display error to inform user they have entered a negative integer value on any of the entry fields
                        else:
                            error_str.set("Invalid input,\nplease enter a positive integer")
                    #Display error to inform user they have left an integer entry blank
                    except:
                        error_str.set("Invalid input,\nplease enter an integer")
                #Display error to inform user they have not entered a meal name
                else:
                    error_str.set("Invalid input,\nplease enter a meal name")

            #Checks if the data being taken is an exercize
            elif win.edit == "Add Exercise":
                #Creating a new exercise in the json dictionary directory and assigning the calorie burn as its value
                win.data[acc_name]["week_track"][day]["exertion"][str(activity.get())] = int(str(c_burn.get()))
                #Writing this addition to the json
                with open("acc_data.json", "w") as f:
                    json.dump(win.data, f, indent = 4)
                #Close the pop-up
                popup.destroy()

        #Function for the exit button
        def click_quit():
            popup.destroy()

        #Configuring the window's grid properties
        popup.columnconfigure((0,4), weight = 1)
        popup.columnconfigure((1,3), weight = 2)
        popup.columnconfigure((2), weight = 5)
        popup.rowconfigure((0,5), weight = 1)
        popup.rowconfigure(1, weight = 2)
        popup.rowconfigure(4, weight = 2)

        #Creating a label based on what the user has requested to edit to display as a title
        if win.edit in MACROS:
            active_title = tk.Label(popup, text = f"Edit {win.edit}", bg = win.win_bac, anchor = "w")
        else:
            active_title = tk.Label(popup, text = win.edit, bg = win.win_bac, anchor = "w")
        active_title.grid(column = 1, row = 1, columnspan = 3, sticky = "NESW")

        #Declaring and gridding the frame that contains all entries
        e_data_frame = tk.Frame(popup, borderwidth = 4, relief = "groove", bg = win.win_bac)
        e_data_frame.grid(column = 1, row = 2, columnspan = 3, sticky = "NESW")
        e_data_frame.grid_propagate(False)

        #Declaring a string var and label for displaying errors to the user (also placing it)
        error_str = tk.StringVar()
        error = tk.Label(popup, textvariable = error_str, fg = "red", bg = win.win_bac, font = 7, width = 10, height = 2).grid(column = 1, row = 3, columnspan = 3, sticky = "NESW")

        #Exit and confirm buttons
        ext_btn = tk.Button(popup, text = "Exit", font = 1, width = 5, command = click_quit, bg = win.btn_fg, fg = win.btn_txt).grid(column = 1, row = 4, sticky = "NESW")
        confirm_btn = tk.Button(popup, text = "Confirm", font = 1, width = 5, command = click_conf, bg = win.btn_fg, fg = win.btn_txt).grid(column = 3, row = 4, sticky = "NESW")

        #Checking if the edit requested has only one asset to alter
        if (win.s_edit_assets + win.i_edit_assets) == 1:
            #Configuring the window slightly to better size the entry frame and error box
            popup.rowconfigure(3, weight = 4)
            popup.rowconfigure(2, weight = 16)
            
            #Configuring the frame's grid properties
            e_data_frame.columnconfigure((0,3), weight = 1)
            e_data_frame.columnconfigure(1, weight = 2)
            e_data_frame.columnconfigure(2, weight = 6)
            e_data_frame.rowconfigure((0,2), weight = 1)
            e_data_frame.rowconfigure(1, weight = 2)

            #Creating a Label next to an entry box for the user to input the required data
            new_data = tk.StringVar()
            t_edit = tk.Label(e_data_frame, text = f"New {win.edit} Goal:", font = 10, bg = win.win_bac).grid(column = 1, row = 1, sticky = "NESW")
            e_edit = tk.Entry(e_data_frame, textvariable = new_data, font = 10).grid(column = 2, row = 1, sticky = "NESW")
        
        #Checking if the edit requested has two assets to alter
        elif (win.s_edit_assets + win.i_edit_assets) == 2:
            #Configuring the window slightly to better size the entry frame and error box
            popup.rowconfigure(3, weight = 3)
            popup.rowconfigure(2, weight = 20)
            
            #Configuring the frame's grid properties
            e_data_frame.columnconfigure((0,3), weight = 1)
            e_data_frame.columnconfigure(1, weight = 2)
            e_data_frame.columnconfigure(2, weight = 6)
            e_data_frame.rowconfigure((0,2,4), weight = 1)
            e_data_frame.rowconfigure((1,3), weight = 2)

            #Creating Labels adjacent to corresponding entry boxs for the user to input the required data
            activity = tk.StringVar()
            t_activity = tk.Label(e_data_frame, text = "Activity Name:", font = 10, bg = win.win_bac).grid(column = 1, row = 1, sticky = "NESW")
            e_activity = tk.Entry(e_data_frame, textvariable = activity, font = 10).grid(column = 2, row = 1, sticky = "NESW")

            c_burn = tk.StringVar()
            t_burn = tk.Label(e_data_frame, text = "Calories Burned:", font = 10, bg = win.win_bac).grid(column = 1, row = 3, sticky = "NESW")
            e_burn = tk.Entry(e_data_frame, textvariable = c_burn, font = 10).grid(column = 2, row = 3, sticky = "NESW")

        #Checking if the edit requested has five assets to alter
        elif (win.s_edit_assets + win.i_edit_assets) == 5:
            #Configuring the window slightly to better size the entry frame and error box
            popup.rowconfigure(3, weight = 3)
            popup.rowconfigure(2, weight = 24)

            #Configuring the frame's grid properties
            e_data_frame.columnconfigure((0,3), weight = 1)
            e_data_frame.columnconfigure(1, weight = 2)
            e_data_frame.columnconfigure(2, weight = 6)
            e_data_frame.rowconfigure((0,2,4,6,8,10), weight = 1)
            e_data_frame.rowconfigure((1,3,5,7,9), weight = 2)

            #Creating Labels adjacent to corresponding entry boxs for the user to input the required data
            food_item = tk.StringVar()
            t_food = tk.Label(e_data_frame, text = f"New Meal:", font = 10, bg = win.win_bac).grid(column = 1, row = 1, sticky = "NESW")
            e_food = tk.Entry(e_data_frame, textvariable = food_item, font = 10).grid(column = 2, row = 1, sticky = "NESW")

            cal = tk.StringVar()
            t_cal = tk.Label(e_data_frame, text = f"Calories:", font = 10, bg = win.win_bac).grid(column = 1, row = 3, sticky = "NESW")
            e_cal = tk.Entry(e_data_frame, textvariable = cal, font = 10).grid(column = 2, row = 3, sticky = "NESW")

            pro = tk.StringVar()
            t_pro = tk.Label(e_data_frame, text = f"Protein:", font = 10, bg = win.win_bac).grid(column = 1, row = 5, sticky = "NESW")
            e_pro = tk.Entry(e_data_frame, textvariable = pro, font = 10).grid(column = 2, row = 5, sticky = "NESW")

            carb = tk.StringVar()
            t_carb = tk.Label(e_data_frame, text = f"Carb:", font = 10, bg = win.win_bac).grid(column = 1, row = 7, sticky = "NESW")
            e_carb = tk.Entry(e_data_frame, textvariable = carb, font = 10).grid(column = 2, row = 7, sticky = "NESW")

            fat = tk.StringVar()
            t_fat = tk.Label(e_data_frame, text = f"Fat:", font = 10, bg = win.win_bac).grid(column = 1, row = 9, sticky = "NESW")
            e_fat = tk.Entry(e_data_frame, textvariable = fat, font = 10).grid(column = 2, row = 9, sticky = "NESW")

        popup.mainloop()