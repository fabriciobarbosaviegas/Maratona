import math

M = int(input())

if M == 0:
    qubits = 0
else:
    total_bits_to_simulate = M * 1000000 * 8

    if total_bits_to_simulate == 0: 
        qubits = 0
    else:
        qubits = (total_bits_to_simulate - 1).bit_length()
        
print(qubits)