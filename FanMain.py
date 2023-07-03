#John Carlo Ablay
#BSCPE 1-5
#Fan Class
#July 1, 2023

#import fan
from Fan import Fan

#create object
fan1 = Fan()
fan2 = Fan()

#display fan 1
fan1.set_speed()
fan1.set_radius()
fan1.set_color()
fan1.set_power()

print('\nFan 1')
print('Speed:', fan1.get_speed())
print('Radius:', fan1.get_radius())
print('Color:', fan1.get_color())
print('Power:', fan1.get_power())

#set values for fan 2
fan2.set_speed()
fan2.set_radius()
fan2.set_color()
fan2.set_power()

#return values for fan 2
print('\nFan 2')
print('Speed:', fan2.get_speed())
print('Radius:', fan2.get_radius())
print('Color:', fan2.get_color())
print('Power:', fan2.get_power())
