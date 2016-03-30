from urllib import request
from PIL import Image

with request.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif') as f:
    data = f.read()
    colors = []
    for i in data[13:]:
        if i == 45:
            break
        colors.append(i)
    colors = [colors[i*3:i*3+3] for i in range(len(colors)//3)]
    for i, c in enumerate(colors):
        if c[0] == 255 and c[1] == 0 and c[2] == 255:
            print('pink index:', i)

with request.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif') as f:
    im = Image.open(f)

w, h = im.size
data = list(im.getdata())
ps = [data[i*w:i*w+w] for i in range(h)]
data = []
for line in ps:
    pos = 0
    for i, p in enumerate(line):
        if p == 195:
            pos = i - 1
            break
    data += line[pos:] + line[0:pos]
im.putdata(data)
im.show()
