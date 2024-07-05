from root import Main
from time import *
from error import Error

try:
    while True:
        main_window = Main("Main", "William Martin")
        main_window.main_window()
        #main_window.errorcall()

except:
    error1 = Error("fatal")
    error1.er_popup()