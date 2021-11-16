# Convert a list of temparutes

# Nota que o exercício está pedindo para converter o último item da tabela de Kelvin para Celsius porém na imagem da tabela está de Kelvin para Fahrenheit.

temperatures = {
    "celsius_fahrenheit": [37, 0],
    "fahrenheit_celsius": [212, -40],
    "kelvin_celsius": [0]
}

temperatures_converted = {
    "celsius_fahrenheit": [],
    "fahrenheit_celsius": [],
    "kelvin_celsius": []
}

# Calculate Celsius to Fahrenheit
for celsius in temperatures["celsius_fahrenheit"]:
    fahrenheit = (celsius * 9 / 5) + 32
    temperatures_converted["celsius_fahrenheit"].append(fahrenheit)

# Calculate Fahrenheit to Celsius
for fahrenheit in temperatures["fahrenheit_celsius"]:
    celsius= (fahrenheit - 32) * 5 / 9
    temperatures_converted["fahrenheit_celsius"].append(celsius)

# Calculate Kelvin to Celsius
for kelvin in temperatures["kelvin_celsius"]:
    celsius = kelvin - 273.15
    temperatures_converted["kelvin_celsius"].append(celsius)


# Print Celsius to Fahrenheit
for i in range(len(temperatures["celsius_fahrenheit"])):
    celsius = temperatures["celsius_fahrenheit"]
    fahrenheit = temperatures_converted["celsius_fahrenheit"]
    print(f"{celsius[i]:.2f}° Celsius = {fahrenheit[i]:.2f}° Fahrenheit")

print()

# Print Fahrenheit to Celsius
for i in range(len(temperatures["fahrenheit_celsius"])):
    fahrenheit = temperatures["fahrenheit_celsius"]
    celsius = temperatures_converted["fahrenheit_celsius"]
    print(f"{fahrenheit[i]:.2f}° Fahrenheit = {celsius[i]:.2f}° Celsius")

print()

# Print Kelvin to Celsius
for i in range(len(temperatures["kelvin_celsius"])):
    kelvin = temperatures["kelvin_celsius"]
    celsius = temperatures_converted["kelvin_celsius"]
    print(f"{kelvin[i]:.2f}° Kelvin = {celsius[i]:.2f}° Celsius")
