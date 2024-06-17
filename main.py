from error import Error
from root import Main
from time import *

try:
    main_window = Main("Main Menu", "William Martin")
    main_window.main_window()
    #main_window.errorcall()

    error1 = Error("integer")
    error1.er_popup()

    str_txt = input("Test: ")
    int(str_txt)

except:
    error1 = Error("fatal")
    error1.er_popup()