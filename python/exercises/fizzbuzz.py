def fizzbuzz():
    """ Print 1 to 100, but print Fizz for multiples of 3, Buzz for 5
        and FizzBuzz for multiples of both. """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
    return


if __name__ == '__main__':
    fizzbuzz()
