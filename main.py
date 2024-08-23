from root import Main
from time import *
from error import Error

#A try statement is used so that the program will be able to continue running if an error is occured
#try:
while True:
    main_window = Main("Main", "User_0")
    main_window.main_window("Monday", "Boot")

#The except statement allows the program to display an error if a fatal error occurs
#except:
#    error1 = Error("white")
#    error1.er_popup()