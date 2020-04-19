
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

y = 2
x = 4
sum_x_y = y + x
print(sum_x_y)