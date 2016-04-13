from urllib import parse
from urllib import request
from http import cookiejar
import xmlrpc.client
import re
import bz2

cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))

def get_info():
    for c in cj:
        if (c.name == 'info'):
            return c.value

    return ''

opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
print(get_info())

url_format = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
MAX_TIMES = 400
fin = False

data = ''

def requestCode(code, times):
    if times > MAX_TIMES:
        return

    global next_code, fin, data

    normal = False
    try:
        with opener.open(url_format + code) as resp:
            page = str(resp.read(), 'utf-8')
            p = re.compile(r'([0-9]+)')
            arr = p.findall(page)
            if page.find('Divide') != -1:
                # Yes. Divide by two and keep going.
                next_code = str(int(code) // 2)
            elif page.find('misleading') != -1:
                # There maybe misleading numbers in the text.
                next_code = arr[1]
            elif page.find('.html') != -1:
                # solution
                fin = True
            elif len(arr) > 0:
                if arr[0] == '4':
                    next_code = arr[1]
                else:
                    next_code = arr[0]
                normal = True
            else:
                # the others
                fin = True
    except Exception as e:
        print(e)
        next_code = code
    else:
        data += get_info()
        print('%d. %s' % (times, next_code))
        times += 1
        if not normal:
            print('%s | Nothing:%s' % (page, code))
    finally:
        if not fin:
            requestCode(next_code, times)
        else:
            print('1:', bz2.decompress(parse.unquote_to_bytes(data.replace('+', '%20'))).decode('ascii'))

requestCode('12345', 1)

x = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print('2:', x.phone('Leopold'))

req = request.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
req.add_header('Cookie', 'info=the flowers are on their way')
with request.urlopen(req) as f:
    print('3:', f.read())
