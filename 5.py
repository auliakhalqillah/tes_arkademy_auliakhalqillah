# Function to generate fibonacci series
def fibo(col,row):
    f1 = 0
    f2 = 1
    N = col*row
    n = int(N)
    fibonacci = [f1,f2]
    i = 0
    while i < n-2:
        f = f1 + f2
        f1 = f2
        f2 = f
        fibonacci.append(f)
        i = i + 1

    fib = []
    j = 0
    k = 0
    l = col
    while j < row:
        ff = fibonacci[k:l]
        k = k + col
        l = l + l
        j = j + 1
        fib.append(ff)

    for kk in range(row):
        for ll in range(col):
            print(fib[kk][ll], end = ",")
        print()


# Main program
col = 4
row = 3
fibo(col,row)
