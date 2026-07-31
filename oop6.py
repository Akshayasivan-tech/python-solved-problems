class Thermometer:
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_fahrenheit(self):
        return (self.__temperature * 9/5) + 32

    def set_temperature(self, new_temp):
        if new_temp >= -273.15:
            self.__temperature = new_temp
        else:
            print("Error: Temperature cannot be below Absolute Zero.")

t = Thermometer(25)
print("Fahrenheit:", t.get_fahrenheit())

t.set_temperature(-300)