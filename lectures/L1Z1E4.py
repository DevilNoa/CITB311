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


# вкарване на a,b,c
a = int(input())
b = int(input())
c = int(input())

# ако а ни е  0, тогава принтирсме едното условие
if a == 0:
    print("special case")

else:
    eq_Roots(a, b, c)