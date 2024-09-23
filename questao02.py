def cal_fibo(fibo):
    num1, num2 = 0, 1
    while num1 < fibo:
        num1, num2 = num2, (num1 + num2 )
    return num1 == fibo

num = int(input("Infome um número: "))

if cal_fibo(num):
    print(f"O número {num} pertence a sequencia de fibonacci!")
else:
    print(f"O número {num} não percente a sequencia de fibonacci!")