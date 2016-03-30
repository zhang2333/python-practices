# a = [1, 11, 21, 1211, 111221,
# len(a[30]) = ?

def compute_next(num):
    num = str(num)
    next_num = ''
    guard = None
    count = None
    for i in range(len(num)):
        if num[i] == guard:
            count += 1
            continue

        if guard:
            next_num += str(count) + guard
        guard = num[i]
        count = 1

    next_num += str(count) + guard

    return int(next_num)

def generate(max):
    arr = [1]
    for i in range(max):
        if i != 0:
            arr.append(compute_next(arr[i-1]))
    return arr

print(len(str(generate(31)[30])))
