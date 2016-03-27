from urllib import request
from PIL import Image

with request.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/wire.png') as f:
    im = Image.open(f)

im_pixels = list(im.getdata())

im_target = Image.new(im.mode, (100, 100))
im_target_pixels = im_target.load()

record = [[0 for n in range(100)] for m in range(100)]

# right, down, left, up
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d = 0
# position
x = -1
y = 0

for i in range(100 * 100):
    if ((not -1 < x + dirs[d][0] < 100) and (i > 0)) or (not -1 < y + dirs[d][1] < 100) \
            or (record[x + dirs[d][0]][y + dirs[d][1]] == 1):
        d = (d + 1) % 4
    x += dirs[d][0]
    y += dirs[d][1]
    im_target_pixels[x, y] = im_pixels[i]
    record[x][y] = 1

im_target.show()
