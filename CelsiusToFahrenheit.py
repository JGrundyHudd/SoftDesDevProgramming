celsius = input('Please enter a temperature in celsius followed by the unit "C": ')
print(celsius + ' is ' + str(float(celsius[:-1]) * 1.8 + 32) + 'F')
