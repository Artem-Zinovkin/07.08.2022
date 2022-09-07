a = int(input("введите первое число "))
b = int(input("введите второе число "))
if a < b:
    d = round(b/a,2)
    print(f"{a} меньше {b} в {d} раз")
elif b < a:
    c = round (a/b , 2)
    print((f"{b} меньше {a}  в  {c} раз"))
