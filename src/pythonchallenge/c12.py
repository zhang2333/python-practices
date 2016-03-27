from urllib import request

img = 'http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx'
with request.urlopen(img) as f:
    data = f.read()
    print(data)
    for i in range(5):
        file = open('evil_%d.jpg' % i, 'wb')
        file.write(data[i::5])
        file.close()
