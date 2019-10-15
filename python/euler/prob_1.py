# Find sum of all multiples of 3 or 5 below 1000

# Naive counting approach
def multiples_of_3_5(num):
    tot_sum = 0
    for i in range(num):
        if (i % 3) == 0:
            tot_sum += i
        elif (i % 5) == 0:
            tot_sum += i
    return tot_sum

# Try using comprehension
total_sum = sum([i for i in range(1000) if (i % 3) == 0 or 
                                           (i % 5) == 0])

# Test
print(multiples_of_3_5(10))
print(multiples_of_3_5(1000))
print(total_sum)
