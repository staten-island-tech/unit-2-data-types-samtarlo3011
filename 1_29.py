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
    number1=int(input("type number 1 here:  "))
    number2=int(input("type number 2 here:  "))
    poss_factors1 = list(range(1,number1+1))
    poss_factors2 = list(range(1,number2+1))
    a=0
    if len(poss_factors1) > len(poss_factors2):
        for i in poss_factors1:
            x=(number1%poss_factors1[a])
            y=(number2%poss_factors2[a])
            if x == 0 and y == 0:
                common_fact=[poss_factors2[a], poss_factors1[a]]
                print(common_fact[a])
            a=a+1
    else:
        for i in poss_factors2:
            x=(number1%poss_factors1[a])
            y=(number2%poss_factors2[a])
            if x == 0 and y == 0:
                common_fact=[poss_factors2[a-1], poss_factors1[a-1]]
                print(common_fact[a])   
            a=a+1         
GCF()
""" for i in poss_factors:
y=(number%poss_factors[x])
x=x+1
if y == 0:
print(y)
if y == 0:
print(poss_factors[x-1]) """