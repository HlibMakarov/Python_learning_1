
import math
#print("Don`t Panic")
length = 10
width = 20
rectangle_square = length * width
print("площадь треугольника при ширине %d см. и длине %d см. равна: %d кв. см." %
      (length, width, rectangle_square))

catheter1 = 4
catheter2 = 4
hypotenuse = math.sqrt(catheter1**2 + catheter2**2)
print("Длинна гипотенузы равна: %.2f см. при длинне катетов %d и %d см. "
      %(hypotenuse, catheter1, catheter2))

radius = 42000
pi = math.pi
area_of_a_circle = (radius**2) * pi
print("Площадь круга равна: %5.2f см2 при радусе %.2f см" %(area_of_a_circle, radius))

# Домашка https://youtu.be/HL-PdDa4m6k?t=6183
# Найти результат выражения для произвольных значений a,b,c a+b*(c/2)
a = 1
b = 2
c = 3
result_1 = a + b * (c / 2)
print(result_1)
# Найти результат выражения для произвольных значений a,b (a2+b2)%2
a = 5
b = 5
result_2 = ((a**2+b**2)%2)
print(result_2)
# Найти результат выражения для произвольных значений a,b,c (a+b)/12*c%4=b
a = 1
b = 2
c = 3
result_3 = ((a + b)/ 12 * c % 4 = b)
# Найти результат выражения для произвольных значений a,b,c (a-b*c)/(a+b)%c
# Найти результат выражения для произвольных значений a,b,c |a+b|/(a-b)2-cos(c)
# Найти результат выражения для произвольных значений a,b,c (невидно ничего)

