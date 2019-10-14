# http://satyajit.ranjeev.in/2012/05/17/python-a-few-things-to-remember.html

freqs = {}
for c in "abracadabra":
    try:
        freqs[c] += 1
    except:
        freqs[c] = 1
print(freqs)

# better solution
freqs = {}
for c in "abracadabra":
    freqs[c] = freqs.get(c, 0) + 1
print(freqs)

# or just use collections
from collections import defaultdict
freqs = defaultdict(int)
for c in "abracadabra":
    freqs[c] += 1
print(freqs)

# or also use counter
from collections import Counter
c = Counter("abracadabra")
print(c['a'])

