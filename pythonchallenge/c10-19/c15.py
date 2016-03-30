import datetime

for i in range(100):
    n = int('1%02d6' % i)
    if n % 4 == 0 and datetime.date(n, 1, 27).weekday() == 1:
        print(n)
