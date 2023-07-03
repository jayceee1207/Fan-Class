#John Carlo Ablay
#BSCPE 1-5
#Fan Class
#July 1, 2023

#import fan

import pyfiglet
import emoji
from pyfiglet import Figlet
from termcolor import colored 

design = ("*********************************************************")
subject_name = ("Object-Oriented Programming")
program_name = Figlet(font='banner3-D')
author_name = ("Programmed by: John Carlo R. Ablay")

design_center = design.center(120)
subject_name_center = subject_name.center(120)
author_name_center = author_name.center(120)



print("\u001b[35;1m", design_center)
print("\u001b[33;1m", subject_name_center)
print("\u001b[33;1m",author_name_center)
print("\u001b[35;1m",design_center)
print(colored(program_name.renderText("FAN"), 'green').center(120))

from Fan import Fan

#create object
fan1 = Fan()
fan2 = Fan()

#display fan 1
fan1.set_speed()
fan1.set_radius()
fan1.set_color()
fan1.set_power()

print('\033[95m''\nFan 1')
print('\033[96m''Speed:', "\u001b[37m", fan1.get_speed())
print('\033[96m''Radius:', "\u001b[37m", fan1.get_radius())
print('\033[96m''Color:', "\u001b[37m", fan1.get_color())
print('\033[96m''Power:', "\u001b[37m", fan1.get_power())

#set values for fan 2
fan2.set_speed()
fan2.set_radius()
fan2.set_color()
fan2.set_power()

#return values for fan 2
print('\033[95m''\nFan 2')
print('\033[96m''Speed:', "\u001b[37m", fan2.get_speed())
print('\033[96m''Radius:', "\u001b[37m", fan2.get_radius())
print('\033[96m''Color:', "\u001b[37m",  fan2.get_color())
print('\033[96m''Power:', "\u001b[37m", fan2.get_power())

print("\nThank you for using my program! Have a good day!")
print(emoji.emojize('Have a good day! :grinning_face:'))
