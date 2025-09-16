T = int(input())

for i in range(T):
    line = input()
    parts = line.split()

    R = int(parts[0])
    S = parts[1]

    result = ""

    for char in S:
        for j in range(R):
            result = result + char

    print(result)