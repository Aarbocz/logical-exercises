# Convert Celsius to Fahrenheit and Fahrenheit to Celsius

# Nota que no exercício está escrito "De Celsius para Fahrenheit: subtraia 32, multiplique por 5 e divida por 9" porém esta fórmula é de Fahrenheit para Celsius e não de Celsius para Fahrenheit.

print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")

menu_choice = input("Choose one: ")

if menu_choice == '1':
    celsius = float(input("Type the temperature in Celsius: "))

    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.2f}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit")

elif menu_choice == '2':
    fahrenheit = float(input("Type the temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit:.2f}° Fahrenheit is equal to {celsius:.2f}° Celsius")

else:
    print("Invalid option.")
