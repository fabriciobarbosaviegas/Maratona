import sys

def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        merged = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, inv_count = merge_sort(arr)
    return inv_count


for line in sys.stdin:
    parts = list(map(int, line.strip().split()))
    if not parts or parts[0] == 0:
        break
    n = parts[0]
    seq = parts[1:]
    if len(seq) != n:
        continue
    inv = count_inversions(seq)
    print("Carlos" if inv % 2 == 0 else "Marcelo")
