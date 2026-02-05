""" x = "this is a thing"
y= x.split( )
z = y[1]
print(y)
print(z) """

def wordcount():
    sentence=input("write sentence here:")
    y=sentence.split( )
    x=0
    for i in (y):
        x=x+1
    print(x)

def odd_or_even():
    number=input("enter a number: ")
    odd_even=(int(number) % 2)
    if (odd_even) == 1:
        print("odd")
    else:
        print("even")
def tip_value():
    satisfaction=input("was your service: Bad, Okay, Good, Great? ")
    bill=float(input("How Much Was Your Bill? "))
    tip=0
    if satisfaction == "Bad":
        tip=tip+0
    elif satisfaction == "Okay":
        tip = tip+15
    elif satisfaction == "Good":
        tip = tip + 20
    elif satisfaction == "Great":
        tip=tip+25
    tip=(tip/100)
    tip=(tip+1)
    total=(bill*float(tip))
    tip=(float(total)-float(bill))
    print(f"bill={bill}")
    print(f"tip={tip}")
    print(f"total={total}")
def Factor():
    number=int(input("type number here: "))
    poss_factors = list(range(1,number+1))
    x=0
    for i in poss_factors:
        y=(number%poss_factors[x])
        x=x+1
        if y == 0:
            print(poss_factors[x-1])
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
tip_value()
odd_or_even()
Factor()
wordcount()
GCF()