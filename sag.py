# a1, b1= map(float, input("Введите координаты точки A:").split())
# a2, b2= map(float, input("Введите координаты точки B:").split())
# c1=a1-a2
# c2=b1-b2
# x=(c1**2+c2**2)**1.5
# print("Длина отрезка AB = ", x)
#
# a, b,c, d,e= map(float, input("Введите:").split())
# if(a>b)and(a>c)and(a>d)and(a>e):
#     print(a)
# elif(b>a)and(b>c)and(b>d)and(b>e):
#     print(b)
# elif(c>a)and(c>b)and(c>d)and(c>e):
#     print(c)
# elif(d>a)and(d>c)and(d>b)and(d>e):
#     print(d)
# elif(e>a)and(e>c)and(e>d)and(e>b):
#     print(e)
#
# A=int(input("Возраст Антона:"))
# B=int(input("Возраст Бориса:"))
# C=int(input("Возраст Виктора:"))
# if(A>B)and(a>C):
#     print("Антон старше всех")
# elif(B>A)and(B>C):
#     print("Борис старше всех")
# elif(C>A)and(C>B):
#     print("Виктория старше всех")
# elif (C==A) and (C > B):
#     print("Виктора и Антон старше Бориса")
# elif (C>A) and (C == B):
#     print("Виктора и Борис старше Антона")
# elif (B==A) and (B > C):
#     print("Борис и Антон старше Вироники")

voz=int(input("Введите ваш возраст : "))
n=voz%100
n1=n%10
if (voz>-1)and (voz<120):
    if (n1==1):
        print(f"Вам {voz} год")
    elif (n >= 11 and n < 19):
        print(f"Вам {voz} лет")
    elif (n1 > 1 and n1 <5):
        print(f"Вам {voz} года")
    else:
        print(f"Вам {voz} лет")
else:
    print("не может быть")

