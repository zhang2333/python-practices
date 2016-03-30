from urllib import request
import re

url_format = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
MAX_TIMES = 400
fin = False

def requestCode(code, times):
    if times > MAX_TIMES:
        return

    global next_code, fin

    normal = False
    try:
        with request.urlopen(url_format + code) as resp:
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
                next_code = arr[0]
                normal = True
            else:
                # the others
                fin = True
    except Exception as e:
        print(e)
        next_code = code
    else:
        print('%d. %s' % (times, next_code))
        times += 1
        if not normal:
            print('%s | Nothing:%s' % (page, code))
    finally:
        if not fin:
            requestCode(next_code, times)

requestCode('12345', 1)
