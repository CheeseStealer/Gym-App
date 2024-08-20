from root import Main
from time import *
from error import Error

try:
    while True:
        main_window = Main("Main", "User_0")
        main_window.main_window("Monday", "Boot")

except:
    error1 = Error("white")
    error1.er_popup()