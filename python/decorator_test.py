def me_seeks(func):
    print('hi im mr.meeseeks!')
    return func

@me_seeks
def print_str(str):
    return print(str)

if __name__ == '__main__':
    print_str('test')