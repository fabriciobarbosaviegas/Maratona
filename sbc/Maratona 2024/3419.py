def convert_to_milliseconds(time_str):
    """Convert time from M:S:MS format to milliseconds."""
    minutes, seconds, milliseconds = map(int, time_str.split(':'))
    return (minutes * 60 * 1000) + (seconds * 1000) + milliseconds

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, V = map(int, data[0].split())
    pilots_times = []
    for i in range(1, N + 1):
        parts = data[i].split()
        pilot_number = int(parts[0])
        times = [convert_to_milliseconds(parts[j]) for j in range(1, V + 1)]
        pilots_times.append((pilot_number, times))
    
    # Find the best lap time and the corresponding pilot
    best_time = float('inf')
    best_pilot = -1
    for pilot, times in pilots_times:
        for time in times:
            if time < best_time:
                best_time = time
                best_pilot = pilot
    
    # Determine the positions (sort by sum of times)
    total_times = [(pilot, sum(times)) for pilot, times in pilots_times]
    total_times.sort(key=lambda x: x[1])
    
    # Check if the best pilot is within the top 10
    top_10_pilots = {total_times[i][0] for i in range(min(10, N))}
    
    if best_pilot in top_10_pilots:
        print(best_pilot)
    else:
        print("NENHUM")

if __name__ == "__main__":
    main()
