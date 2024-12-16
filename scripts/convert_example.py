if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    for line in lines:
        print(f'        "{line}",')
