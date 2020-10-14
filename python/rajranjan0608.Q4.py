print("Welcome to Star Show. Which flag is this?")
for _ in range(2):
    for i in range(6):
        if i != 0:
            for j in range(i):
                print('*', end = " ")
            print()
