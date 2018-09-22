# Задание 1
#1
print(str.isdigit('fdsgffd43543gdfs'))

#2
c = 'fdsfdg  g.fd.  g.f  gdf  gf !! '
print(c.count(" "))

#3
c = 'fdsfdg  g.fd.  g.f  gdf  gf !! '
print(c.count("."))

#4
print(str.center('Homework', 100))

#5
print(str.title('hfjkdshjk hHHhh bbBB bb BBB'))

#Задание 2
#1
a = 179
b = 971
c = (a**2 + b**2)**0.5
print(c)

#2
x = int(input("Enter number: "))
y = x % 100
print (int(y // 10))

#3
x = int(input("Enter number ***: "))
s = str(x)
a = int(s[0])
b = int(s[1])
c = int(s[2])
print(a+b+c)

#4
str=int(input("Enter number n: "))
print(str+2-(str%2))

#5

x = 3.1414242443
print(str(x - int(x))[2:])

#6
x = float(input("Enter float number"))
k = int(x)
if k == 0:
    y = x * 10
    z = int(y)
    print (z)
if k > 0:
    print (int(10 * (x - int(x))))

#Задание 3
y = int(input("Enter Year: "))
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("NO")
else:
    print("YES")

#Задание 4
print("Enter the sides of the triangle: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

#Задание 5
print("Enter numbers : ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b ,c)

#Задание 6
print("Enter numbers : ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a == b == c:
    print("3")
elif a == b or a == c or b == c:
    print("2")
else:
    print("0")
