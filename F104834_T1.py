#програма която решава квадратно уравнение с коефициенти който са като аргументи
#"x1|x2" - когато има два реални корена, където x1 и x2 са стойностите им
#"no real roots" - когато няма реални корени
#"x1" - когато има един корен, където x1 е стойността му
#"special case" - когато е особен случай
#https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/
import math

#дефиниция
def eq_Roots(a,b,c):

    #смятан на дискриминанта
        dis = b * b - 4 * a * c
        sqrt_value = math.sqrt(abs(dis))

    #проверка за два или ени корен
    print((-b + sqrt_value)/(2 * a))
