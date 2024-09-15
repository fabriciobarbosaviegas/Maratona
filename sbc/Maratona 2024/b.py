import sys
import heapq

def solve(N, M, K, graph, max_time):
    def can_visit_k_cities_in_one_night(start, K, T):
        min_times = [float('inf')] * (N + 1)
        min_times[start] = 0
        pq = [(0, start)]  # (time, node)
        visited_cities = 0
        
        while pq:
            current_time, u = heapq.heappop(pq)
            
            if current_time > min_times[u]:
                continue
            
            for v, travel_time in graph[u]:
                if travel_time > T:
                    continue
                new_time = current_time + travel_time
                if new_time < min_times[v]:
                    min_times[v] = new_time
                    heapq.heappush(pq, (new_time, v))
        
        # Check how many cities we can visit within time T
        for i in range(1, N + 1):
            if min_times[i] <= T:
                visited_cities += 1
                if visited_cities >= K:
                    return True
        
        return False
    
    # Binary search on the time
    left, right = 0, max_time
    answer = -1
    
    while left <= right:
        mid = (left + right) // 2
        if can_visit_k_cities_in_one_night(1, K, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

# Reading input
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
K = int(data[2])

graph = [[] for _ in range(N + 1)]
max_time = 0

index = 3
for _ in range(M):
    U = int(data[index])
    V = int(data[index + 1])
    C = int(data[index + 2])
    graph[U].append((V, C))
    graph[V].append((U, C))
    max_time = max(max_time, C)
    index += 3

# Solve the problem
result = solve(N, M, K, graph, max_time + 1)

# Output the result
print(result)
