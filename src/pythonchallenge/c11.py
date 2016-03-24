from urllib import request
from PIL import Image

# build opener
auth = request.HTTPBasicAuthHandler()
auth.add_password(realm='inflate', uri='http://www.pythonchallenge.com', user='huge', passwd='file')
opener = request.build_opener(auth)
request.install_opener(opener)


with request.urlopen('http://www.pythonchallenge.com/pc/return/cave.jpg') as f:
    im = Image.open(f)

# process image
w, h = im.size

even = Image.new(im.mode, im.size)

im_pixels = im.load()
even_pixels = even.load()

for i in range(w):
    for j in range(h):
        if i % 2 and j % 2:
            even_pixels[i, j] = im_pixels[i, j]

even.show()
