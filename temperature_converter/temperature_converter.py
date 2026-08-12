def temperature_converter(temp,unit):
    if unit=='c':
        return temp * 9/5 + 32
    elif unit=='f':
        return (temp - 32)*5/9
print(temperature_converter(25,'c'))
print(temperature_converter(77,'f'))