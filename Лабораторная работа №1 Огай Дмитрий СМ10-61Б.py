import math
import sys

print("Напишите пожалуйста первый коеффициент")
a= int(input())
print("Напишите пожалуйста второй коеффициент")
b= int(input())
print("Напишите пожалуйста третий коеффициент")
c= int(input())
print("Вы ввели а,b,c ",a,b,c)
d=b**2-(4*a*c)
print("Д:",d)
if d > 0 :
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    if (x1 > 0) and (x2 > 0) :
        print("4 kornya")
        x1kon1=math.sqrt(x1)
        x1kon2=(-x1kon1)
        print("x1:",x1kon1,"x2;",x1kon2)
        x2kon1=math.sqrt(x2)
        x2kon2=(-x2kon1)
        print("x3:",x2kon1,"x3;",x2kon2)
    elif x1 < 0 :
        print("2 kornya")
        x2kon1=math.sqrt(x2)
        x2kon2=(-x2kon1)
        print("x1:",x2kon1,"x2;",x2kon2)
    elif x2 < 0: 
        print("2 kornya")
        x1kon1=math.sqrt(x1)
        x1kon2=(-x1kon1)
        print("x1:",x1kon1,"x2;",x1kon2)
    elif (x1 < 0) and (x2 < 0) :
        print("Net korney")
elif d==0:
    print("1 корень")
else:
    print("Нет корней")