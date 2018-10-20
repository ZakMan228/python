#Задание_1
s = input("enter string: ")
try:
    print(s[2], s[-2], s[0:5], s[:-2],
          s[0::2], s[1::2], s[::-1],
          s[::-2], s[-2:0:-1],
          len(s), sep='\n')
except IndexError:
    print("string is short...")

#Задание_2
import math
s = input("Enter string ")
mid_index = math.ceil(len(s) / 2)
part1 = s[0:mid_index]
part2 = s[mid_index:]
s2 = part2+part1
print(s2)

#Задание_3
#3.1
counter = 0
while counter < 11:
    print(counter)
    counter += 1

#3.2
counter = 20
while counter > 0:
    print(counter, end=' ')
    counter -=1


#Задание_4
numbers = [3, 232, 44, 8, 212, 22, 33, 4]
while len(numbers) != 0:
    print(numbers[0])
    numbers = numbers[1:]

#4.2
s = 'absolutely nothing'
while len(s) != 0:
    print(s[0], end=' ')
    s = s[1:]

#4.3
l = [444, 2, 34, 221, 1]
while len(l) != 0:
    min_element = min(l)
    print(min_element)
    l.remove(min_element)

#Задание_5
s ='''We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be.'''

words = s.split()
print("Words count is ", len(words))
for i in range(0, len(words)):
    words[i] = words[i].strip(',')

words.sort()

for word in words:
    print(word)

from collections import Counter
dict_count = Counter(words)
print(dict_count, end='')

#Задание_6
#6.1
year = int(input("Enter Year: "))
y = year
def is_year_leap(y):
    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        return False
    else:
        return True
print(is_year_leap(y))
#6.2
print("Enter sides triangle: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def triangle(a, b, c):

    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(triangle(a, b, c))

#Задание_7
print("Enter the sides of the triangle: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
def get_triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Equilateral triangle'
        if a == b or b == c or c == a:
            return 'Isosceles triangle'
        if a != b and b != c and c != a:
            return 'Versatile triangle'
    else:
        return 'Not a triangle'
print(get_triangle_type(a,b,c))

#Задание_8
#8.1
def enter_word():
    word = input('Enter word ')
    while word.strip().find(' ') != -1:
        word = input('Enter word ')
    return word
print(enter_word())

#8.2
def enter_digit():
    digit = input('Enter number: ')
    while digit.isdigit() != True:
        digit = input('Enter number: ')
    return digit
print(enter_digit())

#Задание_9
x1 = float(input('Enter x1 '))
y1 = float(input('Enter y1 '))7
x2 = float(input('Enter x2 '))
y2 = float(input('Enter y2 '))
import math
def distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return result
print(distance(x1, y1, x2, y2))