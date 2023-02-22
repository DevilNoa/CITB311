#програма която решава квадратно уравнение с коефициенти който са като аргументи
#"x1|x2" - когато има два реални корена, където x1 и x2 са стойностите им - готово
#"no real roots" - когато няма реални корени - готово
#"x1" - когато има един корен, където x1 е стойността му - готово
#"special case" - когато е особен случай-готово
import math
    #функция за намиране на корените
def eq_Roots(a, b, c):
    # смятане на дискриминантата
    dis = ( b ** 2 ) - ( 4 * a * c )
    sqrt_val = math.sqrt(abs(dis))
    # решаваме и принтираме
    if dis > 0:
        print((-b + sqrt_val) / (2 * a),"|",((-b - sqrt_val) / (2 * a)))
    elif dis == 0:
        print(-b / (2 * a))
    else:
        print("no real roots")
# Driver Program
a = 1
b = 10
c = -24
# If a is 0, then incorrect equation
if a == 0:
    print("special case")
else:
    eq_Roots(a, b, c)
