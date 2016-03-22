from urllib import request
from PIL import Image
import re

with request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png') as f:
    im = Image.open(f)

w, h = im.size
gray_line_filter = filter(lambda p: p[1][0] == p[1][1] == p[1][2] and p[0] > w * 42, enumerate(im.getdata()))
gray_line = [p[1][0] for p in list(gray_line_filter)[:w]]
filtered = filter(lambda x: x[0] % 7 == 0, enumerate(gray_line))
char_arr = [chr(x[1]) for x in filtered]
key = ''.join(char_arr)
p = re.compile(r'[0-9]+')
next = [chr(int(x)) for x in p.findall(key)]
print(''.join(next))
