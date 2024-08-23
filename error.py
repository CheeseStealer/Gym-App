import tkinter as tk
from tkinter import ttk

class Error:
    def __init__(er_win, error):
        #Declaring error type as a variable across the whole class
        er_win.error = error
        
        #Declaring some variables to assign colours and formats uniformly across the window
        #This also allows for easy editing of the theme of the window
        #The if statement allows for an endless amount of window presets for specifc error types
        #Fatal error
        if er_win.error == "fatal":
            er_win.win_bac = "dark red"
            er_win.win_title = "Fatal Error"
            er_win.er_msg = "I don't even know what you did"
            er_win.btn_brdr = "black"
            er_win.img_txt_bg = "dark red"
            er_win.btn_txt = "white"
            er_win.btn_fg = "black"
        #Default error
        else:
            er_win.win_bac = "white"
            er_win.win_title = "Unexpected Error"
            er_win.er_msg = "Unexpected error"
            er_win.btn_brdr = "light grey"
            er_win.img_txt_bg = "white"
            er_win.btn_txt = "black"
            er_win.btn_fg = "white"

    def er_popup(er_win):
        #Declaring basic window properties
        popup = tk.Toplevel()
        #Using grab_set here so the user cannot interact with the main window during the error
        popup.grab_set()
        popup.geometry("350x125")
        popup.title(er_win.win_title)
        popup.iconbitmap("er_icon.ico")
        popup.resizable(0,0)
        popup.configure(bg=er_win.win_bac)

        #Function for the ok button to exit the window
        def click_quit():
            popup.destroy()

        #Configuring the window's grid properties
        popup.columnconfigure((1,2,3,4), weight = 4)
        popup.columnconfigure((0,5), weight = 1)
        popup.rowconfigure((0,1,2,3), weight = 4)
        popup.rowconfigure((4,6), weight = 2)
        popup.rowconfigure(5, weight = 1)

        #Declaring the error png as a photo image
        error_name = tk.PhotoImage(file = 'error.png').subsample(12,12)
        
        #Creating the error png and associated text along with a grey bar across the bottom and "OK" exit button
        er_img_lbl = tk.Label(popup, image = error_name, bg = er_win.img_txt_bg).grid(column = 1, row = 1, sticky = "NESW")
        boarder_lbl = tk.Label(popup, bg = er_win.btn_brdr).grid(column = 0, row = 4, columnspan = 6, rowspan = 3, sticky = "NESW")
        er_txt = tk.Label(popup, text = er_win.er_msg, font = 1, bg = er_win.img_txt_bg, fg = er_win.btn_txt).grid(column = 2, row = 1, columnspan = 2, sticky = "NSW")
        ex_btn = tk.Button(popup, text = "OK", font = 1, command = click_quit, bg = er_win.btn_fg, fg = er_win.btn_txt).grid(column = 4, row = 5, sticky = "NESW")

        popup.mainloop()