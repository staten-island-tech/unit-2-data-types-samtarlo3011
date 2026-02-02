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
    satisfaction=input("was your service: Bad, Okay, Good, Great?")
    bill=input("How Much Was Your Bill?")
    int(bill)
    tip=0
    if satisfaction == Bad:
        tip=tip+0
    elif satisfaction == Okay:
        tip = tip+15
    elif satisfaction == Good:
        tip = tip + 20
    else:
        tip=tip+25
    int(tip)
    tip=(tip/100)
    tip=(tip+1)
    total=(bill*tip)
    print(f"bill={bill}")
    print(f"tip={tip}")
    print(f"total={total}")

tip_value()