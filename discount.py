def discount():
    age = int(input("enter age: "))
    card = input("are you a season pass holder/resident?(Yes or No) ")
    if age <12 or age >65 or card==("Yes"):
        print("apply discount")
    else:
        print("do not apply discount")
discount()