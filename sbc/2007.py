def main():
    N = int(input())
    S = len(list(set([i for i in input()])))
    print('Yes') if S >= 3 else print('No')
	

if __name__ == "__main__":
    main()
