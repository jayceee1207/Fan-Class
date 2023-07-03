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
            self.__speed = int(input('Set the fan speed: '))
            if self.__speed == 1:
                self.__speed = 'Slow'
            elif self.__speed == 2:
                self.__speed = 'Medium'
            elif self.__speed == 3:
                self.__speed = 'Fast'

#create set radius

#create set color

#create set power


#create getters methods

#create get speed

#create get radius

#create get color

#create get power
