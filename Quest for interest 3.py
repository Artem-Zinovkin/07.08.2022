a = int(input("введите первое число "))
b = int(input("введите второе число "))
if a < b:
    d = round(a/b*100,2)
    print(f"b ={b}, a= {a} в percent =  {d}")
elif b < a:
    d = round (b/a*100,2)
    print(f"a ={a}, b= {b}. в percent =  {d}%")