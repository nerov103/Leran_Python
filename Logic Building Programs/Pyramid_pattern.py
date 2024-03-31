# looping = 50
# for i in range(looping):
#     print(i*"*")

# =================== another example
# Define the number of rows in the pyramid
# rows = 5


# for i in range(rows):

#     for j in range(rows - i - 1):
#         print(" ", end="")

#     for j in range(2 * i + 1):
#         print("*", end="")
#     # # Move to the next line
#     print()

for i in range(0, 5):
    for x in range(0, i+1):
        print("* ", end="")
    print("\r")
