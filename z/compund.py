ogamount = float(input("How much you take: "))
time = float(input("for how long: "))
intrst = float(input("whts the intrest: "))

result = ogamount * pow(1 + time/100, intrst)
print(result)