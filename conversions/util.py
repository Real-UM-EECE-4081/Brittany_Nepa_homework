def fahrenheit_to_celsius(fahrenheit):
    celsius = float((fahrenheit-32))/(9/5)
    if fahrenheit <= -459.67:
        return "That is an absolute zero / impossible...try again"
    else:
        celsius = float((fahrenheit-32))/(9/5)
        return fahrenheit

def celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius * 9/5 + 32)
    if celsius <= -273.15:
        return "That is an absolute zero / impossible...try again"
    else:
        fahrenheit = float(celsius * 9/5 + 32)
        return fahrenheit

print(celsius_to_fahrenheit(-273.4))
print(fahrenheit_to_celsius(-459.67))
