class Car:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._manufacture = None


    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, value ):
        self._motor = value


    @property
    def manufacture(self):
        return self._manufacture

    @manufacture.setter
    def manufacture(self, value ):
        self._maufacture = value


class Motor:
    def __init__(self, name):
        self.name = name

class Factory:
    def __init__(self, name):
        self.name = name

hilux = Car('Hilux')
toyta = Factory('Toyta')
motor_1 = Motor('2.8')
hilux.factory = toyta
hilux.motor = motor_1
print(hilux.name)
print(hilux.motor.name)
print(hilux.factory.name)