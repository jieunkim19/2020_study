def print_n_times(n, *values):

    for i in range(n):

        for value in values:
            print(value)

        print()

print_n_times(3, "안녕", "fun", "파이썬")
