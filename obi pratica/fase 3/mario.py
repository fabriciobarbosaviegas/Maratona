def main():
    while True:
        length = int(input("Height: "))

        if length > 0 and length < 8:
            break

    for i in range(length):
        print(f"{' '*(length-i-1)}{'#'*(i+1)}  {'#'*(i+1)}")



if __name__ == "__main__":
    main()