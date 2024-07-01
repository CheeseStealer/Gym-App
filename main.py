from root import Main
from time import *
from error import Error

try:
    main_window = Main("Main Menu", "William Martin")
    main_window.main_window()
    #main_window.errorcall()

except:
    error1 = Error("fatal")
    error1.er_popup()