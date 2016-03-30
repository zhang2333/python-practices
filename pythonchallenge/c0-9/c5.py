import pickle
from urllib import request

with request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as resp:
    obj = pickle.load(resp)
    for row in obj:
        print(''.join(map(lambda x: x[0] * x[1], row)))
