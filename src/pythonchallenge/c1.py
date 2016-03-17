# -*- coding:utf-8 -*-

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# method A
arr = list(raw)
for k, v in enumerate(arr):
    n = ord(v)
    if n <= ord('z') and n >= ord('a'):
        arr[k] = chr((n - 97 + 2) % 26 + ord('a'))
print(''.join(arr))

# method B
intab = ''.join([chr(c) for c in range(97, 123)])
outtab = ''.join([chr(c > 122 and (c % 123 + 97) or c) for c in range(97 + 2, 123 + 2)])
trantab = ''.maketrans(intab, outtab)
print(raw.translate(trantab))
solution = 'map'.translate(trantab)
print(solution)
