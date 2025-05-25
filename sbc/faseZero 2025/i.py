import math

m_str = input()
m = int(m_str)

total_classical_bits = m * 1000000 * 8

if total_classical_bits == 0:
    num_qubits = 0
else:
    num_qubits = math.ceil(math.log2(total_classical_bits))

print(num_qubits)