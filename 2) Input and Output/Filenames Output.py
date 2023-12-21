with open(input("file1: "), "r") as file1:
    with open(input("file2: "), "r") as file2:
        print(int(file1.readline()) + int(file2.readline()))