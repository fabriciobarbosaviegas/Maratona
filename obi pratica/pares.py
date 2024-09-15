def is_valid_pair(num1, num2):
    # Check if the digits in num1 and num2 are distinct
    digits = set(str(num1) + str(num2))
    if len(digits) != 10:
        return False
    return True

def find_pairs(N):
    pairs_found = False
    for num1 in range(10000, 100000):
        num2 = num1 * N
        if num2 >= 100000:
            break
        if is_valid_pair(num1, num2):
            pairs_found = True
            print(f"{num2:05d} / {num1:05d} = {N}")
    return pairs_found

while True:
    N = int(input())
    if N == 0:
        break
    
    if not find_pairs(N):
        print(f"There are no solutions for {N}.")
    
    print()  # Blank line between different values of N
