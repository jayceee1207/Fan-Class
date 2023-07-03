#create a class Fan
class Fan:
#create constructor (default values)
    def __init__(self,speed = 'Slow', radius = 5, color = 'blue', on = 0):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    #create setters
    #create set speed
    def set_speed(self):
            self.__speed = int(input('Enter fan speed: '))
            if self.__speed == 1:
                self.__speed = 'Slow'
            elif self.__speed == 2:
                self.__speed = 'Medium'
            elif self.__speed == 3:
                self.__speed = 'Fast'

    #create set radius
    def set_radius(self):
        self.__radius = float(input('Enter fan radius: '))

    #create set color
    def set_color(self):
        self.__color = str(input('Enter fan color: '))

    #create set power
    def set_power(self):
        self.__on = input('Enter fan power:  ')
        if self.__on == '0':
            self.__on = 'The fan is off'
        elif self.__on == '1':
            self.__on = 'The fan is on'

    #create getters methods
    #create get speed
    def get_speed(self):
        return self.__speed
    
    #create get radius
    def get_radius(self):
        return self.__radius

    #create get color
    def get_color(self):
        return self.__color

    #create get power
    def get_on(self):
        return self.__on
