from urllib import request
import re

with request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as resp:
    page = resp.read()
    p = re.compile(r'<!--([^>]+)-->')
    flag = False
    for m in p.finditer(str(page)):
        s = m.group().replace(r'\n', '')
        if flag:
            p1 = re.compile(r'[a-zA-Z0-9]+')
            solution = list()
            for w in p1.finditer(s):
                solution.append(w.group())
            print(''.join(solution))
        flag = True
