def is_binary_palindrome(x):
    n_bits = x.bit_length()
    for i in range(n_bits // 2):
        if ((x >> i) & 1) != ((x >> (n_bits - 1 - i)) & 1):
            return False
    return True


def generate_binary_palindromes(n):
    max_len = n.bit_length()
    for length in range(max_len, 0, -1):
        half_len = (length + 1) // 2
        start = 1 << (half_len - 1)
        end = 1 << half_len
        for first_half in range(end - 1, start - 1, -1):
            first_half_bin = bin(first_half)[2:]
            if length % 2 == 0:
                pal_bin = first_half_bin + first_half_bin[::-1]
            else:
                pal_bin = first_half_bin + first_half_bin[-2::-1]
            pal_num = int(pal_bin, 2)
            if pal_num <= n:
                return pal_num
    return 0  # Caso nenhum palíndromo seja encontrado

# Exemplo:
n = 9945

if is_binary_palindrome(n):
    resultado = n
else:
    resultado = generate_binary_palindromes(n)

print(resultado)