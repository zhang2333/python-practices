from urllib import request
import re

with request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as f:
    page = f.read()
    p = re.compile(r'<!--([^>]+)-->')
    for m in p.finditer(str(page)):
        s = m.group().replace(r'\n', '')
        p1 = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
        solution = list()
        for w in p1.findall(s):
            solution.append(w)
        print(''.join(solution))
