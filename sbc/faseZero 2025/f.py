import collections
import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
queries = [int(input()) for _ in range(q)]

map_sumas_kl = collections.defaultdict(list)
for k_idx in range(n):
    for l_idx in range(k_idx + 1, n):
        s_kl = a[k_idx] + a[l_idx]
        map_sumas_kl[s_kl].append(k_idx)

for s in map_sumas_kl:
    map_sumas_kl[s].sort()

results = []
for target_x in queries:
    count = 0
    for i_idx in range(n):
        for j_idx in range(i_idx + 1, n):
            sum_ij = a[i_idx] + a[j_idx]
            target_sum_kl = target_x - sum_ij
            
            if target_sum_kl in map_sumas_kl:
                k_list = map_sumas_kl[target_sum_kl]
                
                pos = bisect.bisect_right(k_list, j_idx)
                
                count += len(k_list) - pos
    results.append(count)

for res in results:
    print(res)
