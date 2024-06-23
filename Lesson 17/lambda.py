squared = lambda num : num * num
print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(12))

sum = lambda a, b : a + b
print(sum(4, 8))

###########
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
add20 = funcBuilder(20)

print(addTen(7))
print(add20(7))

###########

numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

###########

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

###########
from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)

names = ['Greg Gennaro', 'Percy Zhuang', 'Miggy Mogul']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)