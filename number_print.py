n = int(input("enter row:"))
for i in range(1, n + 1):
    line = ''
    for current_num in range(1, i + 1):
        line += str(current_num)
    print(line.rjust(n, ' '))