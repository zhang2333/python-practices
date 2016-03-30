from urllib import request
import re
import zipfile

request.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', 'channel.zip')

p = re.compile(r'[0-9]+')
FIRST = '90052'

def find_nothing(z, prev_nothing):
    arr = p.findall(get_content(z.read(fill_filename(prev_nothing))))
    if len(arr) > 0:
        return arr[0]
    return None

def get_content(bytes):
    return str(bytes, 'utf-8')

def fill_filename(nothing):
    return nothing + '.txt'

def get_comment(z, nothing):
    return z.getinfo(fill_filename(nothing)).comment

zfile = zipfile.ZipFile('channel.zip', 'r')
print('readme.txt:\n' + get_content(zfile.read('readme.txt')))

nothing = FIRST
comments = b''
while(nothing):
    print(get_content(zfile.read(fill_filename(nothing))))
    comments += get_comment(zfile, nothing)
    nothing = find_nothing(zfile, nothing)

print(comments)
