def GCF():
    num1=int(input("enter number 1 here: "))
    num2=int(input("enter number 2 here: "))
    less=1
    com_fact=[]
    if num1 > num2:
        for i in range(num1):
            b=(num1%less)
            a=(num2%less)
            less=less+1
            if a == 0 and b == 0:
                com_fact.append(less-1)
    elif num1 < num2:
        for i in range(num2):
            b=(num1%less)
            a=(num2%less)
            less=less+1
            if a ==0 and b ==0:
                com_fact.append(less-1)
    print(com_fact[-1])

GCF()