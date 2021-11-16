# Calculate the sum of the first 100 numbers of the Fibonacci sequence

# First two Fibonacci numbers
fibo1 = 0
fibo2 = 1

# Stores Fibonnaci sequence in a list
fibonacci = [0, 1]

# Calculate new Fibonacci number
for i in range(98):
    new_fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = new_fibo
    fibonacci.append(new_fibo)

# Calculate sum of the first 100 Fibonacci numbers
total = 0
for number in range(len(fibonacci)):
    total = total + fibonacci[number]

# Print results
print(f"The sum of the first 100 numbers of the Fibonacci sequence is equal to {total}.")