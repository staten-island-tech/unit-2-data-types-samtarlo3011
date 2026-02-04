def GCF():
    number1=int(input("type number 1 here:  "))
    number2=int(input("type number 2 here:  "))
    poss_factors1 = list(range(1,number1+1))
    poss_factors2 = list(range(1,number2+1))
    a=0
    if poss_factors1 > poss_factors2:
        for i in poss_factors1:
            x=(number1%poss_factors1[a])
            y=(number2%poss_factors2[a])
            a=a+1
            if x == 0 and y == 0:
                common_fact=[poss_factors2[a-1], poss_factors1[a-1]]
                print(common_fact[a-3])
    else:
        for i in poss_factors2:
            x=(number1%poss_factors1[a])
            y=(number2%poss_factors2[a])
            a=a+1
            if x == 0 and y == 0:
                common_fact=[poss_factors2[a-1], poss_factors1[a-1]]
                print(common_fact[a-3])            
GCF()