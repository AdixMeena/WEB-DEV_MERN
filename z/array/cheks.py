list = [1,2,9,4,9,6]

for i in range(len(list)-2):
    if list[i] > list[i+1]:
        print("FAIL")