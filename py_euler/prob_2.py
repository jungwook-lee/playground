# Even Fibonacci numbers of values less than 4M

def fib_num_gen(num):
    """ Generates fibonacci numbers for all numbers less than num """
    fib_1 = 0
    fib_2 = 1
    while (fib_2 < num):
        n_fib = fib_1 + fib_2
        fib_1, fib_2 = fib_2, n_fib
        yield fib_2
        
num = 4000000
fib_arr = [i for i in fib_num_gen(num) if (i & 1) == 0]
print(sum(fib_arr))

# Even better solution
def even_fib_gen(num):
    total = 0
    a = 1
    b = 1
    c = a + b
    while (c < num):
        total += c
        a = b + c
        b = c + a
        c = b + a
    return total

print(even_fib_gen(num))
