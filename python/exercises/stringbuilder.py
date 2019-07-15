import timeit

class StringBuilder(object):
    def __init__(self):
        self.str_list = []

    def __str__(self):
        str_out = ''
        for word in self.str_list:
            str_out = str_out + word
        return str_out

    def add(self, word):
        self.str_list.append(word)

def stringbuilder(words):
    sentence = StringBuilder()
    for word in words:
        sentence.add(word)
    return str(sentence)

# list comprehension for fastest method: https://waymoot.org/home/python_string/
def stringbuilder_better(words):
    return ''.join([words[i] for i in xrange(len(words))])


if __name__ == '__main__':
    words = ['01010100010100010001010' for _ in xrange(10000)]

    print (timeit.timeit(stringbuilder(words)))
    print (timeit.timeit(stringbuilder_better(words)))


