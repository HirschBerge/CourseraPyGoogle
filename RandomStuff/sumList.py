
lst = [1,2,3,4,5,6,7,8,9]

def summin():
    tot = 0
    for key, num in enumerate(lst):
        tot += num
    return tot

print(summin())