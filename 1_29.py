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
    for i in range(poss_factors):
        y=(number%poss_factors[x])
        x=x+1
    if y == 0:
        print(y)

Factor()