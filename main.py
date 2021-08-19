import numpy as np
import matplotlib.pyplot as plt
import cirq
import cirq_google

# print(cirq_google.Foxtail)

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit) ** 0.5,  # Square root of NOT.
    #cirq.X(qubit),
    cirq.measure(qubit, key='m')  # Measurement.
)
print("Circuit:")
print(circuit)

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=100)
print(type(result))
print("Results:")
print(result)

#graph outcome
binarystring = list(str(result))
binarystring = binarystring[2:]
zeros = 0
ones = 0
for x in binarystring:
    if x == "0":
        zeros +=1
    else:
        ones += 1

print("0: " + str(zeros))
print("1: " + str(ones))

data = {'0':zeros, '1':ones}
output = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(output, values, color='blue',
        width=0.4)

plt.xlabel("Output")
plt.ylabel("Occurrences")
plt.title("Ones and zeros")
plt.show()